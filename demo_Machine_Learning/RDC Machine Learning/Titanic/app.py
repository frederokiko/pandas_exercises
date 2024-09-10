from flask import Flask, render_template, request, redirect
import pandas as pd
from model.Classifier import Model

# instanciation of flask app
app = Flask(__name__)


@app.route('/')
def home():
    """
    home renders a page index.html on the created Flask server

    Returns:
        html: index page
    """
    return render_template("index.html", title="Titanic")


@app.route('/form', methods=['POST', 'GET'])
def form():
    """
    form renders a form page to retrieve users informations

    Returns:
        html: form page
    """
    if request.method == 'POST':

        print("Il ya requete")

        age = request.form["age"]
        sex = request.form["sex"]
        pclass = request.form["class"]

        # data={
        #     "age": age,
        #     "sex": sex,
        #     "pclass": pclass
        # }

        # df = pd.DataFrame(data, index=[0])
        print(sex, age, pclass)
        # print("Voici les resultats", Model.get_result(pclass, sex, age))
        resultats = Model.get_result(pclass, sex, age)

        return render_template("form.html", title="Results", result=resultats)

    else:
        print('verifie tes datas')
        return render_template("form.html", title="Form")


# Variable Environnment
if __name__ == "__main__":
    app.run(debug=True, port=3030)
