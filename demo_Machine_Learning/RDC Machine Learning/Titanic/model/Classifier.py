import pandas as pd
import joblib
import numpy as np
# import os

# print("======================================>", os.getcwd())

model = joblib.load('./Titanic/model/best_model.pkl')


class Model():

    def get_result(pclass, sex, age):
        '''
        returns probability
        '''
        x = np.array([pclass, sex, age]).reshape(1, 3)
        proba = model.predict_proba(x)

        if model.predict(x) == 0:
            print(f'tu n\'a pas survecu {proba}')
            return 'tu n\'a pas survecu'
        else:
            print(f' weeee t\'es en vie hourra {proba}')
            return ' weeee t\'es en vie hourra'


# if __name__ == "__main__":
#     pass
