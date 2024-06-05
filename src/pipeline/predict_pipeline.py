# create predict pipeline class 
# create function to load a object
# crate custom class based on the object 
# create fn to convert data into dict 

import os
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from src.exception import CustmerExcepetion
from src.logger import logging
from src.utils import load_obj
from dataclasses import dataclass


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        preprocessor_path = "artifacts\preprcessor.pkl"
        model_path = "artifacts\model.pkl"

        preprocessor = load_obj(file_path = preprocessor_path)
        model = load_obj(file_path = model_path)

        scaled = preprocessor.transform(features)
        pred = model.predict(scaled)

        return pred
    
class CustomData:
    def __init__(self,
                 age:int,
                 workclass:str,
                 education_num:str,
                 marital_status:str,
                 occupation:str,
                 relationship:str,
                 race:str,
                 sex:str,
                 capital_gain:int,
                 capital_loss:int,
                 hours_per_week:int,
                 native_country:str):
        
        self.age = age
        self.workclass = workclass
        self.education_num = education_num
        self.martial_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week
        self.native_country = native_country


    def get_data_as_df(self):
        try:
            output_as_dict = {
                "age" : [self.age],
                "workclass": [self.workclass],
                "education_num": [self.education_num],
                "marital_status" : [self.martial_status],
                "occupation" : [self.occupation],
                "relationship":[self.relationship],
                "race":[self.race],
                "sex":[self.sex],
                "capital_gain":[self.capital_gain],
                "capital_loss":[self.capital_loss],
                "hours_per_week":[self.hours_per_week],
                "native_country":[self.native_country]
            }

            return pd.DataFrame(output_as_dict)
        
        except Exception as e:
            raise CustmerExcepetion(e, sys)


        