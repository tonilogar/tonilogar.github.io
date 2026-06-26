# Propuesta del Trabajo Final de Bàtxelor (TFB)

**A continuación, indica aquella información necesaria para que el docente de la UdA y tu tutor/a puedan tener una primera idea de tu proyecto y podáis asentar las primeras bases para avanzar en tu TFB. Recuerda que es un primer borrador y que tu tutor/a te acompañará para definir con mayor concreción estas primeras ideas.**
**Es recomendable enviar a tu tutor/a este documento antes de tu primer contacto o tutoría.**

## Índice de Acrónimos y Glosario Técnico

Para facilitar la lectura a evaluadores y personas no especialistas en Sistemas de Información Geográfica (GIS) se definen los siguientes términos clave utilizados en este documento:


* **Sentinel-2:** Misión de satélites ópticos de alta resolución (10 metros) perteneciente al programa europeo Copernicus.
* **Sen2Cor:** Algoritmo oficial de la Agencia Espacial Europea (ESA) utilizado para procesar imágenes satelitales y eliminar efectos atmosféricos (incluye un detector de nubes básico que este proyecto pretende mejorar).
* **Tiling:** Técnica geoespacial que consiste en "trocear" imágenes satelitales gigantes en cuadrados más pequeños para que el ordenador pueda procesarlos sin saturar la memoria RAM.
* **OOM:** *Out of Memory* (Fuera de memoria). Colapso del ordenador por intentar cargar demasiados datos gráficos a la vez.
* **COG:** *Cloud Optimized GeoTIFF*. Formato de imagen satelital optimizado para ser consultado y procesado de forma rápida y directa en la nube.
* **PMTiles:** Formato de archivo de mapa diseñado para almacenar teselas geoespaciales en la nube de forma estática, optimizando la velocidad y coste del servidor.
* **gpkg:** *GeoPackage*. Formato de base de datos geoespacial moderno, abierto y compacto.
* **shp:** *Shapefile*. Formato de archivo informático vectorial clásico y muy extendido para almacenar sistemas de información geográfica.
* **On the fly:** Procesamiento o renderizado "sobre la marcha" o en tiempo real. Ocurre en el instante exacto en que el usuario lo solicita, sin necesidad de tener los datos pre-procesados.
* **ESA:** *European Space Agency* (Agencia Espacial Europea).
* **ACA:** Agencia Catalana del Agua.
* **ICGC:** Instituto Cartográfico y Geológico de Cataluña.


---

## 1. Título propuesto

**En general, el título debe ser concreto y debe permitir al lector saber de qué va a tratar tu TFB. En esta primera propuesta, trata de proponer un título acotando la temática y permitiendo al lector conocer la finalidad de este TFB. No debe ser excesivamente extenso.**

Plataforma Geoespacial Escalable para la Monitorización y Procesamiento de Datos Satelitales (Copernicus Sentinel-2): Detección de nubes mediante modelos de machine learning especializados por estacionalidad (nieve vs. sin nieve) en Cataluña.

## 2. Objetivos del TFB

**Objetivo general:**
**Definir el propósito principal del Trabajo Final de Título, indicando qué se pretende lograr con su realización.**

Desarrollar un entorno escalable (pipeline geoespacial) para imágenes Sentinel-2, diseñado para integrar y ejecutar modelos de machine learning, el cual detectara las nubes en imágenes Sentinel-2 sobre el territorio de Cataluña (órbitas R008 y R051) en diferentes periodos "con nieve o sin nieve".

**Objetivos específicos:**
**Establecer los objetivos concretos que, de manera progresiva, permitan alcanzar el objetivo general. Estos deben ser claros, medibles y coherentes con la temática del TFT.**

* 1. Construir la infraestructura tecnológica completa:
Repositorio, servidor online, prácticas DevOps, frontend, backend y bases de datos, para integrar la API de Copernicus para la visualización on the fly en una plataforma Web interactiva.
* 2. Identificar, seleccionar y extraer las fuentes de datos satelitales (Copernicus Sentinel-2), diseñando y desarrollando procesos ETL (Extract, Transform, Load) para su armonización y preparación.
* 3. Entrenar dos arquitecturas de redes neuronales convolucionales (tipo U-Net) especializadas en cada dominio temporal, con el fin de maximizar la capacidad algorítmica de separar nubes reales de la nieve topográfica.
* 4. Evaluar el rendimiento empírico de ambos modelos frente a los falsos positivos más críticos del procesador estándar Sen2Cor: la nieve de los Pirineos y la superficie del agua profunda (Delta del Ebro y Mar Mediterráneo).
* 5. Diseñar una arquitectura de base de datos orientada a la nube basada en Cloud Optimized GeoTIFF (COG) y PMTiles.



