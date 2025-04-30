# 🩺 Medical Diagnosis ML Challenge

## 📚 Background

In modern medicine, technological advances have led to a vast amount of available patient information. While this abundance is beneficial for **common diseases**, **rare diseases (orphan diseases)** suffer from a lack of data, making it difficult to train effective machine learning models.

The objective of this project is to build a system that predicts the **likelihood of a patient suffering from a disease** based on their symptoms and demographic information. The model should perform well for both common and rare diseases, despite the challenges posed by class imbalance and limited data.

---

## 🧠 Problem Definition

### 🏗️ Model Training

The model is trained offline by a machine learning engineer or data science team.

The dataset consists of clinical records with features such as:
- Patient symptoms
- Demographic data (e.g., age, sex, family history)
- Historical medical information

Each file (representing a patient or patient group) must be:
- Cleaned and preprocessed
- Enriched with engineered features
  - Based on the patient row
  - Aggregates across the dataset
  - External medical knowledge sources

Model selection and evaluation are conducted separately to ensure consistency and comparability. Once a model meets defined quality standards, it is approved for deployment.

---

### 🔍 Prediction Task

On a daily basis, new patient data is ingested. The system must process this data and **generate predictions for each patient** in real-time or in batch, ensuring quick and reliable feedback for healthcare professionals.

The model is integrated into a larger health platform and should complete predictions in a limited time window.

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
- **Public APIs** such as NIH, Orphanet, and MIMIC-III
- **CSVs and relational databases**
- **Cloud storage & version control** (e.g., Amazon S3, Redshift, DVC)

### 🧹 Preprocessing

Before model training, data undergoes several preprocessing steps:
- Handling **missing values**
- **Normalizing** numerical features
- **Encoding** categorical variables

Tools used: `pandas`, `NumPy`, `scikit-learn`

### 🧠 Type of Models

A variety of models are explored, including:
- **Tree-based models**: Random Forest, XGBoost
- **Deep Learning**: CNNs, RNNs or Transformer-based models
- **Bayesian and probabilistic models**

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

In the production phase, the trained models are deployed to serve predictions in real-time or batch systems. This stage also includes monitoring and retraining pipelines to ensure long-term model reliability.

### 📦 Deployment

Models are deployed using container-based and serverless infrastructure:
- **Expose the model** through APIs or endpoints
- **Use containers** for portability and scalability

Technologies:
- `Docker`
- `AWS Lambda`

### 📊 Monitoring

To maintain model performance in real-world settings:
- **Monitor data drift**
- **Track model performance** over time
- **Set up alerts** for anomalies or degradation

Tools used:
- `Neptune.ai`
- `Prometheus` + `Grafana`

### 🔁 Retraining

As new data is generated, retraining is automated to keep models updated:
- **Continuously store new patient data**
- **Automate periodic retraining**

Orchestration with: `Apache Airflow`

![Design Diagram](https://github.com/user-attachments/assets/73fc7e1f-77b2-4212-895d-b044fe4aae1b)


