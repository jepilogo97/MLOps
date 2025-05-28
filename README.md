# 🩺 Medical Diagnosis AI Challenge
# MLOps Sample Pipeline Design -> V2.0

## 📚 Objective

This project delivers a production-ready pipeline to predict **a patient's disease severity** based on symptoms and demographic information. The solution supports both **common** and **rare (orphan) diseases**, overcoming challenges like **data imbalance**, **label noise**, and **privacy constraints**.

The final solution is accessible to medical professionals via either:
- a **local desktop interface**, or
- a **remote API** hosted on a cloud platform or institutional server.

---

## 🧠 Problem Definition

### 🏗️ Model Training

Models are trained offline by a data science team using clinical records with features such as:
- Patient symptoms
- Demographic data (e.g., age, sex, family history)
- Historical medical information

Each file must be:
- Cleaned and preprocessed
- Enriched with engineered features
  - Based on the patient row
  - Aggregates across the dataset
  - External medical knowledge sources

Model evaluation is decoupled from training to maintain consistency and ensure proper validation.

---

### 🔍 Prediction Task

On a daily basis, new patient data is ingested. The system must process this data and **generate predictions for each patient** in real-time, ensuring quick and reliable feedback for healthcare professionals.

Predictions must be generated instantly to support medical workflows and time-sensitive clinical decisions.

---

## 🛠️ MLOps Pipeline Architecture

The system is divided into four core components:
1. **Data Management**
2. **Model Lifecycle (Training/Validation/Deployment)**
3. **Serving Infrastructure**
4. **Monitoring & Retraining**

---

## ⚙️ Assumptions

- The model operates under **low-resource constraints** when used locally.
- When deployed remotely, the **API endpoint must support secure authentication**.
- The medical data used respects **HIPAA/GDPR compliance**.
- All pipeline stages must be **containerized and reproducible**.
- The deployment supports **real-time inference only**.

---

## 🛠️ Part 1: Machine Learning Pipeline Design

The following pipeline is proposed for the end-to-end system:

## 🧩 Design

The first phase of the pipeline focuses on understanding the constraints and nature of the data. In the medical domain, various technical and ethical considerations must be accounted for during model development.

### ⚠️ Restrictions and Limitations

- **Data imbalance**: Some diseases are well-documented, while others (rare/orphan diseases) have very few records.
- **Privacy and Ethics**: Medical data must strictly comply with privacy laws and ethical regulations such as **HIPAA** and **GDPR**.
- **Incomplete or noisy labels**: Diagnoses may be imprecise, ambiguous, or even incorrect, introducing noise into the learning process.
- **High dimensionality**: Patient data often includes hundreds of features (symptoms, tests, notes), increasing the risk of **overfitting** and the need for careful feature selection.

### 📊 Available Data Types

The system will process a wide variety of structured and unstructured data sources:

- **Symptomatology** – _Text / Binary_
- **Clinical study results** – _Numeric / Images_
- **Demographic data** – _Numeric / Categorical_
- **Medical history** – _Numeric / Categorical / Clinical notes_

Additionally, labeled tags can include:
- **Specific disease** – _Categorical_
- **Type of disease** – _Numeric_

