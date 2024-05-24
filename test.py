from src.diamondpriceprediction.Pipeline.prediction_pipeline import Customdata
from src.diamondpriceprediction.Pipeline.prediction_pipeline import PredictPipeline 

customdata_obj=Customdata(0.23,"Ideal","E","SI2",61.5,55,3.95,3.98,2.43)
data=customdata_obj.get_data_dataframe()

print(data)

predict=PredictPipeline()
y_predict=predict.predict(data)
print(y_predict)