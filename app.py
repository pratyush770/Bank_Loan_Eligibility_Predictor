from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model/loan_eligibility_predictor_pickle'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        monthly_debt = int(data['monthly_debt'])
        open_accounts = int(data['open_accounts'])
        credit_balance = int(data['credit_balance'])
        open_credit = int(data['open_credit'])

        # Create the feature array for prediction
        final_features = [np.array([monthly_debt, open_accounts, credit_balance, open_credit])]

        # Make prediction
        prediction = model.predict(final_features)
        output = 'Congrats, you are eligible!' if prediction[0] == 1 else 'Sorry, you are not eligible!'

        # Return the prediction result as JSON
        return jsonify({'prediction': output})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
