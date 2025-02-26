# Guía para la Importación, Optimización de Datasets en PostgreSQL con pgAdmin4 y creación de sentencias SQL

**Docente:** Carlos García Calatraba\
**Grupo:** Los cinco

## Alumnos

- **Steven Louis Allus**
- **Carlos Jaime Iglesias Vicente**
- **Michel Clemente Pretel Sacerio**
- **Adrián Rodríguez Fernández**
- **Antonio López García**

**Asignatura:** Base de datos I\
**Curso:** Universitat Carlemany, Data Science

---

# Índice

1. **Introducción**
2. **Exploración de datos**
3. **Sentencias SQL**
4. **Creación e importación de datos a PostgreSQL pgAdmin**
5. **Código de sentencias SQL**

---

## 1. Introducción

En este ejercicio trabajaremos con 7 datasets bajados de la plataforma IMDb Developer: [IMDb Developer](https://developer.imdb.com/).

El objetivo es crear 6 consultas SQL en las que cada una relacione dos o más tablas.

### Datasets utilizados:

- `title.ratings.tsv`
- `title.episode.tsv`
- `title.crew.tsv`
- `title.basics.tsv`
- `name.basics.tsv`
- `title.akas.tsv`
- `title.principals.tsv`

---

## 2. Exploración de datos

Visualizaremos los diez elementos de cada dataset para saber con qué datos trabajamos y decidir qué consultas SQL realizar.
La visualización de datos la realizaremos con comandos de consola cuando los datasets tienen un volumen de más de 1 GB.

### Lectura de archivos grandes desde la consola

#### **Linux**

```sh
head -n 10 title.principals.tsv
zcat title.principals.tsv.gz | head -n 10
awk 'NR<=10' title.principals.tsv
```

#### **Windows (WSL)**

```sh
/mnt/d/datos/title.principals.tsv
head -n 10 /mnt/d/datos/title.principals.tsv
zcat /mnt/d/datos/title.principals.tsv.gz | head -n 10
awk 'NR<=10' /mnt/d/datos/title.principals.tsv
```

#### **MacOS**

```sh
head -n 10 title.principals.tsv
zcat title.principals.tsv.gz | head -n 10
awk 'NR<=10' title.principals.tsv
```

### Ejemplo de datos

#### **title.ratings.tsv**

```
tconst	averageRating	numVotes
tt0000001	5.7	1930
tt0000002	5.8	261
tt0000003	6.5	1745
tt0000004	5.6	176
tt0000005	6.2	2560
tt0000006	5.1	176
tt0000007	5.4	798
tt0000008	5.4	2076
tt0000009	5.3	201
```

---

## 3. Sentencias SQL

Después de visualizar las diez primeras líneas de los datasets, consideramos hacer estas consultas SQL y quedarnos solo con 4 datasets.

### Consultas SQL:

- **TOP 10 Series con más directores diferentes**
- **TOP 10 Guionistas que repiten serie**
- **TOP 10 Series con más episodios dirigidos por el mismo director**
- **TOP 10 Episodios dirigidos y escritos por la misma persona**
- **TOP 10 Series con más episodios sin director conocido**
- **TOP 10 Series con más episodios dirigidos por diferentes directores**

### Datasets a utilizar:

- `title_episode`: Para identificar la relación episodio-serie.
- `title_basics`: Aporta el nombre de la serie.
- `title_principals`: Filtra aquellos registros donde el rol es de guionista (puedes considerar tanto 'writer' como 'screenplay').
- `name_basics`: Traduce el identificador del guionista a su nombre.

---

## 4. Creación e importación de datos a PostgreSQL pgAdmin

La importación de datos nos da problemas en las tablas `title.basics.tsv`, `title.principals.tsv` y `name.basics.tsv`.

### Solución de errores en importación

Se identificó que el problema radicaba en las comillas simples y dobles en los datasets. Se eliminaron con los siguientes comandos:

```sh
sed -i.bak "s/'//g" title.basics.tsv
sed -i.bak "s/\"//g" title.basics.tsv
```

También se encontraron errores de longitud en las columnas `primarytitle` y `originaltitle`, solucionados con:

```sql
ALTER TABLE title_basics
ALTER COLUMN primarytitle TYPE VARCHAR(1024);
ALTER TABLE title_basics
ALTER COLUMN originaltitle TYPE VARCHAR(1024);
```

Para `name_basics.tsv`, el problema era un exceso de longitud en `primaryname`:

```sql
ALTER TABLE name_basics
ALTER COLUMN primaryname TYPE VARCHAR(2048);
```

Tras la importación, se ejecutó `ANALYZE` para optimizar consultas:

```sql
ANALYZE title_episode;
ANALYZE title_basics;
ANALYZE title_principals;
ANALYZE name_basics;
```

---

## Creación de índices

```sql
-- Índice en title_episode.parentTconst para acelerar el JOIN con title_basics
CREATE INDEX idx_title_episode_parentTconst ON title_episode(parentTconst);

-- Índice compuesto en title_principals para acelerar el filtrado por categoría y el JOIN por tconst
CREATE INDEX idx_title_principals_tconst_category ON title_principals(tconst, category);

-- (Opcional) Índice en title_principals.nconst para optimizar los JOIN con name_basics
CREATE INDEX idx_title_principals_nconst ON title_principals(nconst);
```

### ¿Por qué crearlos?

#### Mejora del rendimiento en JOINs y filtros:
Cuando una consulta une tablas o filtra por una columna específica, sin un índice el motor de la base de datos debe realizar un escaneo completo de la tabla. Con los índices, el motor accede directamente a los registros relevantes, reduciendo el tiempo de respuesta.

#### Índice en title_episode.parentTconst:
Este índice es útil porque muchas de tus consultas unen la tabla `title_episode` con `title_basics` mediante `parentTconst = tconst`. Al indexar `parentTconst`, el motor puede encontrar rápidamente las series asociadas a cada episodio.

#### Índice compuesto en title_principals (tconst, category):
En tus consultas filtras por el rol (por ejemplo, `category = 'director'` o `category = 'writer'`) y al mismo tiempo se une por `tconst`. Un índice compuesto en ambas columnas acelera estas operaciones al reducir el conjunto de datos de forma más eficiente.

#### Índice en title_principals.nconst:
Este índice resulta útil para los JOIN que relacionan `title_principals` con `name_basics` mediante `nconst`. Esto mejora la velocidad al obtener información adicional del profesional (como el nombre real).

Con estos índices, tus consultas que involucren relaciones y filtros sobre estas columnas funcionarán de manera más eficiente, mejorando el rendimiento general de la base de datos.


## 5. Código de sentencias SQL

Este apartado presenta varias consultas SQL que analizan datos de series de televisión, utilizando un conjunto de tablas interrelacionadas.  Cada consulta se acompaña de una explicación detallada de su lógica y de las tablas que utiliza.

---

### 1. TOP 10 Series con más directores diferentes

**Consulta:**

```sql
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
```

**Razonamiento:**
```sql
FROM y JOINs: Unen las tablas title_episode, title_basics, title_principals y name_basics para relacionar episodios con series y con los directores de cada episodio.
COUNT(DISTINCT np.nconst): Cuenta el número de directores únicos para cada serie.
GROUP BY y ORDER BY: Agrupan los resultados por serie y los ordenan de mayor a menor según el número de directores.
LIMIT 10: Muestra las 10 series principales.
```
### 2. TOP 10 Guionistas que repiten serie
**Consulta:**
```sql
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
Use code with caution.
SQL
```
**Razonamiento:**
```sql
FROM y JOINs: Unen las tablas title_episode, title_basics, title_principals y name_basics para relacionar episodios con series y con los guionistas de cada episodio.
COUNT(*): Cuenta el número de episodios en los que participa cada guionista en cada serie.
GROUP BY y ORDER BY: Agrupan los resultados por serie y guionista, y los ordenan de mayor a menor según el número de episodios.
LIMIT 10: Muestra los 10 principales resultados.
```
### 3. TOP 10 Series con más episodios dirigidos por el mismo director

**Consulta:**
```sql
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
Use code with caution.
SQL
```
**Razonamiento:**
```sql
FROM y JOINs: Unen las tablas para relacionar episodios (title_episode) con series (title_basics) y con el director de cada episodio (title_principals y name_basics).
COUNT(*): Cuenta el número de episodios dirigidos por el mismo director en cada serie.
GROUP BY y ORDER BY: Agrupan los datos por serie y director, y los ordenan de mayor a menor según el número de episodios.
LIMIT 10: Muestra las 10 series principales.
```
### 4. TOP 10 series con más personas involucradas (en total) a lo largo de sus episodios
**Consulta:**
```sql
SELECT 
    b.primaryTitle AS serie,
    COUNT(DISTINCT p.nconst) AS total_personas_involucradas
FROM title_episode e
JOIN title_basics b ON e.parentTconst = b.tconst
JOIN title_principals p ON e.tconst = p.tconst
JOIN name_basics np ON p.nconst = np.nconst
GROUP BY b.primaryTitle
ORDER BY total_personas_involucradas DESC
LIMIT 10;
```
**Razonamiento:**
```sql
FROM y JOINs: Unen las tablas para relacionar episodios (title_episode) con series (title_basics) y con las personas involucradas en dichos episodios (title_principals y name_basics).
COUNT(DISTINCT p.nconst): Cuenta cada persona única involucrada en los episodios de la serie.
GROUP BY y ORDER BY: Agrupan los datos por serie y los ordenan de mayor a menor según el número de personas involucradas.
LIMIT 10: Muestra las 10 series principales.
```
### 5. TOP 10 Series con más episodios sin director conocido
**Consulta:**
```sql
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
```
**Razonamiento:**
```sql
FROM y JOINs: Unen las tablas title_episode y title_basics y realizan un LEFT JOIN con title_principals para incluir todos los episodios, incluso aquellos sin director.
WHERE p.nconst IS NULL: Filtra los resultados para mostrar solo los episodios sin director conocido.
COUNT(*): Cuenta el número de episodios sin director para cada serie.
GROUP BY y ORDER BY: Agrupan los resultados por serie y los ordenan de mayor a menor según el número de episodios sin director.
LIMIT 10: Muestra las 10 series principales.
```
### 6. TOP 10 Series con más episodios dirigidos por diferentes directores
**Consulta:**
```sql
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
```
**Razonamiento:**
```sql
FROM y JOINs: Unen las tablas para relacionar los episodios (title_episode) con su serie (title_basics), y con el director de ese episodio (title_principals y name_basics).
COUNT(DISTINCT np.nconst): Cuenta la cantidad de directores distintos para cada serie.
COUNT(e.tconst): Se cuenta el número de episodios de cada serie.
GROUP BY y ORDER BY: Agrupa por serie y ordena por la cantidad de directores de forma descendente.
LIMIT 10: Muestra solo las 10 primeras series.
```