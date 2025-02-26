# Guía para la Importación, Optimización de Datasets en PostgreSQL con pgAdmin4 y creación de sentencias SQL

**Docente:** Carlos García Calatraba  
**Grupo:** Los cinco  

## Alumnos

- **Steven Louis Allus**
- **Carlos Jaime Iglesias Vicente**
- **Michel Clemente Pretel Sacerio**
- **Adrián Rodríguez Fernández**
- **Antonio López García**

**Asignatura:** Base de datos I  
**Curso:** Universitat Carlemany, Data Science  

---

# Índice

1. **Introducción**
2. **Exploración de datos**
3. **Sentencias SQL**
4. **Creación e importación de datos a PostgreSQL pgAdmin**
5. **Visualización y optimización de Datos**
6. **Código de sentencias SQL**

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

Para solucionar esto identificamos que el problema son las comillas (`'`) y las comillas dobles (`"`) en los datasets.
Las eliminamos desde la consola para no tener que abrir archivos grandes manualmente con un editor de texto.

### Eliminación de comillas dobles y simples

#### Desde WSL:

```sh
sed -i.bak "s/'//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/title.basics.tsv
sed -i.bak "s/\"//g" /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/title.basics.tsv
```

Estos comandos eliminan todas las comillas simples y dobles en los archivos para evitar errores en la importación de datos. Se crea una copia de seguridad con extensión `.bak` antes de realizar los cambios.

### Importación de datos

Al intentar importar los datos del archivo `title.basics.tsv` usando el comando `COPY`:

```sql
COPY title_basics
FROM 'D:\usuaris\a.lopez.g\trabajos\dataScienceCarlemany\base_datos_01\week_03\title.basics.tsv'
DELIMITER E'\t'
CSV HEADER
NULL '\N';
```

Se produce el siguiente error:

```
ERROR:  value too long for type character varying(255)
CONTEXT:  COPY title_basics, line 846955, column primarytitle: "..."
SQL state: 22001
```

Y un error similar para la columna `originaltitle`.

### Causa:

El error indica que los valores en las columnas `primarytitle` y `originaltitle` del archivo TSV exceden la longitud máxima definida en la tabla `title_basics` (que es `VARCHAR(255)` por defecto). Algunos títulos son más largos de 255 caracteres.

### Solución:

Para solucionar este problema, se aumenta el tamaño de las columnas `primarytitle` y `originaltitle` en la tabla `title_basics`. Se utiliza el comando `ALTER TABLE` para modificar el tipo de dato a `VARCHAR(1024)` (o `TEXT` si se desea una longitud ilimitada).

```sql
ALTER TABLE title_basics
ALTER COLUMN primarytitle TYPE VARCHAR(1024);  -- O TEXT

ALTER TABLE title_basics
ALTER COLUMN originaltitle TYPE VARCHAR(1024);  -- O TEXT
```


Error en name.basics.tsv 
### Parece que es mas grande que 10024.
```sql
ALTER TABLE name_basics
ALTER COLUMN primaryname TYPE VARCHAR(2048);  -- O TEXT
### Optimización de datos con ANALYZE
```


Revisamos cada línea del archivo, asegurándose de que tenga exactamente 6 columnas separadas por tabuladores. Si una línea no cumple con este formato, imprime un mensaje de error (indicando el número de línea y su contenido) en el archivo errores.txt. Se utilizó awk porque el error value too long... persistía incluso después de aumentar el tamaño de las columnas en la base de datos, lo que sugería un problema de formato en el archivo de origen (probablemente tabulaciones faltantes o adicionales).

```
awk -F '\t' 'NF != 6 { print "Error en la línea " NR ": " $0 }' /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/name.basics.tsv > /mnt/d/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/base_datos_01/week_03/errores.txt
El fichero errores.txt indica que hay errores, vamos a ver la linea manualmente.
```

Después de la importación, utilizamos `ANALYZE` para mejorar el rendimiento de las consultas en nuestra base de datos. Este comando permite al sistema recopilar estadísticas sobre el contenido de las tablas, ayudando a optimizar la ejecución de consultas.

```sql
ANALYZE title_episode;
ANALYZE title_basics;
ANALYZE title_principals;
ANALYZE name_basics;
```

Usar `ANALYZE` permite mantener y mejorar el rendimiento de las consultas en tu base de datos, ya que proporciona al sistema la información necesaria para tomar decisiones de ejecución óptimas.

