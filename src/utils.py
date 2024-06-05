import os
import sys
from src.logger import logging
from src.exception import CustmerExcepetion

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score , confusion_matrix ,f1_score

sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")

import pickle

def save_obj(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path , exist_ok=True)

        with open(file_path , "wb") as file_obj:
            pickle.dump(obj , file_obj)

    except Exception as e:
        raise CustmerExcepetion(e, sys)

def evaluate_model(x_train , y_train , x_test , y_test,models , params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]


            gs = GridSearchCV(model, param , cv=5)
            gs.fit(x_train , y_train)
            
            model.set_params(**gs.best_params_)
            model.fit(x_train , y_train) 
            # model. sav

            # make prediction 
            y_pred = model.predict(x_test)
            score = accuracy_score(y_test , y_pred)
            print(score)

            # report[list(model.values())[i]] = score
            report[list(models.values())[i]] = score

            return report

    except Exception as e:
        raise CustmerExcepetion(e,sys)
    
def load_obj(file_path):
    try:
        with open(file_path , "rb") as file_obj:
            return pickle.load(file_obj)
            
    except Exception as e:
        raise CustmerExcepetion(e,sys)
