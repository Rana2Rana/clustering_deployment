
from flask import Flask, render_template, request
import os
import joblib
import numpy as np


app = Flask(__name__)
model = joblib.load(open('churn_main/KmeansModel.joblib', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data1  = request.form["Total_Trans_Amt"]
    data2 = request.form["Avg_Open_To_Buy"]
    data3 = request.form["Avg_Utilization_Ratio"]
    arr = np.array([[data1, data2, data3]])
    pred = model.predict(arr)
    output = pred[0]
    if output == 0:
        pimage = '\static\cluster0.jpg'
    elif output == 1:
        pimage = '\static\cluster1.jpg'
    elif output == 2:
        pimage = '\static\cluster2.jpg'
    else:
        pimage = '\static\cluster3.jpg'

    Prediction='This client belong to group number:  {} '.format(pred[0])
    char = 'This group has the following characteristics:'
    return render_template('result.html',pimage= pimage , Prediction= Prediction,char = char )
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)