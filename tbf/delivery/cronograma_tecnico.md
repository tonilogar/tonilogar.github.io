# Cronograma Técnico y de Desarrollo del TFB

El desarrollo del proyecto se ha estructurado siguiendo un enfoque ágil (por *sprints* o fases de ingeniería), enlazando directamente los hitos técnicos de programación e investigación con las ventanas de entrega exigidas por la Universitat Carlemany (Edición 2510).

## Resumen del Cronograma

| Fechas | Hito Académico (Entrega) | Tareas Técnicas / Desarrollo |
|--------|--------------------------|------------------------------|
| **15 Jun - 10 Jul** | **Entrega 1: Propuesta Inicial** (22/06 - 28/06) | Fundamentación teórica, diseño de arquitectura y selección de zonas de estudio. |
| **11 Jul - 26 Jul** | **Entrega 2: Metodología (60%)** (20/07 - 26/07) | Conexión a Sentinel-2 y DEM, programación ETL y armonización de datos. |
| **27 Jul - 15 Ago** | *Trabajo de campo intensivo* | Diseño de red neuronal (Deep Learning), entrenamiento, validación e inferencias. |
| **16 Ago - 31 Ago** | **Entrega 3: Entrega Completa (100%)** (31/08 - 06/09) | Creación de PMTiles/COG, desarrollo plataforma Web interactiva y redacción final. |
| **1 Sep - 20 Sep**  | **Entrega 4: Depósito Final** (14/09 - 20/09) | Correcciones APA, pruebas de estrés de la Web e incorporación de feedback. |
| **21 Sep - 25 Oct** | **Primera Defensa y PPT** (12/10 - 25/10) | Preparación de PowerPoint, ensayos de oratoria y montaje de la *Live Demo*. |

## Fase 1: Planificación, Diseño Arquitectónico y Fundamentación Teórica
**Fechas:** 15 de Junio – 10 de Julio
* **Hito Académico:** **Entrega 1: Propuesta Inicial (22/06 - 28/06)** y validación con la tutora (2ª Tutoría).
* **Tareas Técnicas:**
  * Revisión exhaustiva de la literatura (Fundamentación Teórica) enfocada en Observación de la Tierra, Deep Learning y el proyecto FIRE-RES.
  * Definición formal de la arquitectura Cloud (Cloud Optimized GeoTIFF y PMTiles).
  * Selección de los perímetros de grandes incendios en Cataluña (Ground Truth).

## Fase 2: Ingeniería de Datos y Desarrollo del ETL
**Fechas:** 11 de Julio – 26 de Julio
* **Hito Académico:** **Entrega 2: Desarrollo del Marco Teórico y Metodología - 60% avance (20/07 - 26/07)**.
* **Tareas Técnicas:**
  * Conexión a la API de Copernicus para la descarga de series temporales (Sentinel-2) y elevación (Copernicus DEM).
  * Programación del pipeline ETL (Extract, Transform, Load).
  * Limpieza de ruido (filtros de nubosidad) y agregación temporal mensual.
  * Armonización espacial de las capas ópticas y topográficas para la creación de los tensores de datos.

## Fase 3: Modelado de Deep Learning (Entrenamiento y Validación)
**Fechas:** 27 de Julio – 15 de Agosto
* **Hito Académico:** Trabajo de campo y validación teórica.
* **Tareas Técnicas:**
  * Diseño de la arquitectura de la red neuronal (convolucional/recurrente) para series temporales espaciales.
  * Entrenamiento del modelo utilizando los índices espectrales y datos topográficos.
  * Evaluación del rendimiento, cálculo de métricas de error y ajuste de hiperparámetros.
  * Generación de las inferencias finales: Mapas de resiliencia y predicción de recuperación vegetal.

## Fase 4: Despliegue de Infraestructura y Frontend Web
**Fechas:** 16 de Agosto – 31 de Agosto
* **Hito Académico:** **Entrega 3: Entrega Completa del TFT - 100% avance (31/08 - 06/09)**.
* **Tareas Técnicas:**
  * Conversión de los resultados matriciales (mapas) a formatos estáticos orientados a la nube (COG/PMTiles).
  * Desarrollo del frontend: plataforma web interactiva con mapas dinámicos.
  * Integración del backend para servir los datos geoespaciales.
  * Redacción de los capítulos de Resultados, Conclusiones y Trabajo Futuro en la memoria oficial.

## Fase 5: Revisión, Pulido y Depósito Final
**Fechas:** 1 de Septiembre – 20 de Septiembre
* **Hito Académico:** **Entrega 4: Depósito Final en 1ª Defensa (14/09 - 20/09)**.
* **Tareas Técnicas:**
  * Incorporación del *feedback* de la tutora tras la Entrega 3.
  * Corrección de formato (Normativa APA) y revisión bibliográfica.
  * Pruebas finales de estrés y usabilidad de la plataforma web.
  * Generación de la versión definitiva (PDF) para el tribunal.

## Fase 6: Preparación de la Defensa
**Fechas:** 21 de Septiembre – 25 de Octubre
* **Hitos Académicos:**
  * **Entrega PPT Defensa:** 05/10 - 11/10
  * **Primera Defensa ante el Tribunal:** 12/10 - 25/10
* **Tareas Técnicas:**
  * Síntesis del proyecto en un PowerPoint visual y de alto impacto.
  * Preparación de una "Live Demo" segura y fluida de la plataforma web para enseñarla en vivo al tribunal.
  * Ensayos de oratoria (ajustando la presentación al tiempo límite de 10-15 minutos).

## Resumen del Cronograma

| Fechas | Hito Académico (Entrega) | Tareas Técnicas / Desarrollo |
|--------|--------------------------|------------------------------|
| **15 Jun - 10 Jul** | **Entrega 1: Propuesta Inicial** (22/06 - 28/06) | Fundamentación teórica, diseño de arquitectura y selección de zonas de estudio. |
| **11 Jul - 26 Jul** | **Entrega 2: Metodología (60%)** (20/07 - 26/07) | Conexión a Sentinel-2 y DEM, programación ETL y armonización de datos. |
| **27 Jul - 15 Ago** | *Trabajo de campo intensivo* | Diseño de red neuronal (Deep Learning), entrenamiento, validación e inferencias. |
| **16 Ago - 31 Ago** | **Entrega 3: Entrega Completa (100%)** (31/08 - 06/09) | Creación de PMTiles/COG, desarrollo plataforma Web interactiva y redacción final. |
| **1 Sep - 20 Sep**  | **Entrega 4: Depósito Final** (14/09 - 20/09) | Correcciones APA, pruebas de estrés de la Web e incorporación de feedback. |
| **21 Sep - 25 Oct** | **Primera Defensa y PPT** (12/10 - 25/10) | Preparación de PowerPoint, ensayos de oratoria y montaje de la *Live Demo*. |
