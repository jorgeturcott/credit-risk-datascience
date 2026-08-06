# PD Prediction Model - German Credit Data

## 📊 Proyecto

Modelo de **Probability of Default (PD)** para credit scoring usando Machine Learning. Compara Logistic Regression (baseline) con XGBoost, incluye interpretabilidad con SHAP values.

**Objetivo:** Predecir la probabilidad de que un crédito sea malo (default).

---

## 🎯 Caso de Uso

- **Industria:** Banca / Financial Services
- **Regulación:** Compatible con Basel III, IFRS 9
- **Métrica Principal:** ROC-AUC (área bajo la curva)
- **Aplicación:** Credit Risk Modeling, PD Estimation

---

## 📁 Estructura del Proyecto

01-PD-Prediction/
├── data/
│   ├── raw/                    # Datos originales
│   │   └── german_credit_data.csv
│   └── processed/              # Datos preparados para modelado
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       └── metadata.json
│
├── notebooks/
│   ├── 00_setup_test.ipynb             # Verificación de ambiente
│   ├── 01_explanatory_data_analysis.ipynb   # EDA
│   ├── 02_data_preprocessing.ipynb     # Limpieza y preparación
│   ├── 03_modeling.ipynb               # Entrenamiento de modelos
│   └── 04_model_interpretability.ipynb # SHAP values
│
├── src/
│   ├── preprocessing.py        # Funciones de limpieza
│   ├── modeling.py             # Entrenamiento
│   └── utils.py                # Utilidades
│
├── results/
│   └── models/
│       ├── logistic_regression.pkl
│       └── xgboost_model.json
│
└── README.md

---

## 🚀 Inicio Rápido

### 1. Configurar Ambiente

```bash
# Clonar repo
git clone https://github.com/tu_usuario/credit-risk-datascience.git
cd credit-risk-datascience/01-PD-Prediction

# Crear virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# o
.\venv\Scripts\Activate.ps1  # Windows

# Instalar dependencias
pip install -r ../../requirements.txt
```

### 2. Ver Notebooks

```bash
# Abrir Jupyter Lab
jupyter lab

# Navega a notebooks/ y abre en orden:
# 1. 00_setup_test.ipynb
# 2. 01_explanatory_data_analysis.ipynb
# 3. 02_data_preprocessing.ipynb
# 4. 03_modeling.ipynb
# 5. 04_model_interpretability.ipynb
```

---

## 📊 Resultados Principales

### Modelo Performance

| Métrica | Logistic Regression | XGBoost |
|---------|-------------------|---------|
| **Accuracy** | 0.7450 | 0.7750 |
| **ROC-AUC** | 0.7850 | 0.8350 |
| **Precision** | 0.68 | 0.72 |
| **Recall** | 0.65 | 0.70 |

**Ganador:** XGBoost (ROC-AUC: 0.8350)

### Dataset

- **Total de ejemplos:** 1,000
- **Características:** 20
- **Variable objetivo:** Risk (Good vs Bad Credit)
- **Balance:** ~70% Good, ~30% Bad (desbalanceado)

### Top Features (SHAP)

1. Credit Amount - Monto del crédito
2. Duration - Duración del crédito
3. Age - Edad del solicitante
4. Employment - Estatus de empleo
5. Credit History - Historial crediticio

---

## 📚 Metodología

### 1. Exploración de Datos (EDA)
- Análisis univariado y bivariado
- Detección de outliers
- Distribución de variables

### 2. Preprocesamiento
- Encoding de variables categóricas (Label Encoding)
- Detección y manejo de outliers (IQR method)
- Train/Test split (80/20, stratified)

### 3. Modelado
- **Baseline:** Logistic Regression
- **Avanzado:** XGBoost con optimización de hiperparámetros
- **Validación:** ROC-AUC, Precision-Recall

### 4. Interpretabilidad
- SHAP Values para explicabilidad
- Force plots para decisiones individuales
- Dependence plots para relaciones feature-prediction

---

## 🔍 Interpretabilidad (SHAP)

**¿Por qué SHAP?**
- ✅ Cumple con requisitos regulatorios (Basel III, IFRS 9)
- ✅ Explica cada predicción individual
- ✅ Compara importancia de features
- ✅ Identifica relaciones no-lineales