## 3. Breve justificación de la propuesta

**¿Qué necesidades cubre tu TFB, qué problema resuelve, a qué le estás dando solución?**
**¿Cómo contribuye a la comunidad, qué valor aporta?**
**Puedes incluir datos de la problemática detectada, situaciones que conoces, en qué contexto aporta valor tu proyecto, etc.**
**Incluye entre 2 y 4 códigos UNESCO de la guía docente.**
**Asimismo, se podrá hacer referencia experiencias previas o situaciones observadas que fundamenten la pertinencia del estudio, así como a los Objetivos de Desarrollo Sostenible (ODS) con los que el trabajo se relaciona.**

* **Problema que resuelve:** La generación de mosaicos cartográficos limpios a partir de satélites se ve constantemente truncada por las nubes. Los procesadores estándar actuales (como el algoritmo Sen2Cor de la ESA) cometen graves errores ópticos: confunden habitualmente el agua oscura profunda del mar con sombras de nubes, y la nieve de los Pirineos con nubosidad espesa. Este TFB soluciona este problema mediante Inteligencia Artificial adaptativa.
* **Valor aportado y Alineación Estratégica:** Al crear modelos "especialistas" (un modelo experto en escenarios con nieve y otro para escenarios sin nieve) concretamente en Cataluña, se elimina la generalización estadística. El mismo trabajo se puede aplicar a los nuevos satelites catalanes.
* **Códigos UNESCO:** 1203 (Ciencia de los Ordenadores), 2505 (Geografía), 3320 (Tecnología de los Sensores Ópticos).
* **ODS:** ODS 9 (Industria, Innovación e Infraestructura) y ODS 13 (Acción por el clima).

## 4. Propuesta de índice de TFB

**Desarrolla un primer borrador de índice adecuando la propuesta, teniendo en cuenta el índice incluido en el plan docente.**

1. Introducción, contextualización y objetivos.
2. Fundamentación teórica.
3. Metodología aplicada y justificación de resultados. 
4. Análisis, interpretación y discusión.
5. Conclusiones y aportaciones. 
6. Trabajo futuro.
7. Referencias bibliográficas y citas.


## 5. Alcance previo

**Incluye el alcance del proyecto, tanto el positivo (qué se va a realizar) como el negativo (qué no se va a realizar, pero podría malinterpretarse como que sí, al ser “frontera”).**

* **Alcance positivo (Qué se hará):** Desarrollo web interactivo, Extracción de series temporales Copernicus Sentinel-2 (órbitas R008 y R051) sobre Cataluña. Entrenamiento de dos redes neuronales de segmentación semántica (Deep Learning) basadas en estacionalidad. Pruebas de validación en zonas conflictivas (Pirineos y costa).
* **Alcance negativo (Qué NO se hará):** No se desarrollarán modelos para predecir el clima o predecir el movimiento de las nubes en el futuro. Tampoco se utilizarán otras constelaciones de satélites (como Sentinel-1 radar o Landsat) ajenas a Sentinel-2. El objetivo es puramente de segmentación binaria espacial (nube/no-nube).Solo es aplicable a Cataluña.

## 6. Competencias que desarrollar

**Incluye un listado de todas las competencias específicas, y el nivel de detalle esperado para cada una de ellas (1-5). Recuerda que debes desarrollar todas las competencias. Algunas más que otras, pero todas deben tener un mínimo.**
**Recuerda que esto debe ser diverso. Es impensable un nivel 4-5 en todas ellas.**

