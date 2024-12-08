# Análisis de Componentes Principales

## Asignatura
**Análisis Multivariante**

**Profesor:** Laura Durán

**Alumnos:** Steven Allus, Antonio López

---

## Índice

1. [Descripción de la actividad](#descripcion)
2. [Definición Componentes Principales](#definicion)
3. [Ejemplo representación tres variables](#ejemplo)
4. [Código R](#codigo-r)
   - [Instalación librerías, carga de datos y muestra de datos](#instalacion)
   - [Escalado variables, reducción de dimensiones](#escalado)
   - [Eigenvalues](#eigenvalues)
   - [Componentes principales Dim1 y Dim2](#componentes)
   - [Varianza de cada dimensión](#varianza)
   - [Varianza acumulada en cada dimensión](#varianza-acumulada)
   - [BIPLOT simultáneo variables e individuos](#biplot)
5. [Conclusiones](#conclusiones)

---

## 1. Descripción de la actividad {#descripcion}

En esta actividad, exploraremos el Análisis de Componentes Principales (PCA) aplicando técnicas estadísticas en R.

El objetivo es identificar patrones comunes entre 10 tumores analizando la expresión de 12 genes. Los datos provienen del archivo `genes_tumores.csv`. Se espera entregar un informe con el código R, explicaciones y conclusiones, utilizando RMarkdown.

---

## 2. Definición Componentes Principales {#definicion}

Los Componentes Principales son combinaciones lineales de las variables originales que maximizan la varianza explicada. Estos permiten representar visualmente datos reduciendo dimensiones con la menor pérdida de información posible.

---

## 3. Ejemplo representación tres variables {#ejemplo}

Se representa un eje de coordenadas utilizando subconjuntos de tres genes. Esto permite una visualización tridimensional que facilita observar similitudes y diferencias entre tumores.

---

## 4. Código R {#codigo-r}

### 4.1 Instalación librerías, carga de datos y muestra de datos {#instalacion}

```r
# Seleccionar directorio de trabajo:
setwd("D:/usuaris/a.lopez.g/trabajos/dataScienceCarlemany/analisis_multivariante/semana_03")

# Instalar y cargar paquetes:
if (!require(logisticPCA)) install.packages("logisticPCA")
if (!require(FactoMineR)) install.packages("FactoMineR")
if (!require(factoextra)) install.packages("factoextra")

library(logisticPCA)
library(FactoMineR)
library(factoextra)

# Importar datos:
genes_tumores <- data.frame(read.csv("genes_tumores.csv"))
genes_tumores <- genes_tumores[, -1] # Excluir la primera columna
head(genes_tumores)
```

---

### 4.2 Escalado variables, reducción de dimensiones {#escalado}

```r
# PCA -> datos escalados con gráfico:
pca_genes <- PCA(genes_tumores, scale.unit = TRUE, graph = TRUE)
```

El escalado asegura que las variables tengan igual peso, evitando sesgos por magnitud o unidades.

---

### 4.3 Eigenvalues {#eigenvalues}

```r
# Resumen de PCA para observar eigenvalues:
summary(pca_genes)
```

Los eigenvalues miden la varianza explicada por cada componente.

---

### 4.4 Componentes principales Dim1 y Dim2 {#componentes}

```r
plot(
  pca_genes$ind$coord[, 1], # Coordenadas en Dim1
  pca_genes$ind$coord[, 2], # Coordenadas en Dim2
  xlab = paste0("Dim 1 (", round(pca_genes$eig[1, 2], 2), "% varianza)"),
  ylab = paste0("Dim 2 (", round(pca_genes$eig[2, 2], 2), "% varianza)"),
  main = "Proyección en Dim1 y Dim2",
  pch = 19, col = "blue"
)
```

---

### 4.5 Varianza de cada dimensión {#varianza}

```r
# Varianza explicada por cada dimensión:
fviz_eig(pca_genes, addlabels = TRUE, ylim = c(0, 100))
```

---

### 4.6 Varianza acumulada en cada dimensión {#varianza-acumulada}

```r
# Representación de la varianza acumulada:
# (Código pendiente)
```

---

### 4.7 BIPLOT simultáneo variables e individuos {#biplot}

```r
# Biplot variables e individuos:
fviz_pca_biplot(
  pca_genes,
  repel = TRUE,
  col.var = "blue",
  col.ind = "black",
  title = "Biplot: Variables e Individuos"
)
```

---

## 5. Conclusiones {#conclusiones}

1. **Interpretación de genes en las componentes principales:**
   - **Dim1 (PC1):** Genes como gene10 (-0.963) y gene5 (0.949) destacan.
   - **Dim2 (PC2):** Genes como gene1 (0.808) y gene3 (0.787) son relevantes.

2. **Análisis de tumores en el biplot:**
   - Tumores agrupados: tumorG, tumorH y tumorI.
   - Tumores atípicos: tumorD y tumorE.

---

**Análisis de Componentes Principales - Trabajo de Análisis Multivariante.**

