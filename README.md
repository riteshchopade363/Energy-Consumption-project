Energy Consumption Prediction is a Machine Learning project based on Linear Regression that estimates energy usage in buildings. 
It uses factors like temperature, humidity, occupancy, and appliance usage (HVAC, lighting, renewable energy) to predict consumption.
The project helps in analyzing energy patterns and improving efficiency through data-driven insights.

Project Workflow (Step-by-Step)
Step 1: Data Collection
Dataset includes temperature, humidity, occupancy, HVAC usage, lighting, etc.

Step 2: Data Preprocessing
Handle missing values
Convert categorical values into numeric (encoding)
Normalize and clean data

Step 3: Model Training
Apply Linear Regression
Train model using input features
Evaluate accuracy

Step 4: Save Model
import pickle
pickle.dump(model, open('trained_model.pkl', 'wb'))

Web Application Flow
Step 5: Run the Application
python flask_app.py

Open in browser:
http://127.0.0.1:5000/

Step 6: Fill the Form
Enter the following details:
Temperature
Humidity
Square Footage
Occupancy
HVAC Usage (ON/OFF)
Lighting Usage (ON/OFF)
Renewable Energy (Yes/No)
Day of Week
Holiday

<img width="1899" height="867" alt="Screenshot 2026-04-05 172636" src="https://github.com/user-attachments/assets/006e2b06-e51d-4f5a-9932-12a5a3de1190" />

Step 7: Submit the Form:
Click on Submit Button

Step 8: Prediction Process:
Data is sent to Flask backend
Input is converted into numeric format
Model processes the input
Linear Regression predicts energy consumption
<img width="1915" height="863" alt="Screenshot 2026-04-05 172716" src="https://github.com/user-attachments/assets/239f7ae9-6eda-40b5-996c-96001c5b5a7f" />
Step 9: View Result
⚡ Predicted Energy Consumption is displayed
Output shown on result page

