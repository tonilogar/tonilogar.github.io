# Actividad 1 - Cloud Computing: Containerization with Docker and FastAPI project setup

**Alumno:** Antonio López García
**Profesor:** Ramon Amela Milian
**Fecha de entrega:** 22-06-2026

## Tareas a realizar y progreso

### 1. Git (25%)
- [ ] Crear repositorio privado en GitHub e inicializarlo con el código base.
- [ ] Invitar al usuario `@ramonamela` como colaborador.
- [ ] Copiar la plantilla (`activity_1_template`) al nuevo proyecto.
- [ ] Hacer el primer commit con el mensaje "First commit".

### 2. Docker (20%)
- [ ] Añadir los requerimientos necesarios al proyecto (`requirements.txt` o `pyproject.toml`).
- [ ] Configurar el `Dockerfile` añadiendo los *targets* (etapas multi-stage) necesarios para un proyecto cloud escalable.

### 3. Docker Compose (25%)
- [ ] Modificar `docker-compose.yml` para usar el *target* adecuado del `Dockerfile`.
- [ ] Modificar `docker-compose.yml` para utilizar un archivo de variables de entorno (`.env`).
- [ ] Mapear el puerto del proyecto del 80 al deseado (por ejemplo, `8080:80` o `8000:80`).
- [ ] Incluir un servicio/target en el `docker-compose` para formatear el código. Comando:
      `entrypoint: sh -c "black --config .black . && ruff check --fix"`
      *(Requiere instalar `black` 24.1.0 y `ruff` 0.1.14)*.

### 4. Setup del Proyecto FastAPI (30%)
- [ ] Crear dos "apps" (módulos/carpetas) separadas: `authentication` y `files`.
- [ ] Crear *routers* (FastAPI APIRouter) dentro de cada aplicación.
- [ ] Importar los nuevos *routers* en el archivo principal (`main.py`).
- [ ] Crear los siguientes *endpoints* (solo devolver 200 OK, sin lógica de negocio, documentados en Swagger):
  - **Authentication:**
    - `POST /register`
    - `POST /login`
    - `POST /logout`
    - `GET /introspect`
  - **Files:**
    - `GET /files`
    - `POST /files`
    - `GET /files/{id}`
    - `POST /files/{id}`
    - `DELETE /files/{id}`
    - `POST /files/merge`

## Entregables Finales
- Código del proyecto comprimido (.zip).
- Hash del commit exacto de GitHub entregado a través del campus virtual.

---
**Commit Hash de entrega:** *(Pendiente)*
