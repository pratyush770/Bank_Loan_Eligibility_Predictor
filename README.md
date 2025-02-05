## LoanCheck
**LoanCheck** is a web-based application designed to help individuals assess their eligibility for a bank loan based on key financial factors. By inputting data such as monthly debt, the number of open accounts, credit balance, and open credit, users can quickly receive an eligibility prediction, which can assist them in making informed financial decisions.
## What the Project Does
This project allows users to:
- Enter key financial details such as monthly debt, open accounts, credit balance, and open credit.
  
- Get an instant prediction about their eligibility for a bank loan based on the provided data.
- Make use of an intuitive and user-friendly interface to input data and receive predictions.
## Technologies Used
- **Frontend**
  - **HTML5, CSS3** (for styling and layout)
  
  - **Bootstrap 5** (for responsive design and components)
  - **JavaScript** (for handling form submissions and dynamic interactions)
  - **jQuery** (for AJAX requests and form data handling)
  
- **Backend**
  - **Python** (for implementing the machine learning model and prediction logic)
  
  - **Flask** (for building the web application and handling requests)
  
- **Machine Learning**
  - The project uses a **machine learning model** (trained on historical data) to predict loan eligibility based on user input.
  
## Key Features
  - **Responsive Design**: The application is designed to be fully responsive, ensuring a smooth user experience across all devices.
  
  - **Real-Time Prediction**: Users receive instant feedback on their loan eligibility based on the input provided.
  - **User-Friendly Interface**: The form is easy to navigate, making it accessible even for users with minimal technical knowledge.
## How to Deploy
- Clone the repository by the following command: `git clone https://github.com/pratyush770/Bank_Loan_Eligibility_Predictor.git`
  
- Create a **virtual environment** (venv) first and install all the packages using `pip install requirements.txt`.
- Create a github repository and make sure to add your venv in **.gitignore** since it contains all dependencies and can be quite large.
- Create your **Render** account by visiting the following link: https://dashboard.render.com
- Click on **New** button on the top right and then select **Web service**.
- Select your **created repository, branch, instance type** and give **name** to your website. Keep other things as it is.
- Click on the **Deploy Web Service** button and you're done!
## Deployment
This project is deployed on **Render** and can be accessed via the following link:

[Website] https://bank-loan-eligibility-predictor.onrender.com
