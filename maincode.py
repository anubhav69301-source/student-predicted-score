import pandas as pd
import numpy as np
import sys
import os
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
# LOAD DATA
def load_data(path):
    data = pd.read_csv(path)
    return data
# SPLIT DATA
def split_data(data):
    X = data[['hours_studied', 'attendance', 'previous_score']]
    y = data['final_score']
    return X, y
# TRAIN MODEL
def train_model():
    data = load_data('data/student_data.csv')
    X, y = split_data(data)

    X_train, X_test, y_train, y_test = train_test_split(  X, y, test_size=0.2, random_state=42)
  model = LinearRegression()
  model.fit(X_train, y_train)
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)
print("Model trained successfully!")
print(f"Mean Absolute Error: {error:.2f}")
 os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/model.pkl')
print("Model saved at model/model.pkl")
# PREDICT
def predict():
    if len(sys.argv) != 4:
        print("Usage:")
        print("Train: python main.py train")
        print("Predict: python main.py <hours> <attendance> <previous_score>")
        sys.exit(1)

    model = joblib.load('model/model.pkl')

    hours = float(sys.argv[1])
    attendance = float(sys.argv[2])
    previous_score = float(sys.argv[3])

    input_data = np.array([[hours, attendance, previous_score]])
    prediction = model.predict(input_data)

    print(f"Predicted Final Score: {prediction[0]:.2f}")
# MAIN LOGIC
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "train":
        train_model()
    else:
        predict()

