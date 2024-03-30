from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from ratZomato.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            TakesOnlineOrders=request.form.get('TakesOnlineOrders'),
            hastablebooking=request.form.get('hastablebooking'),
            Rest_Type=request.form.get('Rest_Type'),
            Votes=request.form.get('Votes'),
            Cuisines=request.form.get('Cuisines'),
            Cost=float(request.form.get('Cost')),
            Type=float(request.form.get('Type')),
            City=float(request.form.get('City'))
              
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)        
