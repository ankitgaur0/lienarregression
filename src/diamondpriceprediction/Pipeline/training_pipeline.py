from src.diamondpriceprediction.components.Data_Injestion import DataIngestion
from src.diamondpriceprediction.components.Data_preprocessing import DataTransformation
from src.diamondpriceprediction.components.Model_traning import Modeltrainer
from src.diamondpriceprediction.Logger import logging
from src.diamondpriceprediction.Exceptionhandle import CustomException

import numpy as np
import pandas as pd

data_ingestion_obj=DataIngestion()

train_data_path,test_data_path=data_ingestion_obj.initiate_data_ingestion()
# now create a object for transformation and provide the output of ingestion module
data_trasformation_object=DataTransformation()

train_array,test_array=data_trasformation_object.initiate_data_transformation(train_data_path,test_data_path)


#now create a objec to model_training module and provide the output of data_preprocessing module
data_modeltrainer_object=Modeltrainer()

data_modeltrainer_object.initiate_model_training(train_array,test_array)