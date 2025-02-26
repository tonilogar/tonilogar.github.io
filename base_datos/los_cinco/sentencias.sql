1. TOP 10 Series con más directores diferentes


-- Selecciona el título principal de la serie y el número de directores únicos asociados a ella.
SELECT 
    b.primaryTitle AS serie,                -- Toma el título principal de la serie desde la tabla "title_basics" y lo renombra como "serie".
    COUNT(DISTINCT np.nconst) AS num_directores  -- Cuenta de forma única (DISTINCT) la cantidad de directores, usando el identificador "nconst" de "name_basics".
FROM title_episode e                         -- Inicia desde la tabla "title_episode" (alias "e"), que relaciona cada episodio con su serie.
JOIN title_basics b ON e.parentTconst = b.tconst  -- Une "title_episode" con "title_basics" (alias "b") usando "parentTconst" para identificar a qué serie pertenece el episodio.
JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'
    -- Une la tabla "title_episode" con "title_principals" (alias "p") para obtener los registros donde el rol es 'director'.
JOIN name_basics np ON p.nconst = np.nconst   -- Une "title_principals" con "name_basics" (alias "np") usando "nconst" para obtener los detalles reales del director.
GROUP BY b.primaryTitle                      -- Agrupa los resultados por el título de la serie para que se cuente el número de directores por serie.
ORDER BY num_directores DESC                 -- Ordena los resultados de mayor a menor según el número de directores.
LIMIT 10;                                    -- Limita la salida a las 10 series que tengan más directores.

Razonamiento:

title_episode: Permite relacionar cada episodio con la serie (a través de parentTconst).
title_basics: Se usa para obtener el nombre o título de la serie.
title_principals: Filtra los roles para quedarnos solo con los directores (campo category = 'director').
name_basics: Nos aporta el nombre real del director a partir de su ID (nconst).
Esta consulta cumple el requisito al unir cuatro fuentes y es comprensible para alguien que está empezando.

2. TOP 10 Guionistas que repiten serie

-- Selecciona el título principal de la serie, el nombre del guionista y el número de episodios en que participó.
SELECT 
    b.primaryTitle AS serie,             -- Selecciona el título principal de la serie desde "title_basics" y lo renombra como "serie".
    np.primaryName AS guionista,           -- Selecciona el nombre del guionista desde "name_basics" y lo renombra como "guionista".
    COUNT(*) AS num_episodios              -- Cuenta el número total de registros (episodios) asociados a cada combinación de serie y guionista.
FROM title_episode e                      -- Usa la tabla "title_episode" (alias "e") para relacionar episodios con series.
JOIN title_basics b ON e.parentTconst = b.tconst  
    -- Une "title_episode" con "title_basics" (alias "b") para obtener el título de la serie a partir de la clave "parentTconst".
JOIN title_principals p ON e.tconst = p.tconst AND p.category IN ('writer', 'screenplay')
    -- Une "title_episode" con "title_principals" (alias "p") para filtrar aquellos registros en los que la categoría es 'writer' o 'screenplay'.
JOIN name_basics np ON p.nconst = np.nconst  
    -- Une "title_principals" con "name_basics" (alias "np") para obtener el nombre real del guionista usando el identificador "nconst".
GROUP BY b.primaryTitle, np.primaryName  
    -- Agrupa los resultados por título de la serie y nombre del guionista para contar los episodios correspondientes a cada combinación.
ORDER BY num_episodios DESC            -- Ordena los resultados de mayor a menor según la cantidad de episodios en los que aparece el guionista.
LIMIT 10;                               -- Muestra solo los 10 primeros resultados.

Razonamiento:

Se utiliza title_episode para identificar la relación episodio-serie.
title_basics aporta el nombre de la serie.
title_principals filtra aquellos registros donde el rol es de guionista (puedes considerar tanto 'writer' como 'screenplay').
name_basics traduce el identificador del guionista a su nombre.
Con esto se cumple el uso de al menos tres fuentes, mostrando para cada serie qué guionista participa en más episodios.

