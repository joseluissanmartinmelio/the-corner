# José San Martín - Sitio Personal

Este es el sitio web personal de José San Martín, construido con MkDocs Material.

## 🌐 Sitio Web

El sitio está disponible en: [https://joseluissanmartinmelio.github.io/the-corner](https://joseluissanmartinmelio.github.io/the-corner)

## 🚀 Configuración de GitHub Pages

Si el sitio no está funcionando, sigue estos pasos:

### 1. Habilitar GitHub Pages
1. Ve a **Settings** > **Pages** en tu repositorio de GitHub
2. En **Source**, selecciona **GitHub Actions**
3. Guarda los cambios

### 2. Ejecutar el workflow manualmente
1. Ve a la pestaña **Actions** en tu repositorio
2. Selecciona el workflow "Deploy MkDocs to GitHub Pages"
3. Haz clic en **Run workflow** > **Run workflow**

### 3. Verificar el deployment
- El workflow debería ejecutarse y completarse exitosamente
- El sitio estará disponible en unos minutos en la URL mencionada arriba

## 🛠️ Desarrollo Local

Para trabajar con el sitio localmente:

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
mkdocs serve

# Construir sitio para producción
mkdocs build
```

## 📁 Estructura

```
├── docs/
│   ├── index.md          # Página principal
│   ├── curriculum.md     # Currículum
│   ├── projects.md       # Proyectos
│   └── assets/
│       └── Foto_jose.jpg # Foto de perfil
├── mkdocs.yml           # Configuración de MkDocs
├── requirements.txt     # Dependencias de Python
└── .github/
    └── workflows/
        └── deploy.yml   # Workflow de GitHub Actions
```

## 📚 Documentación

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages con GitHub Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow)