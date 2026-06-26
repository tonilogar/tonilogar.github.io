# Propuesta del Trabajo Final de Bàtxelor (TFB)

**A continuación, indica aquella información necesaria para que el docente de la UdA y tu tutor/a puedan tener una primera idea de tu proyecto y podáis asentar las primeras bases para avanzar en tu TFB. Recuerda que es un primer borrador y que tu tutor/a te acompañará para definir con mayor concreción estas primeras ideas.** 
**Es recomendable enviar a tu tutor/a este documento antes de tu primer contacto o tutoría.**

## 1. Título propuesto 

**En general, el título debe ser concreto y debe permitir al lector saber de qué va a tratar tu TFB. En esta primera propuesta, trata de proponer un título acotando la temática y permitiendo al lector conocer la finalidad de este TFB. No debe ser excesivamente extenso.**

Plataforma Geoespacial Escalable para la Monitorización y Procesamiento de Datos Satelitales (Copernicus Sentinel-2): Predicción de la Recuperación de Masas Forestales Post-Incendio.

## 2. Objetivos del TFB

**¿Qué objetivo general tiene el TFB? ¿Se pueden definir objetivos específicos que con su cumplimiento permitan conseguir el objetivo general?**

**2.1. Objetivo general:** 
**Definir el propósito principal del Trabajo Final de Título, indicando qué se pretende lograr con su realización.**

Validar la viabilidad de un entorno escalable (pipeline geoespacial) para imágenes Sentinel-2, diseñado arquitectónicamente para integrar y ejecutar modelos de Machine Learning / Deep Learning. Como demostrador práctico (Proof of Concept), se implementará un modelo avanzado para la cuantificación, monitorización y predicción de la dinámica de recuperación de la masa forestal tras Eventos de Incendios Forestales Extremos (EWE).

**2.2. Objetivos específicos:** 
**Establecer los objetivos concretos que, de manera progresiva, permitan alcanzar el objetivo general. Estos deben ser claros, medibles y coherentes con la temática del TFT.**

* 2.2.1. Construir la infraestructura tecnológica completa (repositorio, servidor online, prácticas DevOps, frontend, backend y bases de datos), integrando la API de Copernicus para la visualización *on the fly* en una plataforma Web interactiva.
* 2.2.2. Identificar, seleccionar y extraer las fuentes de datos satelitales (Copernicus Sentinel-2, Copernicus DEM) y de *Ground Truth* (perímetros de grandes incendios), diseñando y desarrollando procesos ETL (Extract, Transform, Load) para su armonización y preparación.
* 2.2.3. Diseñar una arquitectura de base de datos orientada a la nube basada en Cloud Optimized GeoTIFF (COG) y PMTiles.
* 2.2.4. Desarrollar, entrenar y validar un modelo de Deep Learning para series temporales espaciales, capaz de evaluar la severidad inicial, mapear la resiliencia y proyectar la recuperación natural del manto vegetal.

## 3. Breve justificación de la propuesta

**¿Qué necesidades cubre tu TFB, qué problema resuelve, a qué le estás dando solución?**
**¿Cómo contribuye a la comunidad, qué valor aporta?**
**Puedes incluir datos de la problemática detectada, situaciones que conoces, en qué contexto aporta valor tu proyecto, etc.**
**Incluye entre 2 y 4 códigos UNESCO de la guía docente.**
**Asimismo, se podrá hacer referencia experiencias previas o situaciones observadas que fundamenten la pertinencia del estudio, así como a los Objetivos de Desarrollo Sostenible (ODS) con los que el trabajo se relaciona.**

