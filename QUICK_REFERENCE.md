# Quick Reference: Comandos Frecuentes
## Data Science Environment

---

## 🐍 PYTHON & VENV

### Crear venv (primera vez)
```bash
python -m venv venv
```

### Activar venv
**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Desactivar venv
```bash
deactivate
```

### Actualizar pip (recomendado)
```bash
python -m pip install --upgrade pip
```

### Instalar librerías desde requirements.txt
```bash
pip install -r requirements.txt
```

### Congelar versiones actuales (generar requirements.txt)
```bash
pip freeze > requirements.txt
```

### Ver librerías instaladas
```bash
pip list
```

### Desinstalar librería
```bash
pip uninstall pandas
```

---

## 📓 JUPYTER NOTEBOOKS

### Iniciar Jupyter Lab (RECOMENDADO)
```bash
jupyter lab
```

### Iniciar Jupyter Notebook (versión clásica)
```bash
jupyter notebook
```

### Listar kernels disponibles
```bash
jupyter kernelspec list
```

### Instalar kernel de tu venv
```bash
python -m ipykernel install --user --name venv --display-name "Python (credit-risk)"
```

---

## 🔍 TESTING & QUALITY

### Ejecutar pruebas con pytest
```bash
pytest tests/
pytest tests/test_modeling.py  # Archivo específico
pytest -v                       # Verbose (más detalles)
```

### Lint código con pylint
```bash
pylint src/preprocessing.py
```

### Format código con black
```bash
black src/
black src/modeling.py
```

### Check formato sin cambiar (dry-run)
```bash
black --check src/
```

---

## 📊 KAGGLE DATASETS

### Descargar dataset (requiere credenciales)
```bash
kaggle datasets download -d uciml/german-credit-data -p ./01-PD-Prediction/data/raw --unzip
```

### Listar datasets disponibles
```bash
kaggle datasets list -s "credit"
```

---

## 📁 FILES & DIRECTORIES

### Crear directorios
**Windows (PowerShell):**
```bash
mkdir 01-PD-Prediction\data\raw
```

**Mac/Linux:**
```bash
mkdir -p 01-PD-Prediction/data/raw
```

### Listar contenido de carpeta
```bash
ls                 # Mac/Linux
dir                # Windows
ls -la             # Incluir archivos ocultos (Mac/Linux)
```

### Navegar directorios
```bash
cd ruta/al/directorio
cd ..              # Ir un nivel arriba
cd                 # Ir a home
pwd                # Mostrar directorio actual
```

### Eliminar archivo/carpeta
```bash
rm archivo.py      # Archivo (Mac/Linux)
rm -rf carpeta/    # Carpeta recursiva (Mac/Linux)
del archivo.py     # Archivo (Windows)
rmdir carpeta      # Carpeta vacía (Windows)
```

---

## 🔗 GIT & GITHUB

### Configuración inicial (primera vez)
```bash
git config user.name "Jorge Turcott"
git config user.email "tu_email@example.com"
```

### Inicializar repositorio
```bash
git init
```

### Ver estado
```bash
git status
```

### Agregar archivos
```bash
git add .              # Todos los cambios
git add src/           # Carpeta específica
git add file.py        # Archivo específico
```

### Commits
```bash
git commit -m "Descripción clara del cambio"
git commit -m "Add XGBoost model with SHAP analysis"
```

### Ver historial
```bash
git log
git log --oneline      # Versión compacta
git log --graph --oneline --all  # Visual
```

### Ramas
```bash
git branch                      # Listar ramas
git branch feature/pd-model     # Crear rama
git checkout feature/pd-model   # Cambiar a rama
git checkout -b feature/lgd     # Crear y cambiar
```

### Merge
```bash
git merge feature/pd-model      # Merge rama a main
```

### Push a GitHub
```bash
git push origin main
git push origin feature/pd-model
```

### Pull desde GitHub
```bash
git pull origin main
```

### Clone repositorio
```bash
git clone https://github.com/usuario/credit-risk-datascience.git
```

