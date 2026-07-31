#!/usr/bin/env python3
"""
Download Datasets Script
Descarga automáticamente los datasets recomendados de Kaggle para los proyectos
"""

import os
import sys
import subprocess
from pathlib import Path

# Datasets recomendados por proyecto
DATASETS = {
    "01-PD-Prediction": {
        "german": "uciml/german-credit-data",
        "lending": "wordsforthewise/lending-club",  # Comentado - es muy grande (~5GB)
        "home-credit": "kaggle/kaggle-survey-2023",  # Alternativa más pequeña
    },
    "02-LGD-Modeling": {
        "loan-default": "wordsforthewise/lending-club",
    },
}

def check_kaggle_installed():
    """Verifica si kaggle CLI está instalado"""
    try:
        subprocess.run(["kaggle", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_kaggle_credentials():
    """Verifica si las credenciales de Kaggle están configuradas"""
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    return kaggle_json.exists()

def download_dataset(dataset_id: str, destination: Path):
    """Descarga un dataset de Kaggle"""
    destination.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📥 Descargando: {dataset_id}")
    print(f"   Destino: {destination}")
    
    try:
        # Comando de Kaggle
        cmd = f'kaggle datasets download -d {dataset_id} -p "{destination}" --unzip'
        
        # En Windows usa shell=True, en Unix no
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"   ✅ Descarga exitosa")
            return True
        else:
            print(f"   ❌ Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"   ❌ Excepción: {e}")
        return False

def main():
    print("="*60)
    print("KAGGLE DATASETS DOWNLOADER")
    print("="*60)
    
    # Verificar Kaggle CLI
    if not check_kaggle_installed():
        print("\n❌ Kaggle CLI no está instalado")
        print("   Instala con: pip install kaggle")
        sys.exit(1)
    
    # Verificar credenciales
    if not check_kaggle_credentials():
        print("\n❌ Credenciales de Kaggle no configuradas")
        print("   1. Ve a https://kaggle.com/settings/account")
        print("   2. Haz clic en 'Create New API Token'")
        print("   3. Guarda kaggle.json en ~/.kaggle/")
        print("   4. Ejecuta: chmod 600 ~/.kaggle/kaggle.json")
        sys.exit(1)
    
    print("\n✅ Kaggle CLI configurado correctamente\n")
    
    # Opción interactiva
    print("Datasets disponibles para descargar:\n")
    print("1. German Credit (pequeño, 🟢 recomendado para empezar)")
    print("2. Lending Club (grande, ~5GB, requiere mucho espacio)")
    print("3. Home Credit (mediano, 🟡 buen equilibrio)")
    print("4. Todos los pequeños/medianos (1 + 3)")
    print("0. Salir sin descargar")
    
    choice = input("\nSelecciona opción (0-4): ").strip()
    
    datasets_to_download = []
    
    if choice == "1":
        datasets_to_download = [
            ("01-PD-Prediction/data/raw", "uciml/german-credit-data")
        ]
    elif choice == "2":
        datasets_to_download = [
            ("01-PD-Prediction/data/raw", "wordsforthewise/lending-club")
        ]
    elif choice == "3":
        datasets_to_download = [
            ("01-PD-Prediction/data/raw", "kaggle/kaggle-survey-2023")
        ]
    elif choice == "4":
        datasets_to_download = [
            ("01-PD-Prediction/data/raw", "uciml/german-credit-data"),
            ("01-PD-Prediction/data/raw", "kaggle/kaggle-survey-2023"),
        ]
    else:
        print("\n👋 Sin descargas. Saliendo.")
        sys.exit(0)
    
    # Descargar datasets
    success_count = 0
    for dest_path, dataset_id in datasets_to_download:
        dest = Path(dest_path)
        if download_dataset(dataset_id, dest):
            success_count += 1
    
    # Resumen
    print("\n" + "="*60)
    print(f"Descarga completada: {success_count}/{len(datasets_to_download)} exitosas")
    print("="*60 + "\n")
    
    print("Próximos pasos:")
    print("  1. jupyter lab")
    print("  2. Abre 01-PD-Prediction/notebooks/00_setup_test.ipynb")
    print("  3. ¡Comienza tu primer proyecto!\n")

if __name__ == "__main__":
    main()