![Design Diagram](https://github.com/user-attachments/assets/299e1466-caf4-4bca-9546-f1aa78272682)


## 🛠️ Development

The development phase involves gathering and preprocessing diverse medical datasets, selecting suitable machine learning models, handling class imbalance and data scarcity, and rigorously validating model performance.

### 📥 Data Sources

Medical data is obtained from a combination of:
- **Electronic Health Records (EHR)**
- **Public APIs** NIH, Orphanet, and MIMIC-III
- **CSVs and relational databases**
- **Cloud storage & version control** (Amazon S3, Redshift, DVC)

### 🧹 Preprocessing

Before model training, data undergoes several preprocessing steps:
- Handling **missing values**
- **Normalizing** numerical features
- **Categorical** encoding (OneHot, Target Encoding)
- **Feature scaling** (Z-score, MinMax)
- Text **normalization** for clinical notes

Tools used: `pandas`, `NumPy`, `scikit-learn`, `great_expectations`

### 🧠 Type of Models

A variety of models are explored, including:
- **Tree-based models**: Random Forest, XGBoost
- **Deep Learning**: CNNs, RNNs or Transformer-based models
- **Bayesian and probabilistic models**

**Model selection** usually favors **XGBoost** for structured symptom and demographic data due to its superior accuracy, speed, and ability to manage imbalanced datasets effectively.

Frameworks: `scikit-learn`, `PyTorch`, `TensorFlow`

### 🧬 Data Management Strategies

To address challenges posed by rare diseases:
- **Synthetic data generation** (e.g., SMOTE, GANs)
- **Transfer learning or meta-learning**
- Custom strategies for **limited data scenarios**

Tools: `scikit-learn`, `learn2learn`, synthetic data libraries

### ✅ Validation

Model evaluation considers the specific context of class imbalance and medical prediction:

- **Stratified validation**
- **Cross-validation**
- Metrics used: `F1-score`, `AUC-ROC`, `sensitivity`, `specificity`

Framework: `scikit-learn`

![Design Diagram](https://github.com/user-attachments/assets/8fa7012e-f92d-4dbe-b730-4b27cd11d6af)


## 🚀 Production

In the production phase, the trained models are deployed to serve predictions in real-time. This stage also includes monitoring and retraining pipelines to ensure long-term model reliability.

### 📦 Deployment

### ⚙️ Infrastructure Options

| Mode      | Stack                               |
|-----------|-------------------------------------|
| Local     | `Docker`, `Streamlit` GUI           |
| Remote    | `FastAPI` + `Uvicorn` on `EC2`      |

---

### 🌐 API Serving

Expose the model via a RESTful API using `FastAPI`.

- `POST /predict` – Returns prediction and SHAP-based explanation.
- Interactive docs available via Swagger UI.
- Designed for easy integration into healthcare systems.

---

### 📦 Containerization

Ensure reproducible and portable deployments using `Docker`.

- All components are fully containerized.
- Build automation via GitHub Actions on `main` push.
- Deployment options:
- Deployment options:
  - **Local**:
    - `docker-compose` setup
    - Includes a `Streamlit` interface for medical staff to input patient data and receive predictions
  - **Remote**:
    - Hosted on an `AWS EC2` instance running `Docker` or `docker-compose`
    - SSH access for manual or automated deployment
    - Recommended for lightweight real-time inference workloads

---

### 🧪 CI/CD Pipeline

Automated workflow ensures continuous integration and delivery.

- ✅ Unit testing: `pytest`
- 🧼 Code quality: `flake8`
- 🐳 Docker image build on commit
- 🧪 Staging environment integration tests

---

### 📈 Monitoring & Logging

Robust monitoring ensures real-time reliability, model quality, and early detection of issues.

- **🔍 Data Drift Detection** – `Evidently.ai`  
  Detects changes in feature distributions between training and live data.

- **📊 Model Performance Tracking** – `MLflow`  
  Logs metrics like accuracy, F1-score, and AUC. Supports experiment versioning and monitoring over time.

- **📈 Dashboards & Alerts** – `Prometheus` + `Grafana`  
  Real-time dashboards and alerts for latency, prediction volume, and performance thresholds.

- **🚨 Error Logging** – `Sentry`  
  Captures API/runtime exceptions and sends notifications.

---

### 🔁 Retraining

Automated retraining ensures the model stays accurate as new data becomes available.

- **📥 Data Ingestion** – Continuously log new patient records.
- **🔁 Scheduled Retraining** – Periodic model updates to adapt to recent trends.
- **⚙️ Orchestration** – Managed with `Apache Airflow` for scheduling and reproducibility.

---

## 🖥️ Interface for Medical Use

### Local Use:
- GUI built in `Streamlit`
- Loads model from serialized `joblib` or `ONNX` file
- Lightweight and interpretable output

### Cloud Use:
- Access via HTTPS-secured API endpoint
- Returns JSON with class + confidence scores
- Optimized for real-time response

---

![Design Diagram](https://github.com/user-attachments/assets/73fc7e1f-77b2-4212-895d-b044fe4aae1b)


