import os,sys
import pandas as pd
import numpy as np
from src.diamondpriceprediction.Exceptionhandle import CustomException
from src.diamondpriceprediction.Logger import logging
from src.diamondpriceprediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            modeltrainer_path=os.path.join("artifacts","model.pkl")

            preprocessor_obj=load_object(preprocessor_path)
            modeltrainer_obj=load_object(modeltrainer_path)

            scaled_data=preprocessor_obj.transform(features)

            pred=modeltrainer_obj.predict(scaled_data)
            return pred

        except Exception as e:
            raise CustomException(e,sys)
        

class Customdata:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        self.carat=carat
        self.cut=cut
        self.color=color
        self.clarity=clarity
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z

    def get_data_dataframe(self):
        try:
            custom_data_input_dirt={
                "carat":[self.carat],
                "depth":[self.depth],
                "table":[self.table],
                "x":[self.x],
                "y":[self.y],
                "z":[self.z],
                "cut":[self.cut],
                "color":[self.color],
                "clarity":[self.clarity],
            }

            custom_dataframe=pd.DataFrame(custom_data_input_dirt)
            logging.info("custom data dataframe is created")

            return custom_dataframe


        except Exception as e:
            raise CustomException(e,sys)
    

