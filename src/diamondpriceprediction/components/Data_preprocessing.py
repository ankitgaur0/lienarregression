import os,sys
import numpy as np
import pandas as pd
from src.diamondpriceprediction.Logger import logging
from src.diamondpriceprediction.Exceptionhandle import CustomException
from src.diamondpriceprediction.components.Data_Injestion import DataIngestion
from dataclasses import dataclass
from pathlib import Path

# import from some sklearn library
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

# for utils
from src.diamondpriceprediction.utils.utils import save_object
#@dataclass it is treated as destructor in python
@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path=os.path.join("artifacts",'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_object=DataTransformationConfig()
    # get_data_transformation method is used to transform the data
    def get_data_trasnformation(self):
        
        try:
            # this is for transformation of data
            logging.info("data transformation is initated")
            numerical_columns=['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_columns=['cut', 'color', 'clarity']

            # now the unique entity of categorical_columns for performing encoding
            cut_category=['Ideal', 'Premium', 'Good', 'Very Good', 'Fair']
            color_category=['E', 'I', 'J', 'H', 'F', 'G', 'D']
            clarity_category=['SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF']

            logging.info("Pipeline initiated")
            #now we have to make the piple lines for performing process on numberical and categorical columns
            numerical_pipeline=Pipeline(
                    steps=[
                        ("imputee",SimpleImputer()),
                        ("scaling",StandardScaler())

                    ]
            )
            categorical_pipeline=Pipeline(
                    steps=[
                        ("imputer",SimpleImputer(strategy="most_frequent")),
                        ("encoder",OrdinalEncoder(categories=[cut_category,color_category,clarity_category])),
                        ("scaler",StandardScaler())
                     ]
            )
            # now define a transformation object 
            preprocessor=ColumnTransformer(
                    [
                        ("categorical",categorical_pipeline,categorical_columns),
                        ("numberical",numerical_pipeline,numerical_columns)
                    ]
                )
            
            return (preprocessor)

        except Exception as e:
            print("the Exception is occurs in the data_preproccor phase")
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data complete")
            # now i will log the head value of the train and test data frame in loggine
            logging.info(f"the head values of train dataframe is: \n{train_df.head().to_string()}")
            logging.info(f"the test dataframe head is: \n {test_df.head().to_string()}")
            
            # now we make a object of get_data_transformation() method
            preprocessor_obj=self.get_data_trasnformation()
            # before fit transform , we should segregate the target column and drop the unwanted column
            targeted_column='price'
            drop_columns=[targeted_column,'Unnamed: 0']
            input_feature_train_df=train_df.drop(drop_columns,axis=1)
            targeted_feature_train_df=train_df[targeted_column]

            input_feature_test_df=test_df.drop(drop_columns,axis=1)
            targeted_feature_test_df=test_df['price']

            # now fit and transform the train and test data
            input_feature_train_array=preprocessor_obj.fit_transform(input_feature_train_df)
            # for validate the model
            input_feature_test_array=preprocessor_obj.transform(input_feature_test_df)
            train_array=np.c_[input_feature_train_array,np.array(targeted_feature_train_df)]
            test_array=np.c_[input_feature_test_array,np.array(targeted_feature_test_df)]


            logging.info("appling preprocessing object on train and test input data")

            #now i save the object for further processing
            save_object(
                file_path=self.data_transformation_object.preprocessor_object_file_path,
                obj=preprocessor_obj
            )

            logging.info("processing pickle file saved")
            return (
                train_array,
                test_array
            )


        except Exception as e:
            print("the exception is occured in the transformation phase")

            raise CustomException(e,sys)