3. TOP 10 Series con más episodios dirigidos por el mismo director


-- Selecciona el título de la serie, el nombre del director y la cantidad de episodios que ha dirigido en esa serie.
SELECT 
    b.primaryTitle AS serie,               -- Obtiene el título principal de la serie desde la tabla title_basics y lo renombra como "serie".
    np.primaryName AS director,              -- Obtiene el nombre del director desde la tabla name_basics y lo renombra como "director".
    COUNT(*) AS num_episodios                -- Cuenta el número total de episodios en que ese director ha trabajado en la serie.
FROM title_episode e                        -- Utiliza la tabla title_episode (alias "e") para relacionar episodios con series.
JOIN title_basics b ON e.parentTconst = b.tconst  
    -- Une title_episode con title_basics (alias "b") mediante el campo parentTconst para identificar a qué serie pertenece cada episodio.
JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'
    -- Une title_episode con title_principals (alias "p") y filtra aquellos registros en los que el rol es "director".
JOIN name_basics np ON p.nconst = np.nconst   
    -- Une title_principals con name_basics (alias "np") para obtener el nombre real del director a partir del identificador nconst.
GROUP BY b.primaryTitle, np.primaryName   
    -- Agrupa los resultados por el título de la serie y el nombre del director para contar la cantidad de episodios por cada combinación.
ORDER BY num_episodios DESC                   -- Ordena los resultados de mayor a menor según el número de episodios dirigidos.
LIMIT 10;                                     -- Limita la salida a las 10 combinaciones principales.

Razonamiento:

title_episode y title_basics se usan para identificar la serie a la que pertenece cada episodio.
title_principals se encarga de filtrar el rol de director en cada episodio.
name_basics aporta el nombre del director.
Esta consulta identifica en cada serie al director que ha dirigido más episodios, integrando cuatro datasets.

4. TOP 10 series con más personas involucradas (en total) a lo largo de sus episodios

SELECT 
    b.primaryTitle AS serie,                  -- Selecciona el título principal de la serie y lo renombra como "serie"
    COUNT(DISTINCT p.nconst) AS total_personas_involucradas  
        -- Cuenta de forma única (DISTINCT) el número de personas involucradas (identificadas por nconst) en los episodios
FROM title_episode e                           -- Se parte de la tabla "title_episode" (alias "e"), que relaciona episodios con series
JOIN title_basics b 
    ON e.parentTconst = b.tconst                -- Une "title_episode" con "title_basics" (alias "b") mediante parentTconst para obtener el título de la serie
JOIN title_principals p 
    ON e.tconst = p.tconst                      -- Une "title_episode" con "title_principals" (alias "p") para obtener los registros de personas involucradas en cada episodio
JOIN name_basics np 
    ON p.nconst = np.nconst                     -- Une "title_principals" con "name_basics" (alias "np") para asegurar que cada persona involucrada tenga información completa (por ejemplo, nombre real)
GROUP BY b.primaryTitle                        -- Agrupa los resultados por el título de la serie para contar el número de personas por cada serie
ORDER BY total_personas_involucradas DESC      -- Ordena las series de mayor a menor según la cantidad de personas involucradas
LIMIT 10;                                      -- Limita la salida a las 10 series con mayor participación

Razonamiento:

FROM y JOINs: Se unen las tablas para relacionar episodios (title_episode) con series (title_basics) y con las personas involucradas en dichos episodios (title_principals y name_basics).
COUNT(DISTINCT p.nconst): Se cuenta cada persona única involucrada en los episodios de la serie.
GROUP BY y ORDER BY: Se agrupan los datos por serie y se ordenan de mayor a menor según el número de personas involucradas.
LIMIT 10: Se muestran las 10 series principales.


5. TOP 10 Series con más episodios sin director conocido