---

## 🐍 PYTHON SCRIPTS

### Ejecutar script
```bash
python script.py
python test_environment.py
```

### Ejecutar con argumentos
```bash
python download_datasets.py --dataset german
```

### Ver ayuda
```bash
python script.py --help
python -h
```

---

## 📊 PANDAS COMANDOS COMUNES

Dentro de un Jupyter notebook o script Python:

```python
import pandas as pd

# Cargar datos
df = pd.read_csv('data.csv')
df = pd.read_parquet('data.parquet')

# Exploración
df.head()           # Primeras filas
df.tail()           # Últimas filas
df.shape            # Dimensiones
df.info()           # Tipos de datos
df.describe()       # Estadísticas

# Seleccionar datos
df[['col1', 'col2']]     # Columnas específicas
df.iloc[0:10]            # Primeras 10 filas
df[df['col'] > 5]        # Filtro

# Limpiar datos
df.dropna()              # Eliminar nulos
df.fillna(0)             # Llenar nulos
df.drop_duplicates()     # Eliminar duplicados

# Operaciones
df['new_col'] = df['col1'] + df['col2']
df.groupby('category').mean()

# Guardar
df.to_csv('output.csv', index=False)
df.to_parquet('output.parquet')
```

---

## 🤖 SKLEARN WORKFLOW

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, confusion_matrix

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features (importante para muchos algoritmos)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
auc = roc_auc_score(y_test, y_pred)
print(f"ROC-AUC: {auc:.4f}")
```

---

## 🎨 VISUALIZATION

```python
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import graph_objects as go

# Matplotlib - Static plots
plt.figure(figsize=(10, 6))
plt.hist(df['column'])
plt.title('Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()

# Seaborn - Statistical plots
sns.boxplot(data=df, x='category', y='value')
plt.savefig('boxplot.png')

# Plotly - Interactive plots
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['column']))
fig.show()
```

---

## 🔴 TROUBLESHOOTING

### Módulo no encontrado
```
ModuleNotFoundError: No module named 'xgboost'
```
**Solución:** Asegúrate que el venv está activado y ejecuta:
```bash
pip install xgboost
```

### Conflicto de versiones
**Solución:** Reinstala desde requirements.txt limpio:
```bash
pip install --upgrade -r requirements.txt
```

### Port ya en uso (Jupyter)
```bash
jupyter lab --port=8888
# o
jupyter lab --port=8889
```

### Permission denied (archivos)
```bash
chmod +x script.py  # Mac/Linux
```

---

## 📋 WORKFLOW TÍPICO

### Día 1: Setup
```bash
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python test_environment.py
jupyter lab
```

### Día 2+: Desarrollo
```bash
# Activar venv (si no está activado)
source venv/bin/activate

# Abrir Jupyter
jupyter lab

# Después de cambios: commit a Git
git add .
git commit -m "Feature description"
git push origin main
```

### Workflow Git
```bash
git status                                    # Ver cambios
git add .                                     # Preparar cambios
git commit -m "Add feature X"                 # Commit
git push origin main                          # Push a remoto
```

---

## 🎯 CHECKLIST DIARIO

- [ ] Activar venv
- [ ] Verificar rama Git (git branch)
- [ ] Abrir Jupyter Lab
- [ ] Hacer cambios
- [ ] Guardar código (Ctrl+S en editor)
- [ ] Testear cambios
- [ ] Commit a Git si son cambios importantes
- [ ] Desactivar venv antes de salir

---

## 📞 OBTENER AYUDA

### Documentación oficial
- Python: https://docs.python.org/3/
- Pandas: https://pandas.pydata.org/docs/
- scikit-learn: https://scikit-learn.org/
- XGBoost: https://xgboost.readthedocs.io/

### En Jupyter
```python
help(pd.read_csv)
pd.read_csv?           # IPython magic
```

### Stack Overflow
- Tag: `python`, `pandas`, `scikit-learn`, `xgboost`

---

**Última actualización:** Julio 2026
