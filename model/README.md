
# Medical Diagnostic API – Dockerized Service

This project provides a lightweight and portable API service that allows a physician to submit three patient values (representing symptoms or measurements) and receive a simulated diagnostic result. The service is packaged in a Docker container for easy deployment on any system, without requiring model training.

## 🔍 Purpose

To simulate a medical diagnostic system capable of returning one of the following outcomes based on a combination of three input values:

- `NO ENFERMO` (Not Sick)  
- `ENFERMEDAD LEVE` (Mild Disease)  
- `ENFERMEDAD AGUDA` (Acute Disease)  
- `ENFERMEDAD CRÓNICA` (Chronic Disease)

## 🚀 How It Works

- A simple classification model (`LogisticRegression`) is trained on startup using simulated data.
- The model is exposed via a Flask REST API.
- You provide three numerical inputs, and the model returns one of the four states.

## 🧱 Project Structure

```
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## ⚙️ Prerequisites

- Docker installed

## 🛠️ Build the Docker Image

```bash
docker build -t medical-diagnostic-api .
```

## 🧪 Run the Service

```bash
docker run -d -p 5000:5000 medical-diagnostic-api
```

## 📡 Make a Prediction

```bash
curl -X POST http://localhost:5000 \
     -H "Content-Type: application/json" \
     -d '{"age": 3, "medical_visits_frequency": 4, "physical_activity_level": 2}'
```

Response:

```json
{
  "estado": "ENFERMEDAD LEVE"
}
```

## 🧼 Stop the Container

```bash
docker ps
docker stop <container_id>
```
