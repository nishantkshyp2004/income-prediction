import os 
import sys
sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")
import pandas as pd
import numpy as np

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustmerExcepetion

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransfromartionConfigs

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_file_path = os.path.join("artifacts", "train.csv")
    test_file_path = os.path.join("artifacts", "test.csv")
    raw_file_path = os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def inititate_data_ingestion(self):
        logging.info("Data ingestion Started!")
        try:
            # reading the data
            data = pd.read_csv(os.path.join("notebook/", "income_cleandata.csv"))
            logging.info("Successfully read the data")
            
            # making dir
            os.makedirs(os.path.dirname(self.ingestion_config.raw_file_path), exist_ok=True)
            logging.info("Making folder...")

            # saving the csv file
            data.to_csv(self.ingestion_config.raw_file_path, index=False)
            logging.info("successfully save the data")
            
            # splitting into train and test 
            train_set , test_set = train_test_split(data , test_size=0.2, random_state=42)
            logging.info("Successfully splitted data into train and split")

            # saving into artifacts folder
            train_set.to_csv(self.ingestion_config.train_file_path , index= False , header=True)
            test_set.to_csv(self.ingestion_config.test_file_path , index=False , header = True)

            logging.info("Data ingested successfully")
            return(
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path
            )

        except Exception as e:
            logging.info("Error occured in file name")
            raise CustmerExcepetion(e, sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data , test_data = obj.inititate_data_ingestion()
        

    data_transformation = DataTransformation()
    train_arr , test_arr , _= data_transformation.inititate_data_transformation(train_data , test_data)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr , test_arr)
    # completed