#!/usr/bin/env python3
"""
Test Environment Script
Verifica que todas las librerías de data science estén instaladas correctamente
"""

import sys
import importlib
from pathlib import Path

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}{text:^60}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")

def test_library(lib_name: str, import_name: str = None, version_attr: str = "__version__"):
    """Test if a library is installed and accessible"""
    if import_name is None:
        import_name = lib_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, version_attr, "No version info")
        print(f"{GREEN}✓{RESET} {lib_name:25} | v{version}")
        return True
    except ImportError as e:
        print(f"{RED}✗{RESET} {lib_name:25} | NOT INSTALLED")
        return False
    except Exception as e:
        print(f"{YELLOW}!{RESET} {lib_name:25} | Error: {str(e)[:40]}")
        return False

# Main testing
print_header("CREDIT RISK DATA SCIENCE ENVIRONMENT TEST")

print(f"Python Version: {sys.version}")
print(f"Python Executable: {sys.executable}")
print(f"Working Directory: {Path.cwd()}")

# Test Core Libraries
print_header("Core Data Processing")
test_library("pandas", "pandas")
test_library("numpy", "numpy")

# Test ML Libraries
print_header("Machine Learning Libraries")
test_library("scikit-learn", "sklearn")
test_library("xgboost", "xgboost")
test_library("lightgbm", "lightgbm")
test_library("catboost", "catboost")

# Test Interpretability
print_header("Model Interpretability & Explainability")
test_library("SHAP", "shap")
test_library("LIME", "lime")

# Test Visualization
print_header("Visualization Libraries")
test_library("matplotlib", "matplotlib")
test_library("seaborn", "seaborn")
test_library("plotly", "plotly")

# Test Jupyter & Computing
print_header("Jupyter & Interactive Computing")
test_library("jupyter", "jupyter")
test_library("jupyterlab", "jupyterlab")
test_library("IPython", "IPython")
test_library("ipykernel", "ipykernel")

# Test Statistical
print_header("Statistical Analysis")
test_library("scipy", "scipy")
test_library("statsmodels", "statsmodels")

# Test Utilities
print_header("Utilities & Tools")
test_library("pandas-profiling", "pandas_profiling")
test_library("python-dotenv", "dotenv")
test_library("tqdm", "tqdm")

# Test Optional/Advanced
print_header("Optional Advanced Libraries")
test_library("streamlit", "streamlit")
test_library("sqlalchemy", "sqlalchemy")

# Final verification
print_header("ENVIRONMENT VERIFICATION COMPLETE")
print(f"{GREEN}✓ Your environment is ready for Credit Risk Data Science!{RESET}\n")

# Quick sanity check
print("Quick sanity check...")
try:
    import pandas as pd
    import numpy as np
    import sklearn
    import xgboost as xgb
    import shap
    import matplotlib.pyplot as plt
    
    print(f"{GREEN}✓ All critical imports successful{RESET}")
    print(f"\n{GREEN}Ready to start: Coursera ML Specialization{RESET}")
    print(f"  1. Open Jupyter: {YELLOW}jupyter lab{RESET}")
    print(f"  2. Download dataset from Kaggle")
    print(f"  3. Start with 01-PD-Prediction/notebooks/\n")
    
except ImportError as e:
    print(f"{RED}✗ Critical import failed: {e}{RESET}")
    print(f"   Please ensure all libraries in requirements.txt are installed")
    print(f"   Run: {YELLOW}pip install -r requirements.txt{RESET}")
