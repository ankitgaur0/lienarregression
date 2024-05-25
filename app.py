from src.diamondpriceprediction.Pipeline.prediction_pipeline import Customdata,PredictPipeline

from flask import Flask,request,render_template,jsonify

app=Flask("__name__")

@app.route("/")
#here i will accosiated it with a method name(home_page)
def home_page():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict_datapoints():
    if request.method == "GET":
        return render_template("form.html")
    else:
        DATA=Customdata(
            carat=request.form.get('carat'),
            depth=request.form.get('depth'),
            table=request.form.get('table'),
            x=request.form.get('x'),
            y=request.form.get('y'),
            z=request.form.get('z'),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        df=DATA.get_data_dataframe()

        pred_obj=PredictPipeline()
        pred=pred_obj.predict(df)

        result=round(pred[0],2)

        return render_template("result.html",final_result=result)
        

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)