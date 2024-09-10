from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib  # Charger le modèle
import os

# Charger le modèle pré-entrainé
model = joblib.load('./Laboratoire_python/monmodel.pkl')

app = Flask(__name__)

# Chemin vers le dossier des captures d'écran
SCREENSHOTS_FOLDER = 'Laboratoire_python\static\screenshots'
screenshots = os.listdir(SCREENSHOTS_FOLDER)

# Variable pour garder la position de l'image actuelle
current_image_index = 0

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données du formulaire
        credit_score = float(request.form['credit_score'])
        gender = 0 if request.form['gender'] == "Homme" else 1
        age = int(request.form['age'])
        tenure = int(request.form['tenure'])
        balance = float(request.form['balance'])
        num_of_products = int(request.form['num_of_products'])
        has_cr_card = 1 if request.form['has_cr_card'] == "Oui" else 0
        is_active_member = 1 if request.form['is_active_member'] == "Oui" else 0
        estimated_salary = float(request.form['estimated_salary'])
        
        # Déterminer le pays
        country = request.form['country']
        france = 1 if country == "France" else 0
        germany = 1 if country == "Allemagne" else 0
        spain = 1 if country == "Espagne" else 0
        
        # Créer un DataFrame avec les données
        new_data = pd.DataFrame({
            'CreditScore': [credit_score],
            'Gender': [gender],
            'Age': [age],
            'Tenure': [tenure],
            'Balance': [balance],
            'NumOfProducts': [num_of_products],
            'HasCrCard': [has_cr_card],
            'IsActiveMember': [is_active_member],
            'EstimatedSalary': [estimated_salary],
            'France': [france],
            'Germany': [germany],
            'Spain': [spain]
        })
        
        # Faire la prédiction
        prediction = model.predict(new_data)
        result = "Le client quittera la banque." if prediction[0] == 1 else "Le client ne quittera pas la banque."

        return render_template('form.html', prediction_text=result)

    except ValueError:
        return render_template('form.html', prediction_text="Erreur: Veuillez entrer des valeurs valides.")

@app.route('/stats')
def stats():
    global current_image_index
    # Récupérer le nom de l'image actuelle
    current_image = screenshots[current_image_index]
    return render_template('stats.html', current_image=current_image)

@app.route('/next')
def next_image():
    global current_image_index
    # Passer à l'image suivante
    if current_image_index < len(screenshots) - 1:
        current_image_index += 1
    else:
        current_image_index = 0  # Revenir à la première image
    return redirect(url_for('stats'))

@app.route('/previous')
def previous_image():
    global current_image_index
    # Revenir à l'image précédente
    if current_image_index > 0:
        current_image_index -= 1
    else:
        current_image_index = len(screenshots) - 1  # Aller à la dernière image
    return redirect(url_for('stats'))

if __name__ == "__main__":
    app.run(debug=True)

