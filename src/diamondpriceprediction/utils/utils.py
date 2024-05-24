import numpy as np
import pandas as pd
import os,sys
import pickle
from src.diamondpriceprediction.Logger import logging
from src.diamondpriceprediction.Exceptionhandle import CustomException

from sklearn.metrics import mean_absolute_error , mean_squared_error,r2_score

def save_object(file_path,obj):
    try:
        file_path=os.path.dirname(file_path)

        os.makedirs(file_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info("Exception is occured in utils file")
        raise CustomException(e,sys)
    

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            #here fit in the model with the help of object
            model.fit(X_train,y_train)
            #now predict the output by giving X_test data
            y_predict=model.predict(X_test)

            #now get accuracy by r2_score
            test_model_score=r2_score(y_test,y_predict)

            report[list(models.key())[i]]=test_model_score

            return report


    except Exception as e:
        logging.info("Exception during the model training part/phase")
        raise CustomException(e,sys)
    

    def load_object(file_path):
        try:
            with open(file_path,"rb") as file_obj:
                return pickle.load(file_obj)

        except Exception as e:
            raise CustomException(e,sys)
