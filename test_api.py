import requests

# HTML
r = requests.post("http://127.0.0.1:5002/predict", {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100})

# API
for dic in [
    
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100},
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100},
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100},
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100},
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100},
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100},
    {"Total_Trans_Amt": 1000, "Avg_Open_To_Buy":100, "Avg_Utilization_Ratio":100}
]:
    r = requests.post("http://127.0.0.1:5002/api/predict", dic)
    print(r.text)
    
# Healthcheck
r = requests.get("http://127.0.0.1:5002/healthcheck", dic)
