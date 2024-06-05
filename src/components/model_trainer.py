import os
import sys
import pandas as pd
import numpy as np

sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")

from src.logger import logging
from src.exception import CustmerExcepetion
from src.utils import save_obj , evaluate_model

from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    train_model_file_path = os.path.join("artifacts/", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self , train_arr , test_arr):
        try:
            logging.info("Model Training Started")
            x_train , y_train , x_test , y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            
            logging.info("Initiate ML Models") 

            models = {
                "random_forest": RandomForestClassifier(),
                "descion_tree":DecisionTreeClassifier(),
                "logistic":LogisticRegression()
            }

            logging.info("Hyper Para-meter-Tuning")

            params = {
                "random_forest":{
                    "class_weight":["balanced"],
                    'n_estimators': [20, 50, 30],
                    'max_depth': [10, 8, 5],
                    'min_samples_split': [2, 5, 10],
                },
                "descion_tree":{
                    "class_weight":["balanced"],
                    "criterion":['gini',"entropy","log_loss"],
                    "splitter":['best','random'],
                    "max_depth":[3,4,5,6],
                    "min_samples_split":[2,3,4,5],
                    "min_samples_leaf":[1,2,3],
                    "max_features":["auto","sqrt","log2"]
                },
                "logistic":{
                    "class_weight":["balanced"],
                    'penalty': ['l1', 'l2'],
                    'C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'solver': ['liblinear', 'saga']
                }
            }

            logging.info("Model Evaluating")

            model_report:dict = evaluate_model(x_train=x_train , y_train=y_train , x_test=x_test , 
                           y_test=y_test , models=models , params=params)
            
            # to get the best model 
            best_model_score = max(sorted(model_report.values()))

            # to get best model name 
            best_model_name = list(models.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            logging.info(f"Best model name {best_model_name} accuracy score is {best_model_score}")

            logging.info("Model Training completed successfully...")
            save_obj(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
                )


        except Exception as e:
            raise CustmerExcepetion(e,sys)