| Competencia | DEFINICIÓN | NIVEL ESPERADO |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| CT1  | Elaborar la memoria del proyecto, y comunicar de manera clara con un lenguaje específico de ciencia de datos.                                         | 4              |
| CT3  | Realizar una investigación que proponga una solución a una problemática real, evaluando y comunicando los resultados.                                 | 4              |
| CT4  | Plantear un proyecto innovador teniendo en cuenta sus condicionantes técnicos, legales y la gestión segura de los datos.                              | 3              |
| CT5  | Plantear un proyecto innovador reflexionando sobre su impacto en la sociedad, su huella ecológica y el equilibrio sostenible.                         | 2              |
| CE2  | Estructurar la información en base a conocimientos y de principios de la ciencia de datos para un uso posterior.                                      | 4              |
| CE3  | Diseñar y gestionar sistemas de información para el almacenamiento y el tratamiento de datos.                                                         | 4              |
| CE4  | Escoger y utilizar técnicas de aprendizaje automático y construir sistemas que se empleen para la toma de decisiones.                                 | 5              |
| CE5  | Escoger y utilizar técnicas de modelización estadística y análisis de datos para la toma de decisiones.                                               | 4              |
| CE8  | Gestionar de forma integral proyectos y planificar el proceso de trabajo y el tiempo de ejecución requerido.                                          | 4              |
| CE10 | Desarrollar las tareas profesionales de gestión y explotación de datos respetando la legislación, normativa y ética vigente.                          | 2              |
| CE11 | Visualizar la información a fin de facilitar la exploración y el análisis de datos para que el usuario final pueda tomar decisiones.                  | 3              |

## 7. Listado de datos necesarios

**Todo proyecto de Ciencia e Ingeniería de datos parte de un mismo origen: Los datos.**
**Sin ellos, no somos capaces de obtener resultados, a pesar de contar con capacidad técnica o infraestructura.**
**¿Tienes los datos? ¿Cuáles son y en qué formato? ¿Son públicos? ¿Son de la empresa en la que trabajas? ¿Cómo esperas obtenerlos? ¿Hay algún condicionante técnico o legal?**

