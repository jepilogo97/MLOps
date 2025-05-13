# 🩺 Medical Diagnostic API – Dockerized Service

This project provides a lightweight and portable API service that allows a physician to submit three patient values (representing symptoms or measurements) and receive a simulated diagnostic result. The service is packaged in a Docker container for easy deployment on any system, without requiring prior model training.

---

## 🎯 Purpose

To simulate a medical diagnostic system capable of returning one of the following outcomes based on a combination of three numerical input values:

- `NO ENFERMO` (Not Sick)  
- `ENFERMEDAD LEVE` (Mild Disease)  
- `ENFERMEDAD AGUDA` (Acute Disease)  
- `ENFERMEDAD CRÓNICA` (Chronic Disease)

---

## 🚀 How It Works

- On startup, a `LogisticRegression` model is trained using synthetic data.
- The model is exposed via a `Flask` REST API.
- Users can:
  - **Send a POST request to the API** endpoint with three values.
  - **Access the web interface in a browser** and manually enter the input values.

---

## 🧱 Project Structure

```
├── app.py                 # Flask API with web and REST interface
├── Dockerfile             # Container setup
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## ⚙️ Prerequisites

- Docker installed

---

## 🛠️ Build the Docker Image

```bash
docker build -t medical-diagnostic-api .
```

---

## ▶️ Run the Service

```bash
docker run -d -p 5000:5000 medical-diagnostic-api
```

Once running, open your browser and go to:

```
http://localhost:5000
```

You will see a simple web form to input the three required values and receive a prediction.

---

## 📡 Make a Prediction via cURL

If you prefer using the REST API instead of the browser:

```bash
curl -X POST http://localhost:5000/predict      -H "Content-Type: application/json"      -d '{"age": 3, "medical_visits_frequency": 4, "physical_activity_level": 2}'
```

Expected response:

```json
{
  "estado": "ENFERMEDAD LEVE"
}
```

> 🔎 **Note:** Make sure to send the POST request to `/predict`. The root endpoint (`/`) only serves the HTML form.

---

## 🧼 Stop the Container

```bash
docker ps          # Find the container ID
docker stop <container_id>
```

---

## 📝 Notes

- The API supports both **form-based** and **JSON-based** interaction.