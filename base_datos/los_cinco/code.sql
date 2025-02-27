DROP TABLE IF EXISTS title_episode;
DROP TABLE IF EXISTS title_basics;
DROP TABLE IF EXISTS title_principals;
DROP TABLE IF EXISTS name_basics;

CREATE TABLE title_episode (
    tconst VARCHAR(20) PRIMARY KEY,
    parentTconst VARCHAR(20),
    seasonNumber INTEGER,
    episodeNumber INTEGER
);

CREATE TABLE title_basics (
    tconst VARCHAR(20) PRIMARY KEY,
    titleType VARCHAR(50),
    primaryTitle VARCHAR(255),
    originalTitle VARCHAR(255),
    isAdult INTEGER,
    startYear INTEGER,
    endYear INTEGER,
    runtimeMinutes INTEGER,
    genres VARCHAR(255)
);

CREATE TABLE title_principals (
    tconst VARCHAR(20),
    ordering INTEGER,
    nconst VARCHAR(20),
    category VARCHAR(50),
    job VARCHAR(255),
    characters TEXT
);

CREATE TABLE name_basics (
    nconst VARCHAR(20) PRIMARY KEY,
    primaryName VARCHAR(255),
    birthYear INTEGER,
    deathYear INTEGER,
    primaryProfession VARCHAR(255),
    knownForTitles VARCHAR(255)
);


COPY title_episode
FROM 'D:\usuaris\a.lopez.g\trabajos\dataScienceCarlemany\base_datos_01\week_03\title.episode.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

SELECT *
FROM title_episode
LIMIT 10;


--sed -i.bak "s/'//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/title.basics.tsv
--sed -i.bak "s/\"//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/title.basics.tsv

ALTER TABLE title_basics
ALTER COLUMN primarytitle TYPE VARCHAR(1024);  -- O TEXT

ALTER TABLE title_basics
ALTER COLUMN originaltitle TYPE VARCHAR(1024);  -- O TEXT

COPY title_basics
FROM 'D:\usuaris\a.lopez.g\trabajos\dataScienceCarlemany\base_datos_01\week_03\title.basics.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

SELECT *
FROM title_basics
LIMIT 10;

--sed -i.bak "s/'//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/title.principals.tsv
--sed -i.bak "s/\"//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/title.principals.tsv

ALTER TABLE title_principals
ALTER COLUMN job TYPE VARCHAR(1024);  -- O TEXT

COPY title_principals
FROM 'D:\usuaris\a.lopez.g\trabajos\dataScienceCarlemany\base_datos_01\week_03\title.principals.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

--sed -i.bak "s/'//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/name.basics.tsv
--sed -i.bak "s/\"//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/name.basics.tsv

ALTER TABLE name_basics
ALTER COLUMN primaryname TYPE VARCHAR(2048);  -- O TEXT
COPY name_basics
FROM 'D:\usuaris\a.lopez.g\trabajos\dataScienceCarlemany\base_datos_01\week_03\name.basics.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';

ANALYZE title_episode;
ANALYZE title_basics;
ANALYZE title_principals;
ANALYZE name_basics;

-- Índice en title_episode.parentTconst para acelerar el JOIN con title_basics
CREATE INDEX idx_title_episode_parentTconst ON title_episode(parentTconst);

-- Índice compuesto en title_principals para acelerar el filtrado por categoría y el JOIN por tconst
CREATE INDEX idx_title_principals_tconst_category ON title_principals(tconst, category);

-- (Opcional) Índice en title_principals.nconst para optimizar los JOIN con name_basics
CREATE INDEX idx_title_principals_nconst ON title_principals(nconst);



--1. TOP 10 Series con más directores diferentes

SELECT 
b.primaryTitle AS serie, 
COUNT(DISTINCT np.nconst) AS num_directores
FROM title_episode e
JOIN title_basics b ON e.parentTconst = b.tconst
JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'
JOIN name_basics np ON p.nconst = np.nconst
GROUP BY b.primaryTitle
ORDER BY num_directores DESC
LIMIT 10;

--2. TOP 10 Guionistas que repiten serie
SELECT
b.primaryTitle AS serie, 
np.primaryName AS guionista, 
COUNT(*) AS num_episodios
FROM title_episode e
JOIN title_basics b ON e.parentTconst = b.tconst
JOIN title_principals p ON e.tconst = p.tconst AND p.category IN ('writer', 'screenplay')
JOIN name_basics np ON p.nconst = np.nconst
GROUP BY b.primaryTitle, np.primaryName
ORDER BY num_episodios DESC
LIMIT 10;

--3. TOP 10 Series con más episodios dirigidos por el mismo director

SELECT 
b.primaryTitle AS serie, 
np.primaryName AS director, 
COUNT(*) AS num_episodios
FROM title_episode e
JOIN title_basics b ON e.parentTconst = b.tconst
JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'
JOIN name_basics np ON p.nconst = np.nconst
GROUP BY b.primaryTitle, np.primaryName
ORDER BY num_episodios DESC
LIMIT 10;



-- 4. TOP 10 series con más personas involucradas (en total) a lo largo de sus episodios
SELECT 
b.primaryTitle AS serie,
COUNT(DISTINCT p.nconst) AS total_personas_involucradas
FROM title_episode e
JOIN title_basics b 
ON e.parentTconst = b.tconst
JOIN title_principals p 
ON e.tconst = p.tconst
JOIN name_basics np 
ON p.nconst = np.nconst
GROUP BY b.primaryTitle
ORDER BY total_personas_involucradas DESC
LIMIT 10;

--5. TOP 10 Series con más episodios sin director conocido

SELECT 
b.primaryTitle AS serie, 
COUNT(*) AS num_episodios_sin_director
FROM title_episode e
JOIN title_basics b ON e.parentTconst = b.tconst
LEFT JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'
WHERE p.nconst IS NULL
GROUP BY b.primaryTitle
ORDER BY num_episodios_sin_director DESC
LIMIT 10;


--6. TOP 10 Series con más episodios dirigidos por diferentes directores
SELECT 
b.primaryTitle AS serie, 
COUNT(DISTINCT np.nconst) AS num_directores, 
COUNT(e.tconst) AS num_episodios
FROM title_episode e
JOIN title_basics b ON e.parentTconst = b.tconst
JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'
JOIN name_basics np ON p.nconst = np.nconst
GROUP BY b.primaryTitle
ORDER BY num_directores DESC
LIMIT 10;
