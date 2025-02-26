-- Eliminar tablas si ya existen
DROP TABLE IF EXISTS title_crew;
DROP TABLE IF EXISTS title_basics;
DROP TABLE IF EXISTS title_principals;
DROP TABLE IF EXISTS name_basics;




CREATE TABLE title_crew (
    tconst VARCHAR(15) NOT NULL PRIMARY KEY,
    directors TEXT,
    writers TEXT
);


CREATE TABLE title_basics (
    tconst VARCHAR(15) NOT NULL PRIMARY KEY,
    titleType VARCHAR(20),
    primaryTitle TEXT,
    originalTitle TEXT,
    isAdult BOOLEAN,
    startYear SMALLINT,
    endYear SMALLINT,
    runtimeMinutes INT,
    genres VARCHAR(255)
);

CREATE TABLE title_principals (
    tconst VARCHAR(15) NOT NULL,
    ordering SMALLINT,
    nconst VARCHAR(15),
    category VARCHAR(20),
    job TEXT,
    characters TEXT,
    PRIMARY KEY (tconst, ordering)
);


CREATE TABLE name_basics (
    nconst VARCHAR(15) NOT NULL PRIMARY KEY,
    primaryName TEXT,
    birthYear SMALLINT,
    deathYear SMALLINT,
    primaryProfession VARCHAR(255),
    knownForTitles VARCHAR(255)
);




COPY title_crew
FROM '/tmp/title.crew.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

COPY title_basics
FROM '/tmp/title.basics.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

-- Quitadas las comillas dobles y simples
--sed -i '' 's/"//g' /tmp/title.basics.tsv
--sed -i '' "s/'//g" /tmp/title.basics.tsv

COPY title_principals
FROM '/tmp/title.principals.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

--sed -i '' 's/"//g' /tmp/title.principals.tsv
--sed -i '' "s/'//g" /tmp/title.principals.tsv

COPY name_basics
FROM '/tmp/name.basics.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

------


-----
-- Optimizar estadísticas de consulta. Esto ayuda a PostgreSQL a optimizar el uso de índices en futuras consultas.
ANALYZE title_crew;
ANALYZE title_basics;
ANALYZE title_principals;
ANALYZE name_basics;

-- Crear índices para mejorar rendimiento en consultas. Creando un indice de lingitud limitada
CREATE INDEX idx_title_basics_type ON title_basics(titleType varchar_pattern_ops);
CREATE INDEX idx_title_principals_nconst ON title_principals(nconst);
CREATE INDEX idx_name_basics_primaryName ON name_basics(SUBSTRING(primaryName FROM 1 FOR 100));



--- Consulto para ver si se puede optimizar algun TEXTO en title_principals
SELECT 
    MAX(LENGTH(category)) AS max_category,
    MAX(LENGTH(tconst)) AS max_tconst,
    MAX(LENGTH(ordering::TEXT)) AS max_ordering,
    MAX(LENGTH(nconst)) AS max_nconst,
    MAX(LENGTH(job)) AS max_job,
    MAX(LENGTH(characters)) AS max_characters
FROM title_principals;

--- Analizar mejora TEXT y otros varchar
ALTER TABLE title_principals 
ALTER COLUMN category TYPE VARCHAR(25),
ALTER COLUMN job TYPE VARCHAR(300),
ALTER COLUMN characters TYPE VARCHAR(1500);



SELECT 
    MAX(LENGTH(tconst)) AS max_tconst,
    MAX(LENGTH(directors)) AS max_directors,
    MAX(LENGTH(writers)) AS max_writers
FROM title_crew;

ALTER TABLE title_crew 
ALTER COLUMN directors TYPE VARCHAR(5000),
ALTER COLUMN writers TYPE VARCHAR(15000);


SELECT 
    MAX(LENGTH(tconst)) AS max_tconst,
    MAX(LENGTH(titleType)) AS max_titleType,
    MAX(LENGTH(primaryTitle)) AS max_primaryTitle,
    MAX(LENGTH(originalTitle)) AS max_originalTitle,
    MAX(LENGTH(genres)) AS max_genres
FROM title_basics;

ALTER TABLE title_basics 
ALTER COLUMN titleType TYPE VARCHAR(15),
ALTER COLUMN primaryTitle TYPE VARCHAR(500),
ALTER COLUMN originalTitle TYPE VARCHAR(500),
ALTER COLUMN genres TYPE VARCHAR(50);


SELECT 
    MAX(LENGTH(nconst)) AS max_nconst,
    MAX(LENGTH(primaryName)) AS max_primaryName,
    MAX(LENGTH(primaryProfession)) AS max_primaryProfession,
    MAX(LENGTH(knownForTitles)) AS max_knownForTitles
FROM name_basics;


-- Verificar la carga de datos
SELECT COUNT(*) AS total_filas_title_crew FROM title_crew;
SELECT COUNT(*) AS total_filas_title_basics FROM title_basics;
SELECT COUNT(*) AS total_filas_title_principals FROM title_principals;
SELECT COUNT(*) AS total_filas_name_basics FROM name_basics;

-- Comprobar si es un error
SELECT * FROM name_basics WHERE LENGTH(primaryName) > 1000 LIMIT 10;


-- Truncar los valores para que no esten por encima de 500
UPDATE name_basics
SET primaryName = LEFT(primaryName, 500)
WHERE LENGTH(primaryName) > 500;

-- Confirmamos que se ha ejecutado
SELECT * FROM name_basics WHERE LENGTH(primaryName) > 1000 LIMIT 10;

ALTER TABLE name_basics 
ALTER COLUMN primaryName TYPE VARCHAR(500);

-- Compruebo que no se ha acortado mas de la cuenta
SELECT nconst, primaryName 
FROM name_basics 
ORDER BY LENGTH(primaryName) DESC 
LIMIT 10;

ROLLBACK;