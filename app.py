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
        # Extract data from form
        monthly_debt = int(request.form['monthly_debt'])
        open_accounts = int(request.form['open_accounts'])
        credit_balance = int(request.form['credit_balance'])
        open_credit = int(request.form['open_credit'])
        
        # Create the feature array for prediction
        final_features = [np.array([monthly_debt, open_accounts, credit_balance, open_credit])]
        
        # Make prediction
        prediction = model.predict(final_features)
        output = 'Eligible' if prediction[0] == 1 else 'Not Eligible'

        # Return prediction as JSON
        return jsonify(prediction_text=f"Eligibility: {output}")
    except Exception as e:
        # Handle error and return message
        return jsonify(prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