* **Problema que resuelve:** Los Eventos de Incendios Forestales Extremos (EWE) suponen un grave riesgo de colapso ecológico y socioeconómico. Tras su extinción, es vital conocer la capacidad de resiliencia del ecosistema para discriminar zonas que se recuperarán naturalmente frente a aquellas en riesgo de degradación crónica (ej. erosión del suelo). Este TFB desarrolla una herramienta basada en Inteligencia Artificial y Observación de la Tierra para analizar y predecir esta sucesión ecológica.
* **Valor aportado y Alineación Estratégica:** Este trabajo se alinea intrínsecamente con los objetivos del proyecto europeo Horizonte 2020 **FIRE-RES**, que promueve la innovación tecnológica para crear territorios resilientes al fuego. La herramienta actuará como un *Decision Support System (DSS)*, proporcionando predicciones que informen a los equipos gestores sobre dónde es urgente aplicar silvicultura preventiva o repoblaciones. Además, su metodología tiene potencial directo para ser integrada de forma práctica en los *Living Labs* impulsados por FIRE-RES en toda Europa.
* **Códigos UNESCO:** 1203 (Ciencia de los Ordenadores), 2505 (Geografía), 2417 (Biología Vegetal / Ecología Forestal).
* **ODS:** ODS 13 (Acción por el clima) y ODS 15 (Vida de ecosistemas terrestres).

## 4. Propuesta de índice de TFB

**Desarrolla un primer borrador de índice adecuando la propuesta, teniendo en cuenta el índice incluido en el plan docente.**

1. Introducción, contextualización y objetivos (Alineación Estratégica FIRE-RES)
2. Fundamentación teórica (Observación de la Tierra y Deep Learning)
3. Metodología aplicada y justificación (Pipeline Geoespacial, ETL y Entrenamiento del Modelo)
4. Resultados (Mapeo de Resiliencia y Proyección Vegetal)
5. Análisis, interpretación y discusión
6. Conclusiones y aportaciones (Integración en Living Labs)
7. Referencias bibliográficas y citas

## 5. Alcance previo

**Incluye el alcance del proyecto, tanto el positivo (qué se va a realizar) como el negativo (qué no se va a realizar, pero podría malinterpretarse como que sí, al ser “frontera”).**

* **Alcance positivo (Qué se hará):** Desarrollo web interactivo, Extracción de series temporales Copernicus Sentinel-2 y modelo de elevación DEM, Modelo de Deep Learning aplicado a polígonos de grandes incendios históricos (ej. Cataluña desde 2015) y visualización web con COG/PMTiles.
* **Alcance negativo (Qué NO se hará):** No se desarrollarán modelos predictivos para otro tipo de catástrofes (inundaciones, terremotos) ni se utilizarán imágenes de radar (Sentinel-1). Tampoco se entrará a analizar biomasa o química del suelo mediante sensores físicos *in situ*.

## 6. Competencias que desarrollar

**Incluye un listado de todas las competencias específicas, y el nivel de detalle esperado para cada una de ellas (1-5). Recuerda que debes desarrollar todas las competencias. Algunas más que otras, pero todas deben tener un mínimo.**
**Recuerda que esto debe ser diverso. Es impensable un nivel 4-5 en todas ellas.**

| CE | DEFINICIÓN | NIVEL ESPERADO |
|----|------------|----------------|
| CE2 | Estructurar la información en base a conocimientos y de principios de la ciencia de datos para un uso posterior. | 4 |
| CE3 | Diseñar y gestionar sistemas de información para el almacenamiento y el tratamiento de datos. | 5 |
| CE4 | Escoger y utilizar técnicas de aprendizaje automático y construir sistemas que empleen para la toma de decisiones. | 4 |
| CE5 | Escoger y utilizar técnicas de modelización estadística y análisis de datos para la toma de decisiones. | 3 |
| CE8 | Gestionar de forma integral proyectos relacionados con la información, utilizando técnicas vinculadas a la ciencia de datos. | 4 |
| CE10| Desarrollar las tareas profesionales de gestión y de explotación de datos respetando la legislación, la normativa y las especificaciones vigentes. | 2 |
| CE11| Visualizar la información a fin de facilitar la exploración y el análisis de datos para que el usuario final pueda tomar decisiones. | 5 |

## 7. Listado de datos necesarios

