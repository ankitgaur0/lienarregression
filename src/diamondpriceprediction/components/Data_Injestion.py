import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from src.diamondpriceprediction.Logger import logging
from src.diamondpriceprediction.Exceptionhandle import CustomException
from dataclasses import dataclass
from pathlib import Path
import os,sys


# there is two more term called as artifacts and configure .
# artifacts is the collections of outputs of different-different components(data_ingestion,data_preprocessing,model training).
#confi(configure) is the configuration regarding about the components.
class DataIngestionConfig:
    raw_data_path:str=os.path.join('artifacts','raw.csv')
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        # now here i have to make the object of the DataIngestionConfig class
        self.ingestion_config=DataIngestionConfig()
        # now by create the object i can use raw_data_pah,train,test_data_path


    def initiate_data_ingestion(self):
        logging.info("Now i started to inject the data")
        try:
            data=pd.read_csv(Path(os.path.join("notebook/data","diamonds.csv")))
            logging.info("i inject the data into data variable")

            # now i create a path for making directory for raw data and test and train data output (artifacts)
            os.makedirs(os.path.join(os.path.dirname(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("create a raw data file and store the raw data as artifacts")
            # we did not use artifacts folder name in os.path.join because self.ingestion_config.raw_data_path aleardy used it


            logging.info("now i split the data")
            train_data,test_data=train_test_split(data,test_size=0.30,random_state=42)

            logging.info("train test split is completed")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("i stored the train data and test data in the form of csv in artifacts folder")


            return (

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            print("error occurs during the data ingestion phase")
            raise CustomException(e,sys)