# Portfolio Profesional — Django Web App https://kevinlarguia.pythonanywhere.com/
<img width="1698" height="889" alt="image" src="https://github.com/user-attachments/assets/491dc667-1daf-4158-8d64-a5649e6a80f8" />


Portfolio profesional desarrollado con Django 6.0 y diseño dark **terminal-inspired** completamente responsive. Soporte bilingüe (ES/EN), gestión dinámica vía admin, búsqueda y filtros avanzados, animaciones scroll-reveal, y más.

## 🛠 Tecnologías

- **Backend:** Python 3 / Django 6.0
- **Frontend:** HTML5, CSS3 (sin framework), vanilla JS, Bootstrap Icons
- **Tipografía:** JetBrains Mono + Manrope (Google Fonts)
- **Base de datos:** SQLite 3
- **i18n:** sistema nativo de Django (gettext), sin dependencias externas

## ✨ Features

- **Bilingüe ES/EN** — botón de toggle en el navbar con bandera 🇦🇷 / 🇬🇧, persistente por sesión
- **Tema dark "terminal/dev"** con paleta lima neón + ámbar
- **Hero interactivo** con typewriter effect bilingüe, terminal mock animada y parallax sutil
- **Contador animado** de estadísticas
- **Filtros por tecnología** y buscador full-text en proyectos
- **Destacados primero** en el listado de proyectos (controlado por flag `destacado` desde el admin)
- **Timeline vertical** con íconos por tipo (trabajo / educación / proyecto / certificación)
- **Formulario de contacto** con validación client-side, contador de caracteres, copiar al portapapeles
- **Progress bar de scroll** y botón "volver arriba"
- **Scroll reveal** animaciones (IntersectionObserver)
- **Page loader** inicial y meta tags OpenGraph
- **Fully responsive** — mobile-first desde 320px

## 🚀 Instalación

```bash
# 1. Entorno virtual
python -m venv venv
source venv/Scripts/activate   # Git Bash en Windows
# venv\Scripts\activate         # CMD en Windows
# source venv/bin/activate      # Linux/Mac

# 2. Dependencias
pip install -r requirements.txt

# 3. Migraciones
python manage.py migrate

# 4. Servidor
python manage.py runserver
```

## 🌐 Traducciones

Las traducciones inglés ya vienen compiladas en `locale/en/LC_MESSAGES/django.mo`.

Si modificás algún texto y querés regenerar las traducciones, editá `locale/en/LC_MESSAGES/django.po` y ejecutá:

```bash
python compile_translations.py
```

Este script es una implementación pura en Python del `msgfmt` de gettext, así que **no necesitás instalar gettext en tu sistema** (útil en Windows).

## 📁 Estructura

```
portfolio/
├─ app_portfolio/
│  ├─ models.py, views.py, admin.py, urls.py
│  └─ templates/       # base, home, proyectos, trayectoria, contacto
├─ portfolio_root/
│  ├─ settings.py
│  └─ urls.py
├─ locale/en/LC_MESSAGES/
│  ├─ django.po
│  └─ django.mo
├─ static/
│  ├─ css/main.css
│  └─ js/main.js
├─ compile_translations.py
├─ db.sqlite3
└─ manage.py
```

Desarrollado con ♥ por Kevin Larguia — 2026.
