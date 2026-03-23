# Student Score Predictor
## Overview
This project is a basic machine learning application built using Python. It predicts a student's final exam score based on three factors:
a)  Hours studied  
b)  Attendance percentage  
c)  Previous exam score  
The goal is to understand how regression models work in a simple and practical scenario.
## How It Works
The project uses a Linear Regression model from scikit-learn.  
The model is trained on a small dataset and then used to predict scores for new inputs
## Project Structure
student-score-predictor

a)data                # Dataset file  
b) src                 # Source code (training and prediction)  
c) model               # Saved trained model  
d) requirements.txt     # Dependencies  
e) README.md            # Project documentation  
## Setup Instructions
### Step 1: Clone the repository
git clone https://github.com/your-username/student-score-predictor  
cd student-score-predictor  
### Step 2: Create a virtual environment
python -m venv venv  
Activate it:
Windows:
venv\Scripts\activate  
Linux/Mac:
source venv/bin/activate  
### Step 3: Install dependencies
pip install -r requirements.txt  
## Running the Project
### Train the model
python src/train.py  
This will train the model and save it in the `model` folder.
### Make a prediction
python src/predict.py 5 80 70  
Example output:
Predicted Final Score: 74.32  
## Technologies Used
a) Python  
b) pandas  
c) scikit-learn  
d) numpy  
e)joblib  
## Notes
a) This is a simple project meant for learning purposes.  
b) The dataset is small, so predictions are approximate.  
c) You can improve results by adding more data.

THANKS
Namrata kumari
SUBMISSION REQUIREMENTS  GitHub Repository  Your repository must be set to Public visibility before submission. Private repositories will not be accessible during evaluation and will result in rejection. Submit the repository root URL strictly in the following format: https://github.com/{github-username}/{repo-name} Do not submit a tree URL .