**Todo proyecto de Ciencia e Ingeniería de datos parte de un mismo origen: Los datos.**
**Sin ellos, no somos capaces de obtener resultados, a pesar de contar con capacidad técnica o infraestructura.**
**¿Tienes los datos? ¿Cuáles son y en qué formato? ¿Son públicos? ¿Son de la empresa en la que trabajas? ¿Cómo esperas obtenerlos? ¿Hay algún condicionante técnico o legal?**

| ID | DEFINICIÓN / COMENTARIO | Público | Disponible |
|----|-------------------------|---------|------------|
| 1  | Imágenes multiespectrales Sentinel-2 (Copernicus API) para la extracción de índices espectrales (NDVI, NBR) a través de series temporales. | Sí | Sí |
| 2  | Copernicus DEM (Modelo de Elevación Digital) para incluir la topografía (altitud, pendiente, orientación) como co-variable predictora crítica. | Sí | Sí |
| 3  | Perímetros históricos de grandes incendios (ej: Cataluña desde 2015) para acotar las zonas de estudio y servir de *Ground Truth* del ciclo temporal completo. | Sí | Sí |

**Las solicitudes de TFB deberán tener, como mínimo, un origen de dato público y disponible. Si estas contienen datos privados y/o no disponibles (por el momento), será considerado un riesgo. Deberás detallar esto, junto con otros posibles, en la siguiente sección.**

## 8. Análisis de riesgos

**Haz una lista de posibles riesgos que pueden impactar negativamente el desarrollo de tu proyecto y, para cada uno, una posible manera de solucionarlo, o una alternativa que lo evite.**

* **Riesgo 1:** Limitación de cuotas de la API de Copernicus en la extracción de series temporales extensas.
  * *Mitigación:* Trabajar prioritariamente con imágenes Cloud Optimized GeoTIFF (COG) procesadas *on the fly* o, en su defecto, utilizar formatos estáticos orientados a la nube (PMTiles) o desplegar un servidor de teselas ráster (MBTiles).
* **Riesgo 2:** Interferencias atmosféricas (nubosidad) en las imágenes satelitales que generen ruido estocástico en la fenología anual.
  * *Mitigación:* Aplicar filtros de nubosidad estrictos integrados en el preprocesamiento ETL y utilizar la agregación mensual para suavizar anomalías. En casos extremos de ausencia prolongada de datos útiles de Sentinel-2, se utilizarán imágenes del programa Landsat como fuente de datos complementaria.

## 9. Planificación y cronograma de trabajo

**Propón una planificación para el desarrollo del TFB. Para ello, puedes definir un cronograma en el que se incluyan las acciones necesarias y las fechas límites para el cumplimiento de dichas acciones. Compartir y consensuar esta información con tu tutor/a os permitirá coordinaros y trabajar de manera más cómoda y óptima.**


### Fase 1: Planificación, Diseño Arquitectónico y Fundamentación Teórica
**Fechas:** 15 de Junio – 10 de Julio
* **Hito Académico:** **Entrega 1: Propuesta Inicial (22/06 - 28/06)** y validación con la tutora (2ª Tutoría).
* **Tareas Técnicas:**
  * Revisión exhaustiva de la literatura (Fundamentación Teórica) enfocada en Observación de la Tierra, Deep Learning y el proyecto FIRE-RES.
  * Definición formal de la arquitectura Cloud (Cloud Optimized GeoTIFF y PMTiles).
  * Selección de los perímetros de grandes incendios en Cataluña (Ground Truth).

### Fase 2: Ingeniería de Datos y Desarrollo del ETL
**Fechas:** 11 de Julio – 26 de Julio
* **Hito Académico:** **Entrega 2: Desarrollo del Marco Teórico y Metodología - 60% avance (20/07 - 26/07)**.
* **Tareas Técnicas:**
  * Conexión a la API de Copernicus para la descarga de series temporales (Sentinel-2) y elevación (Copernicus DEM).
  * Programación del pipeline ETL (Extract, Transform, Load).
  * Limpieza de ruido (filtros de nubosidad) y agregación temporal mensual.
  * Armonización espacial de las capas ópticas y topográficas para la creación de los tensores de datos.

