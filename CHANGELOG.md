## 📂 CHANGELOG

### [2.0.0] - 2025-05-27

#### Added
- Local execution option with `Streamlit` GUI for medical staff
- Remote API deployment using `FastAPI` + `Uvicorn` on AWS EC2
- Secure API endpoint with authentication support (assumed)
- CI/CD pipeline automation using GitHub Actions for Docker build and testing
- Data quality validation with `great_expectations`
- Text normalization in preprocessing for clinical notes
- Containerized pipeline stages for reproducibility and portability
- Real-time prediction enforced as exclusive mode
- Prediction explanation via SHAP values exposed through API
- Monitoring additions:
  - Data drift detection using `Evidently.ai`
  - Model performance tracking via `MLflow`
  - Dashboards and alerts using `Prometheus` + `Grafana`
  - Error logging with `Sentry`
- Retraining orchestration and scheduling using `Apache Airflow`
- Added detailed CI/CD pipeline steps including linting and integration tests

#### Changed
- Expanded preprocessing techniques: categorical encoding (OneHot, Target Encoding), feature scaling (Z-score, MinMax)
- Model evaluation decoupled from training phase for better validation consistency
- Shifted deployment focus to containerized solutions supporting both local and remote use
- Enhanced prediction task definition to stress instant real-time inference to support clinical workflows

#### Fixed
- Addressed reproducibility issues by enforcing containerization
- Improved handling of missing data and noisy labels with added preprocessing robustness
- Streamlined deployment and monitoring workflows for better maintainability and scalability

---
