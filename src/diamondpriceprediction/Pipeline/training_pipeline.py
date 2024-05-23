from src.diamondpriceprediction.components.Data_Injestion import DataIngestion

from src.diamondpriceprediction.Logger import logging
from src.diamondpriceprediction.Exceptionhandle import CustomException

import numpy as np
import pandas as pd

object=DataIngestion()

object.initiate_data_ingestion()