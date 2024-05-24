import os,sys
import numpy as np
import pandas as pd
from src.diamondpriceprediction.components.Data_Injestion import DataIngestion
from src.diamondpriceprediction.components.Data_preprocessing import DataTransformation
from src.diamondpriceprediction.Exceptionhandle import CustomException
from src.diamondpriceprediction.utils.utils import evaluate_model
from src.diamondpriceprediction.utils.utils import save_object
from src.diamondpriceprediction.Logger import logging
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet

#from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


@dataclass
class ModeldataConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class Modeltrainer:
    def __init__(self):
        #now create a object of ModeldataConfig
        self.model_trainer_config=ModeldataConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info(" spliting the dependent and independent data from train and test array")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                "LinearRegression":LinearRegression(),
                "Ridge":Ridge(),
                "Lasso":Lasso(),
                "ElasticNet":ElasticNet()
            }
          
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print("\n","="*40,"\n")
            
            logging.info(f"the model_report is {model_report}")
            #best models score
            best_models_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_models_score )
            ]
            best_model=models[best_model_name]

            print(f"best model name :{best_model_name} \n best model score is {best_models_score}")
            print("\n","="*40,"\n")
            logging.info(f"best model name is :{best_model_name} \n best model score is{best_models_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                objects=best_model
            )


        except Exception as e:
            logging.info("the Exception is occured in model trainer part")
            raise CustomException(e,sys)
