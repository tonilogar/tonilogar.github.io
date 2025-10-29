# Versión estática para GitHub Pages

Esta carpeta contiene una versión 100 % estática de la aplicación usando **HTML, CSS y JavaScript**.
Puedes publicarla en GitHub Pages o cualquier hosting estático.

## Configuración

1. Crea (o reutiliza) la tabla `user_names` en tu proyecto de Supabase.
2. Abre `config.js` y reemplaza:
   - `SUPABASE_URL` por la URL de tu proyecto (`https://xxxxx.supabase.co`).
   - `SUPABASE_ANON_KEY` por la **anon public key** (Settings → API → Project API keys).
3. Opcional: personaliza estilos en `styles.css`.

## Publicación

1. Sube la carpeta `github_pages` a tu repositorio.
2. En GitHub, ve a *Settings → Pages* y selecciona la rama y carpeta (`/github_pages`).
3. Espera a que GitHub procese el sitio y accede a la URL generada.

> **Importante:** la clave anónima de Supabase es pública por diseño, pero garantiza que las políticas RLS y permisos de la tabla están restringidos a las operaciones necesarias (`insert` y `select`) antes de exponerla.
