from flask import Flask, request, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load your trained model
with open('weather_model.pkl', 'rb') as file:
    model = pickle.load(file)



@app.route('/predict', methods=['POST'])
def predict():
    req_data = request.get_json()

    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'Temp_C': [req_data['Temp_C']],
        'Dew_Point_Temp_C': [req_data['Dew_Point_Temp_C']],
        'Rel_Hum': [req_data['Rel_Hum']],
        'Wind_Speed_km_h': [req_data['Wind_Speed_km_h']],
        'Visibility_km': [req_data['Visibility_km']],
        'Press_kPa': [req_data['Press_kPa']]
    })

    # Perform prediction
    prediction = model.predict(input_data)[0]

    

    # Return predicted weather label
    return jsonify({
        'predicted_weather_label': predicted_weather_label
    })

if __name__ == '__main__':
    app.run(debug=True)
