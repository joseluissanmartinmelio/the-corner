#!/usr/bin/env python3
"""
Script para verificar la configuración del sitio MkDocs
"""

import os
import sys
import subprocess
import yaml

def check_mkdocs_config():
    """Verificar la configuración de MkDocs"""
    print("🔍 Verificando configuración de MkDocs...")
    
    if not os.path.exists('mkdocs.yml'):
        print("❌ No se encontró mkdocs.yml")
        return False
    
    try:
        with open('mkdocs.yml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        print(f"✅ Site name: {config.get('site_name', 'No definido')}")
        print(f"✅ Site URL: {config.get('site_url', 'No definido')}")
        print(f"✅ Theme: {config.get('theme', {}).get('name', 'No definido')}")
        
        return True
    except Exception as e:
        print(f"❌ Error al leer mkdocs.yml: {e}")
        return False

def check_docs_folder():
    """Verificar que existan los archivos de documentación"""
    print("\n📁 Verificando archivos de documentación...")
    
    if not os.path.exists('docs'):
        print("❌ No se encontró la carpeta docs/")
        return False
    
    required_files = ['index.md', 'curriculum.md', 'projects.md']
    for file in required_files:
        file_path = os.path.join('docs', file)
        if os.path.exists(file_path):
            print(f"✅ {file} existe")
        else:
            print(f"❌ {file} no existe")
            return False
    
    return True

def check_build():
    """Verificar que el sitio se pueda construir"""
    print("\n🔨 Verificando construcción del sitio...")
    
    try:
        result = subprocess.run(['mkdocs', 'build'], 
                              capture_output=True, text=True, cwd='.')
        if result.returncode == 0:
            print("✅ El sitio se construye correctamente")
            return True
        else:
            print(f"❌ Error al construir el sitio: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ MkDocs no está instalado")
        return False

def check_github_workflow():
    """Verificar el workflow de GitHub Actions"""
    print("\n⚙️ Verificando workflow de GitHub Actions...")
    
    workflow_path = '.github/workflows/deploy.yml'
    if not os.path.exists(workflow_path):
        print("❌ No se encontró el workflow de deploy")
        return False
    
    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow = yaml.safe_load(f)
        
        print("✅ Workflow de deploy encontrado")
        print(f"✅ Nombre: {workflow.get('name', 'No definido')}")
        
        # Verificar que se ejecute en push a main
        on_config = workflow.get('on', {})
        if 'push' in on_config and 'main' in on_config['push'].get('branches', []):
            print("✅ Se ejecuta en push a main")
        else:
            print("❌ No está configurado para ejecutarse en push a main")
        
        return True
    except Exception as e:
        print(f"❌ Error al leer el workflow: {e}")
        return False

def main():
    print("🚀 Verificando configuración del sitio MkDocs para GitHub Pages\n")
    
    checks = [
        check_mkdocs_config(),
        check_docs_folder(),
        check_build(),
        check_github_workflow()
    ]
    
    if all(checks):
        print("\n🎉 ¡Todas las verificaciones pasaron!")
        print("\n📋 Pasos adicionales para verificar:")
        print("1. Ve a Settings > Pages en tu repositorio de GitHub")
        print("2. Asegúrate de que 'Source' esté configurado como 'GitHub Actions'")
        print("3. Verifica que el workflow se haya ejecutado en la pestaña 'Actions'")
        print("4. El sitio debería estar disponible en: https://joseluissanmartinmelio.github.io/the-corner")
    else:
        print("\n❌ Algunas verificaciones fallaron. Revisa los errores arriba.")
    
    return 0 if all(checks) else 1

if __name__ == '__main__':
    sys.exit(main())