| ID | DEFINICIÓN / COMENTARIO | Tipo de Fichero | Origen / Fuente | Público | Disponible |
| -- | ----------------------- | --------------- | --------------- | ------- | ---------- |
| 1  | Imágenes multiespectrales Copernicus Sentinel-2 (Órbitas R008 y R051 sobre Cataluña). | `.COG` / `.pmtiles` | ESA ([Copernicus Data Space](https://dataspace.copernicus.eu/)) | Sí | Sí |
| 2  | Máscaras vectoriales de Mar y masas de agua (e.g., MASCARA_CATALUNYA_700) para forzar la exclusión del agua durante el entrenamiento. | `.gpkg` / `.shp` | ICGC ([Cartografía Hidrogeológica](https://www.icgc.cat/es/Geoinformacion-y-mapas/Datos-y-productos/Geoinformacion-geologica-y-geofisica/Cartografia-hidrogeologica/Cartografia-hidrogeologica-continua-escala-125000)) | Sí | Sí |
| 3  | Máscaras de validación generadas mediante el algoritmo original Sen2Cor para servir de línea base estadística. | `.COG` | ESA ([Copernicus Data Space](https://dataspace.copernicus.eu/)) | Sí | Sí |

**Las solicitudes de TFB deberán tener, como mínimo, un origen de dato público y disponible. Si estas contienen datos privados y/o no disponibles (por el momento), será considerado un riesgo. Deberás detallar esto, junto con otros posibles, en la siguiente sección.**

## 8. Análisis de riesgos

**Haz una lista de posibles riesgos que pueden impactar negativamente el desarrollo de tu proyecto y, para cada uno, una posible manera de solucionarlo, o una alternativa que lo evite.**

* **Riesgo:** Cuellos de botella en la memoria computacional (Out of Memory - OOM) al entrenar redes neuronales con imágenes satelitales gigantescas (10980x10980 px).
  * *Mitigación:* Se diseñará e implementará una fase estricta de *Tiling* para trocear las imágenes en parches matemáticos de 512x512 píxeles antes de introducirlos a la red neuronal.

## 9. Planificación y cronograma de trabajo

**Propón una planificación para el desarrollo del TFB. Para ello, puedes definir un cronograma en el que se incluyan las acciones necesarias y las fechas límites para el cumplimiento de dichas acciones. Compartir y consensuar esta información con tu tutor/a os permitirá coordinaros y trabajar de manera más cómoda y óptima.**

La planificación de este proyecto se basa en las fechas académicas oficiales y se alinea con los 5 objetivos técnicos planteados: Construcción de la infraestructura tecnológica (Obj. 1), Procesos ETL y obtención de datos (Obj. 2), Entrenamiento de modelos U-Net (Obj. 3), Evaluación frente a Sen2Cor (Obj. 4) y Arquitectura orientada a la nube (Obj. 5).

### Fase 1: Planificación y Propuesta Inicial
**Fechas:** 25/05/2026 – 28/06/2026
* **Hitos Académicos:**
  * VC de PLANIFICACIÓN: 25/05/2026 - 31/05/2026
  * 1ª Tutoría: 01/06/2026 - 21/06/2026
  * **Entrega 1: PROPUESTA INICIAL (22/06/2026 - 28/06/2026)**
* **Tareas Técnicas:**
  * Fundamentación teórica y definición de la arquitectura de infraestructura tecnológica (Obj. 1).
  * Análisis inicial y evaluación de las fuentes de datos satelitales para los procesos ETL (Obj. 2).

### Fase 2: Infraestructura, ETL y Metodología
**Fechas:** 29/06/2026 – 26/07/2026
* **Hitos Académicos:**
  * 2ª Tutoría: 29/06/2026 - 19/07/2026
  * **Entrega 2: DESARROLLO DEL MARCO TEÓRICO Y METODOLOGÍA (60% del avance) (20/07/2026 - 26/07/2026)**
* **Tareas Técnicas:**
  * Construcción de la infraestructura: repositorio, servidor online, prácticas DevOps y BD (Obj. 1).
  * Extracción y armonización de Copernicus Sentinel-2 mediante el desarrollo de procesos ETL (Obj. 2).
  * Diseño de la arquitectura de base de datos en la nube basada en formatos COG y PMTiles (Obj. 5).

### Fase 3: Entrenamiento Machine Learning y Evaluación
**Fechas:** 27/07/2026 – 06/09/2026
* **Hitos Académicos:**
  * 3ª Tutoría: 27/07/2026 - 30/08/2026
  * **Entrega 3: ENTREGA COMPLETA DEL TFT (100% del avance) (31/08/2026 - 06/09/2026)**
* **Tareas Técnicas:**
  * Entrenamiento de las dos redes neuronales convolucionales (tipo U-Net) por estacionalidad (Obj. 3).
  * Evaluación empírica de falsos positivos en los Pirineos y masas de agua profunda frente a Sen2Cor (Obj. 4).
  * Integración de la visualización *on the fly* en el frontend de la plataforma web interactiva.

### Fase 4: Revisión, Depósito Final y Defensa
**Fechas:** 14/09/2026 – 25/10/2026
* **Hitos Académicos:**
  * **Entrega 4: DEPÓSITO FINAL EN 1ª DEFENSA (14/09/2026 - 20/09/2026)**
  * VC informativa sobre defensas: 28/09/2026 - 04/11/2026
  * Entrega PPT defensa: 05/10/2026 - 11/10/2026
  * **Primera defensa: 12/10/2026 - 25/10/2026**
* **Tareas Técnicas:**
  * Síntesis visual de la plataforma geoespacial en la presentación de defensa.
  * Preparación de material interactivo de mapas web para la exposición oral.

### Resumen del Cronograma

| Fechas | Hito Académico | Tareas Técnicas / Desarrollo |
|--------|----------------|------------------------------|
| **25/05 - 28/06** | **Entrega 1: Propuesta Inicial** | Diseño de Infraestructura (Obj. 1) e inicio ETL (Obj. 2). |
| **29/06 - 26/07** | **Entrega 2: Metodología (60%)** | Full Stack y DevOps (Obj. 1), Procesos ETL (Obj. 2) y Arquitectura COG/PMTiles (Obj. 5). |
| **27/07 - 06/09** | **Entrega 3: Entrega Completa (100%)** | Entrenamiento U-Net (Obj. 3) y Evaluación empírica Sen2Cor (Obj. 4). |
| **14/09 - 20/09** | **Entrega 4: Depósito Final** | Corrección de formato y revisiones finales previas al tribunal. |
| **05/10 - 25/10** | **Primera Defensa ante Tribunal** | Generación de presentación (PPT) y preparación de oratoria. |