### Fase 3: Modelado de Deep Learning (Entrenamiento y Validación)
**Fechas:** 27 de Julio – 15 de Agosto
* **Hito Académico:** Trabajo de campo y validación teórica.
* **Tareas Técnicas:**
  * Diseño de la arquitectura de la red neuronal (convolucional/recurrente) para series temporales espaciales.
  * Entrenamiento del modelo utilizando los índices espectrales y datos topográficos.
  * Evaluación del rendimiento, cálculo de métricas de error y ajuste de hiperparámetros.
  * Generación de las inferencias finales: Mapas de resiliencia y predicción de recuperación vegetal.

### Fase 4: Despliegue de Infraestructura y Frontend Web
**Fechas:** 16 de Agosto – 31 de Agosto
* **Hito Académico:** **Entrega 3: Entrega Completa del TFT - 100% avance (31/08 - 06/09)**.
* **Tareas Técnicas:**
  * Conversión de los resultados matriciales (mapas) a formatos estáticos orientados a la nube (COG/PMTiles).
  * Desarrollo del frontend: plataforma web interactiva con mapas dinámicos.
  * Integración del backend para servir los datos geoespaciales.
  * Redacción de los capítulos de Resultados, Conclusiones y Trabajo Futuro en la memoria oficial.

### Fase 5: Revisión, Pulido y Depósito Final
**Fechas:** 1 de Septiembre – 20 de Septiembre
* **Hito Académico:** **Entrega 4: Depósito Final en 1ª Defensa (14/09 - 20/09)**.
* **Tareas Técnicas:**
  * Incorporación del *feedback* de la tutora tras la Entrega 3.
  * Corrección de formato (Normativa APA) y revisión bibliográfica.
  * Pruebas finales de estrés y usabilidad de la plataforma web.
  * Generación de la versión definitiva (PDF) para el tribunal.

### Fase 6: Preparación de la Defensa
**Fechas:** 21 de Septiembre – 25 de Octubre
* **Hitos Académicos:**
  * **Entrega PPT Defensa:** 05/10 - 11/10
  * **Primera Defensa ante el Tribunal:** 12/10 - 25/10
* **Tareas Técnicas:**
  * Síntesis del proyecto en un PowerPoint visual y de alto impacto.
  * Preparación de una "Live Demo" segura y fluida de la plataforma web para enseñarla en vivo al tribunal.
  * Ensayos de oratoria (ajustando la presentación al tiempo límite de 10-15 minutos).

### Resumen del Cronograma

| Fechas | Hito Académico (Entrega) | Tareas Técnicas / Desarrollo |
|--------|--------------------------|------------------------------|
| **15 Jun - 10 Jul** | **Entrega 1: Propuesta Inicial** (22/06 - 28/06) | Fundamentación teórica, diseño de arquitectura y selección de zonas de estudio. |
| **11 Jul - 26 Jul** | **Entrega 2: Metodología (60%)** (20/07 - 26/07) | Conexión a Sentinel-2 y DEM, programación ETL y armonización de datos. |
| **27 Jul - 15 Ago** | *Trabajo de campo intensivo* | Diseño de red neuronal (Deep Learning), entrenamiento, validación e inferencias. |
| **16 Ago - 31 Ago** | **Entrega 3: Entrega Completa (100%)** (31/08 - 06/09) | Creación de PMTiles/COG, desarrollo plataforma Web interactiva y redacción final. |
| **1 Sep - 20 Sep**  | **Entrega 4: Depósito Final** (14/09 - 20/09) | Correcciones APA, pruebas de estrés de la Web e incorporación de feedback. |
| **21 Sep - 25 Oct** | **Primera Defensa y PPT** (12/10 - 25/10) | Preparación de PowerPoint, ensayos de oratoria y montaje de la *Live Demo*. |
