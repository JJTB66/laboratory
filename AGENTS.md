# AGENTS.md — Reglas para agentes de IA / Rules for AI agents

Las siguientes reglas son OBLIGATORIAS. Cualquier agente de IA debe leerlas y verificarlas **antes** de modificar o realizar cualquier cambio en este repositorio.

The following rules are MANDATORY. Any AI agent must read and verify them **before** modifying or making any change in this repository.

## 1. Entorno / Environment

- Usar SIEMPRE el virtualenv del proyecto: `venv\Scripts\python.exe` (Python 3.12.10, Django 6.1.1).
  Always use the project virtualenv: `venv\Scripts\python.exe`.
- Ejecutar los comandos de Django siempre a través de `manage.py` (`runserver`, `makemigrations`, `migrate`, `startapp`, etc.).
  Run Django commands always through `manage.py`.
- No instalar paquetes fuera del virtualenv.
  Do not install packages outside the virtualenv.

## 2. Antes de modificar / Before making changes

- Leer este archivo completo antes de cualquier cambio.
  Read this entire file before any change.
- Comprender la estructura del proyecto (`config/`, aplicaciones, modelos, URLs) antes de tocar código.
  Understand the project structure (`config/`, apps, models, URLs) before touching code.
- Consultar `git status` para conocer el estado del working tree.
  Run `git status` to know the working tree state.
- No modificar `db.sqlite3`, `.env`, secretos ni datos generados sin aviso explícito.
  Do not modify `db.sqlite3`, `.env`, secrets, or generated data without an explicit warning.

## 3. Reglas de código / Code rules

- Seguir las convenciones de Django y PEP 8.
  Follow Django and PEP 8 conventions.
- No agregar comentarios en el código salvo que se pidan explícitamente.
  Do not add code comments unless explicitly requested.
- Nunca subir secretos, claves o tokens al repositorio (ej. `SECRET_KEY` en producción).
  Never commit secrets, keys, or tokens to the repository.
- Ejecutar `venv\Scripts\python.exe manage.py check` después de cambios para validar el proyecto.
  Run `manage.py check` after changes to validate the project.

## 4. Git

- No hacer commits a menos que el usuario lo pida explícitamente.
  Do not commit unless the user explicitly asks.
- Mensajes de commit claros, en español, de preferencia <= 50 caracteres.
  Clear commit messages, in Spanish, preferably <= 50 characters.
- No hacer push ni crear PRs sin autorización explícita.
  Do not push or create PRs without explicit authorization.