import os
import sys

sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")

from src.exception import CustmerExcepetion
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    obj = DataIngestion()
    train_data , test_data = obj.inititate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr , test_arr , _= data_transformation.inititate_data_transformation(train_data , test_data)
    
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr , test_arr)

    