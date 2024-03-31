from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from ratZomato.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/home')
def index():
    return render_template('home.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('predict.html')
    else:
        data=CustomData(
            TakesOnlineOrders=int(request.form.get('TakesOnlineOrders')),
            hastablebooking=int(request.form.get('hastablebooking')),
            Rest_Type=int(request.form.get('Rest_Type')),
            Votes=int(request.form.get('Votes')),
            Cuisines=int(request.form.get('Cuisines')),
            Cost=float(request.form.get('Cost')),
            Type=float(request.form.get('Type')),
            City=int(request.form.get('City'))
              
        )
        pred_df=data.get_data_as_dataframe()
        print(pred_df)
        print("Before Prediction")
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=np.round(predict_pipeline.predict(pred_df),2)
        print("after Prediction")
        return render_template('predict.html',results=results[0])
    

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)        
