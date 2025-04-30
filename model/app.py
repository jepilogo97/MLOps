from flask import Flask, request, jsonify, render_template_string
import numpy as np
import joblib
import os
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix

app = Flask(__name__)

# Entrenamiento simulado del modelo con lógica mejorada
def train_model():
    np.random.seed(42)
    X = np.random.rand(200, 3) * 10  # Genera datos aleatorios
    y = []
    for row in X:
        age, visits, activity = row
        # Clasificación de enfermedades considerando más variabilidad
        if age > 70:
            if visits < 2 or activity < 1.5:
                y.append(3)  # ENFERMEDAD CRÓNICA
            elif visits < 4 or activity < 3:
                y.append(2)  # ENFERMEDAD AGUDA
            else:
                y.append(1)  # ENFERMEDAD LEVE
        elif age > 50:
            if visits < 3 or activity < 2:
                y.append(2)  # ENFERMEDAD AGUDA
            elif visits < 5 or activity < 4:
                y.append(1)  # ENFERMEDAD LEVE
            else:
                y.append(0)  # NO ENFERMO
        elif age > 30:
            if activity < 3:
                y.append(1)  # ENFERMEDAD LEVE
            elif visits < 4 or activity < 5:
                y.append(2)  # ENFERMEDAD AGUDA
            else:
                y.append(0)  # NO ENFERMO
        else:
            if activity < 3:
                y.append(1)  # ENFERMEDAD LEVE
            elif visits < 2 or activity < 4:
                y.append(2)  # ENFERMEDAD AGUDA
            else:
                y.append(0)  # NO ENFERMO

    y = np.array(y)
    
    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Definir el pipeline del modelo
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(multi_class='multinomial', solver='lbfgs'))
    ])

    # Realizar Grid Search para optimizar el modelo
    param_grid = {
        'clf__C': [0.01, 0.1, 1, 10, 100],
        'clf__max_iter': [100, 200, 300]
    }
    grid_search = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    # Guardar el modelo entrenado
    joblib.dump(best_model, 'model.pkl')

    # Evaluar el modelo en el conjunto de prueba
    y_pred_test = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_test)
    print(f"Precisión en conjunto de prueba: {accuracy:.4f}")

    return best_model

# Cargar o entrenar modelo
if os.path.exists('model.pkl'):
    model = joblib.load('model.pkl')
else:
    model = train_model()

labels = {
    0: "NO ENFERMO",
    1: "ENFERMEDAD LEVE",
    2: "ENFERMEDAD AGUDA",
    3: "ENFERMEDAD CRÓNICA"
}

# Ruta API JSON
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        s1 = float(data['age'])
        s2 = float(data['medical_visits_frequency'])
        s3 = float(data['physical_activity_level'])
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Please provide three numeric values: age, medical_visits_frequency, physical_activity_level"}), 400
    input_data = np.array([[s1, s2, s3]])
    prediction = model.predict(input_data)[0]
    estado = labels.get(prediction, "DESCONOCIDO")
    return jsonify({"estado": estado})

# Página web con formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    estado = ""
    error_message = ""
    if request.method == 'POST':
        try:
            s1 = float(request.form['age'])
            s2 = float(request.form['medical_visits_frequency'])
            s3 = float(request.form['physical_activity_level'])
            input_data = np.array([[s1, s2, s3]])
            prediction = model.predict(input_data)[0]
            estado = labels.get(prediction, "DESCONOCIDO")
        except Exception as e:
            error_message = f"Error: {e}"

    return render_template_string("""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Diagnóstico Médico</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container mt-5">
                <h2>Diagnóstico Médico</h2>
                <form method="post" class="mt-3">
                    <div class="mb-3">
                        <label for="age" class="form-label">Edad</label>
                        <input type="text" class="form-control" id="age" name="age" required>
                    </div>
                    <div class="mb-3">
                        <label for="medical_visits_frequency" class="form-label">Frecuencia de Visitas Médicas</label>
                        <input type="text" class="form-control" id="medical_visits_frequency" name="medical_visits_frequency" required>
                    </div>
                    <div class="mb-3">
                        <label for="physical_activity_level" class="form-label">Nivel de Actividad Física</label>
                        <input type="text" class="form-control" id="physical_activity_level" name="physical_activity_level" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Diagnosticar</button>
                </form>
                
                {% if estado %}
                    <div class="mt-4 alert alert-success">
                        <h3>Resultado: {{ estado }}</h3>
                    </div>
                {% endif %}
                {% if error_message %}
                    <div class="mt-4 alert alert-danger">
                        <h3>{{ error_message }}</h3>
                    </div>
                {% endif %}
            </div>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
    """, estado=estado, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
