import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
import pandas as pd
import joblib  # Charger le modèle

# Charger le modèle pré-entrainé
model = joblib.load('./Laboratoire_python/monmodel.pkl')

def predict():
    try:
        # Récupérer les données entrées par l'utilisateur
        credit_score = float(entry_credit_score.get())
        gender = 0 if gender_var.get() == "Homme" else 1
        age = int(entry_age.get())
        tenure = int(entry_tenure.get())
        balance = float(entry_balance.get())
        num_of_products = int(entry_num_of_products.get())
        has_cr_card = 1 if has_cr_card_var.get() == "Oui" else 0
        is_active_member = 1 if is_active_member_var.get() == "Oui" else 0
        estimated_salary = float(entry_estimated_salary.get())
        
        # Récupérer le pays sélectionné
        france = 1 if country_var.get() == "France" else 0
        germany = 1 if country_var.get() == "Allemagne" else 0
        spain = 1 if country_var.get() == "Espagne" else 0
        
        # Créer un DataFrame avec les données de l'utilisateur
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
        
        # Afficher le résultat de la prédiction
        if prediction[0] == 1:
            result_label.config(text="Le client quittera la banque.")
        else:
            result_label.config(text="Le client ne quittera pas la banque.")
    
    except ValueError:
        # En cas d'erreur dans l'entrée (si ce n'est pas un nombre)
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides")

# Créer la fenêtre principale
window = tk.Tk()
window.title("Prédiction de départ client")

# Ajout des champs de saisie pour chaque variable
tk.Label(window, text="Credit Score:").pack()
entry_credit_score = tk.Entry(window)
entry_credit_score.pack()

# Liste déroulante pour le sexe
tk.Label(window, text="Genre:").pack()
gender_var = StringVar(window)
gender_var.set("Homme")  # Valeur par défaut
gender_menu = OptionMenu(window, gender_var, "Homme", "Femme")
gender_menu.pack()

tk.Label(window, text="Age:").pack()
entry_age = tk.Entry(window)
entry_age.pack()

tk.Label(window, text="Tenure:").pack()
entry_tenure = tk.Entry(window)
entry_tenure.pack()

tk.Label(window, text="Balance:").pack()
entry_balance = tk.Entry(window)
entry_balance.pack()

tk.Label(window, text="Nombre de produits (max 4):").pack()
entry_num_of_products = tk.Entry(window)
entry_num_of_products.pack()

# Liste déroulante pour la possession de carte de crédit
tk.Label(window, text="Possède une carte de crédit:").pack()
has_cr_card_var = StringVar(window)
has_cr_card_var.set("Oui")  # Valeur par défaut
has_cr_card_menu = OptionMenu(window, has_cr_card_var, "Oui", "Non")
has_cr_card_menu.pack()

# Liste déroulante pour le statut de membre actif
tk.Label(window, text="Membre actif:").pack()
is_active_member_var = StringVar(window)
is_active_member_var.set("Oui")  # Valeur par défaut
is_active_member_menu = OptionMenu(window, is_active_member_var, "Oui", "Non")
is_active_member_menu.pack()

tk.Label(window, text="Salaire estimé:").pack()
entry_estimated_salary = tk.Entry(window)
entry_estimated_salary.pack()

# Liste déroulante pour le pays
tk.Label(window, text="Pays:").pack()
country_var = StringVar(window)
country_var.set("France")  # Valeur par défaut
country_menu = OptionMenu(window, country_var, "France", "Allemagne", "Espagne")
country_menu.pack()

# Bouton pour faire la prédiction
predict_button = tk.Button(window, text="Prédire", command=predict)
predict_button.pack()

# Label pour afficher le résultat
result_label = tk.Label(window, text="Résultat de la prédiction: ")
result_label.pack()

# Démarrer la fenêtre
window.mainloop()
