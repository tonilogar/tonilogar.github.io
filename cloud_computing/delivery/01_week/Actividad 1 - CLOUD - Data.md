# Servicios de cloud computing
**Profesor:** Ramon Amela Milian
**Práctica:** Contenerización con Docker y configuración de un proyecto FastAPI

## Datos de la actividad
| Campo | Valor |
| --- | --- |
| **Número de actividad** | 1 |
| **Profesor** | Ramon Amela Milian |
| **Idioma de impartición** | Inglés |
| **Agrupación** | Individual |
| **Fecha de entrega** | 22-06-2026 |

## Descripción de la actividad
En esta actividad, se trabajarán los principios de la contenerización. El alumno aprenderá a contenerizar y lanzar un servicio HTTP con todas sus dependencias. Al construir un contenedor Docker, el alumno se asegurará de que sea altamente portátil y fácilmente desplegable en cualquier proveedor de nube pública. El trabajo comenzará a partir de un proyecto funcional minimalista de FastAPI.

Para minimizar el tiempo invertido en configurar el entorno, se proporcionan instrucciones sobre cómo virtualizar un Ubuntu 22.04.4 LTS en el campus virtual.

## Competencias
**CE3** – Diseñar y gestionar sistemas de información para el tratamiento y almacenamiento de datos.

| COMPETENCIAS (CE / CT) | RESULTADOS DE APRENDIZAJE (RA) | INDICADORES DE EVALUACIÓN (IE) |
| :--- | :--- | :--- |
| **CE3** | **RA1** – Resumir la evolución histórica y las oportunidades actuales en la administración de sistemas de datos en entornos cloud. | **IE1** – El alumno comprende y utiliza técnicas modernas de virtualización empleadas en la administración de sistemas. |
| | **RA3** – Justificar el uso de tecnologías cloud para garantizar la escalabilidad, accesibilidad y coherencia de una solución de software. | **IE7** – El alumno es capaz de lanzar una aplicación personalizada en un entorno virtualizado. |

---

## Contenidos de la actividad
- **Git**
  - Inicialización del proyecto
  - Uso de un repositorio público en la nube
- **Docker**
  - Capacidad para añadir *targets* (etapas de construcción) y modificarlos
- **Docker compose**
  - Capacidad para modificar *targets* existentes con las modificaciones más habituales
  - Capacidad para crear nuevos *targets*
- **Configuración del proyecto**
  - Capacidad para crear nuevos EP (Endpoints)
  - Capacidad para usar correctamente el *router*
  - Capacidad para estandarizar el proceso de desarrollo mediante formateadores de código

---

## Descripción de las tareas
Para lograr los objetivos presentados en la descripción, el alumno seguirá los siguientes pasos:

- Crear cuentas de GitHub para cada uno de los participantes del proyecto.
- Crear un repositorio privado en GitHub e inicializarlo con el código proporcionado.
- Invitar al usuario `@ramonamela` como colaborador del proyecto creado.
- Copiar la plantilla del proyecto en el proyecto recién creado.
- Hacer el primer commit con el mensaje `"First commit"`.
- Añadir los requisitos (dependencias) necesarios al proyecto.
- Añadir tantos *targets* en el archivo `Dockerfile` como se considere que debe tener un proyecto cloud escalable.
- Modificar el archivo `docker-compose` para usar el *target* creado previamente.
- Modificar el archivo `docker-compose` para usar un archivo de variables de entorno (`.env`).
- Modificar el archivo `docker-compose` para mapear el puerto del proyecto del `80` al puerto deseado (los puertos sugeridos son 8080 u 8000, pero se puede elegir cualquier otra opción razonable).
- Incluir un *target* en el `docker-compose` para formatear el código del proyecto. Esto se hará mediante el siguiente comando:
  - `entrypoint: sh -c "black --config .black . && ruff check --fix"`
  - *Ten en cuenta que, para ejecutar el comando anterior, deben estar instaladas la versión 24.1.0 de `black` y la versión 0.1.14 de `ruff`.*
- En el proyecto FastAPI:
  - Crear dos "apps" (módulos) llamadas `"authentication"` y `"files"`.
  - Crear *routers* dentro de ambas aplicaciones nuevas.
  - Importar los nuevos *routers* desde el archivo principal.
  - Crear los siguientes *endpoints* en los *routers* recién creados:
    - **Authentication:**
      - `register` – POST
      - `login` – POST
      - `logout` – POST
      - `introspect` – GET
    - **Files:**
      - `files` – GET
      - `files` – POST
      - `files/{id}` – GET
      - `files/{id}` – POST
      - `files/{id}` – DELETE
      - `files/merge` – POST

*Nota: Estos endpoints deben aparecer en el archivo de Swagger y devolver siempre un código 200. En este entregable, no se implementará ninguna lógica de negocio en los endpoints.*

Los pasos anteriores se pueden agrupar en los siguientes puntos resumen:
1. Git
2. Docker
3. Docker compose
4. Configuración del proyecto (Project setup)

---

## Aspectos formales de las tareas
Todo el código del proyecto debe entregarse en **formato comprimido** a través del campus virtual. Además, en el texto entregado, se debe incluir el **hash del commit** con el código subido a GitHub. Este hash debe contener exactamente la misma versión del código que se entrega.

| Tarea | Porcentaje |
| --- | --- |
| 1. Git | 25% |
| 2. Docker | 20% |
| 3. Docker compose | 25% |
| 4. Configuración del proyecto | 30% |

## Evaluación
| Número | Tarea | Peso de la nota | IE |
| --- | --- | --- | --- |
| 1 | Contenerización con Docker y configuración de un proyecto FastAPI | 20% | IE1, IE7 |

## Recursos de información
- Cápsulas y videoconferencias.