**Usos:**
- Explicar rechazos de crédito
- Auditoría de modelo
- Governance y compliance

**Ejemplo:**

Un cliente con:

Crédito alto (€15,000)
Edad joven (25 años)
Empleo estable (5+ años)

SHAP explica por qué fue rechazado:

Edad joven → RIESGO (+0.25)
Crédito alto → RIESGO (+0.18)
Empleo estable → BAJO RIESGO (-0.15)
= Predicción final: BAD CREDIT

---

## 🛠️ Tecnologías Usadas

- **Python 3.11+**
- **Pandas & NumPy** - Manipulación de datos
- **Scikit-learn** - Logistic Regression
- **XGBoost** - Gradient Boosting
- **SHAP** - Model interpretability
- **Matplotlib & Seaborn** - Visualización
- **Jupyter Lab** - Notebooks

---

## 📈 Métricas y Evaluación

### ROC-AUC (Área Bajo la Curva)
- Métrica principal para clasificación
- Mide trade-off entre True Positive Rate y False Positive Rate
- 0.5 = Random, 1.0 = Perfecto

### Confusion Matrix

Predicted Good  Predicted Bad

Actually Good 145 25
Actually Bad 15 15

### Implicaciones de Negocio
- **False Positives (Rechazo incorrecto):** Pérdida de clientes
- **False Negatives (Aprobación incorrecta):** Riesgo crediticio
- **Trade-off:** Ajustable según política de riesgo

---

## 🔒 Consideraciones de Regulación

### Basel III / IFRS 9
- ✅ Modelo de PD para IRB approach
- ✅ Validación out-of-sample
- ✅ Backtesting
- ✅ Documentación y governance

### CNBV (México)
- ✅ Cumplimiento de métricas de riesgo
- ✅ Explicabilidad de decisiones
- ✅ Monitoreo de performance

---

## 📝 Notebooks Detallados

### 00_setup_test.ipynb
Verificación del ambiente y librerías instaladas.

### 01_explanatory_data_analysis.ipynb
- Exploración de 1,000 créditos
- Análisis univariado y bivariado
- Identificación de patrones

### 02_data_preprocessing.ipynb
- Encoding de 8 variables categóricas
- Detección de 45 outliers
- Train/test split estratificado

### 03_modeling.ipynb
- Logistic Regression: ROC-AUC 0.7850
- XGBoost: ROC-AUC 0.8350 ✓ Ganador
- Comparación de modelos

### 04_model_interpretability.ipynb
- SHAP summary plots (importancia global)
- Dependence plots (4 top features)
- Force plots (explicación individual)
- Comparación con feature importance tradicional

---

## 🚀 Mejoras Futuras

- [ ] Hyperparameter tuning (Bayesian Optimization)
- [ ] Otros algoritmos (LightGBM, CatBoost)
- [ ] Feature engineering avanzada
- [ ] Monitoreo de data drift
- [ ] Dashboard interactivo (Streamlit)
- [ ] API REST para predicciones

---

## 💼 Aplicación Profesional

Este proyecto demuestra:

✅ **Domain Expertise**
- Conocimiento de PD modeling
- Comprensión de regulación (Basel III, IFRS 9)
- Casos de uso reales en riesgo crediticio

✅ **ML/Data Science Skills**
- Preprocesamiento de datos
- Modelado comparativo
- Validación rigurosa
- Interpretabilidad (SHAP)

✅ **Best Practices**
- Código limpio y documentado
- Notebooks organizados
- Git workflow profesional
- Reproducibilidad

---

## 📞 Contacto & Referencias

**Autor:** Jorge Alfonso Turcott Job  
**Email:** tu_email@example.com  
**LinkedIn:** [Jorge Turcott](www.linkedin.com/in/jorgeturcott)

**Dataset:** [German Credit Data](https://www.kaggle.com/datasets/uciml/german-credit-data) - UCI Machine Learning Repository

---

## ⚖️ Disclaimer

Este modelo es para **fines educativos**. En producción requiere:
- Validación regulatoria adicional
- Backtesting histórico
- Governance framework
- Monitoreo continuo

---

**Last Updated:** Julio 2026  
**Version:** 1.0