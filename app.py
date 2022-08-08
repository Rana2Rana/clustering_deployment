
from flask import Flask, render_template, request, jsonify
import os
import joblib
import numpy as np


app = Flask(__name__)
model = joblib.load(open('churn_main/KmeansModel.joblib', 'rb'))

def predict_cluster(data):
    data1  = data["Total_Trans_Amt"]
    data2 = data["Avg_Open_To_Buy"]
    data3 = data["Avg_Utilization_Ratio"]
    arr = np.array([[data1, data2, data3]])
    pred = model.predict(arr)
    output = pred[0]
    return output

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/healthcheck', methods=["GET"])
def healthcheck():
    return "API is alive"

@app.route('/api/predict', methods=['POST'])
def predict_api():
    output = predict_cluster(request.form)
    return jsonify({
        "cluster_id": str(output)
    })
    

@app.route('/predict', methods=['POST'])
def predict():
    output = predict_cluster(request.form)
    if output == 0:
        pimage = '\static\cluster0.jpg'
    elif output == 1:
        pimage = '\static\cluster1.jpg'
    elif output == 2:
        pimage = '\static\cluster2.jpg'
    else:
        pimage = '\static\cluster3.jpg'

    Prediction='This client belong to group number:  {} '.format(output)
    char = 'This group has the following characteristics:'
    return render_template('result.html', pimage=pimage , Prediction=Prediction, char=char )
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5002))
    app.run(host="0.0.0.0", threaded=True, port=port, debug=True)