SELECT 
    b.primaryTitle AS serie,  -- Selecciona el título principal de la serie de la tabla "title_basics" y lo renombra como "serie".
    COUNT(*) AS num_episodios_sin_director  -- Cuenta todos los registros (episodios) para cada serie. En este contexto, cada registro corresponde a un episodio sin director.
    FROM title_episode e  -- Parte de la tabla "title_episode" (alias "e"), que contiene los episodios y la relación con su serie (a través de "parentTconst").
  JOIN title_basics b ON e.parentTconst = b.tconst  -- Une "title_episode" con "title_basics" (alias "b") usando "parentTconst" para relacionar cada episodio con su serie.
  LEFT JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director'  -- Realiza una unión externa (LEFT JOIN) con "title_principals" (alias "p") para traer los datos del director.
    -- Se filtra por "p.category = 'director'" para que solo se consideren registros con ese rol.
    -- El LEFT JOIN asegura que se incluyan todos los episodios, incluso aquellos sin un registro de director.
    WHERE p.nconst IS NULL  -- Filtra los resultados para quedarse solo con aquellos episodios donde no se encontró un director (es decir, "p.nconst" es NULL).
    GROUP BY b.primaryTitle  -- Agrupa los resultados por el título principal de la serie para contar, por cada serie, el número de episodios sin director.
    ORDER BY num_episodios_sin_director DESC  -- Ordena las series de mayor a menor según la cantidad de episodios sin director.
    LIMIT 10;  -- Limita la salida a las 10 series con mayor número de episodios sin director.

Razonamiento:

title_episode y title_basics permiten identificar la relación episodio-serie.
Se hace un LEFT JOIN con title_principals (filtrado por director) para identificar episodios sin registro de director.
La condición WHERE p.nconst IS NULL filtra aquellos episodios en que no se encontró un director.
Aunque aquí se utilizan tres datasets, podrías agregar un join adicional con name_basics si quisieras mostrar algún detalle extra en otro contexto; de igual forma cumple el mínimo requerido.

6. TOP 10 Series con más episodios dirigidos por diferentes directores

SELECT 
    b.primaryTitle AS serie, -- Selecciona el título principal de la serie desde "title_basics" y lo renombra como "serie".
COUNT(DISTINCT np.nconst) AS num_directores, -- Cuenta de forma única (DISTINCT) la cantidad de directores involucrados en los episodios de la serie, usando el identificador "nconst" de "name_basics".
COUNT(e.tconst) AS num_episodios  -- Cuenta el total de episodios para la serie, usando el identificador del episodio (tconst) de "title_episode".
FROM title_episode e  -- Se parte de la tabla "title_episode" (alias "e"), que relaciona cada episodio con su serie a través de "parentTconst".
JOIN title_basics b ON e.parentTconst = b.tconst  -- Une "title_episode" con "title_basics" (alias "b") para obtener la información de la serie (por ejemplo, el título) mediante el campo "parentTconst".
JOIN title_principals p ON e.tconst = p.tconst AND p.category = 'director' -- Une "title_episode" con "title_principals" (alias "p") para extraer los registros en que el rol es 'director'.
-- Se utiliza la condición "p.category = 'director'" para filtrar únicamente los registros correspondientes al director.
    JOIN name_basics np ON p.nconst = np.nconst -- Une "title_principals" con "name_basics" (alias "np") para obtener los detalles del director (por ejemplo, su nombre), usando "nconst".
GROUP BY b.primaryTitle  -- Agrupa los resultados por el título de la serie, permitiendo contar el número de directores y episodios por cada serie.
    ORDER BY num_directores DESC  -- Ordena las series de mayor a menor según la cantidad de directores diferentes involucrados.
    LIMIT 10;  -- Limita la salida a las 10 series con mayor cantidad de directores diferentes.

Razonamiento:

title_episode y title_basics se usan para obtener la serie a la que pertenece cada episodio.
title_principals filtra aquellos registros de episodios en los que hay director.
name_basics permite contar de forma única (con DISTINCT) a cada director involucrado en la serie.
Esta consulta integra cuatro fuentes y ayuda a identificar qué series cuentan con la mayor diversidad de directores.