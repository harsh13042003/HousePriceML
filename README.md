# House Price Prediction using Machine Learning

## About the Project
This project is a simple and practical implementation of a **Machine Learning regression model** to predict house prices.  
The idea behind this project is to understand how real-world data can be used to make predictions based on meaningful features.

The model predicts the **price of a house** using factors such as:
- area of the house
- number of bedrooms
- age of the house

This project was developed as a **self-learning and academic project** to strengthen core concepts of Machine Learning and data handling.

---

## Problem Statement
House prices depend on multiple factors and estimating them manually is not always accurate.  
The goal of this project is to build a model that can **learn patterns from historical data** and predict house prices efficiently using Machine Learning.

---

## Approach Used
- Supervised Machine Learning
- Regression-based model
- Linear Regression algorithm
- Train-test split for evaluation

The model is trained on historical data and tested on unseen data to measure its performance.

---

## Dataset Information
The dataset is stored in a CSV file and contains structured housing data.

### Input Features:
- `area` – Total area of the house
- `bedrooms` – Number of bedrooms
- `age` – Age of the house in years

### Output:
- `price` – Price of the house (in Lakhs)

---

## Project Workflow
1. Load the dataset using Pandas
2. Explore and understand the data structure
3. Separate features and target variable
4. Split data into training and testing sets
5. Train the Linear Regression model
6. Evaluate model performance using R² score
7. Predict house prices for new inputs

---

## Model Evaluation
The model performance is evaluated using the **R² Score**, which indicates how well the model explains the variance in house prices.

A higher R² score shows that the model fits the data well.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Visual Studio Code
- Git & GitHub

---

## How to Run the Project

Step 1: Clone the repository:
```bash
git clone https://github.com/harsh13042003/HousePriceML.git

Step 2: Navigate to the Project Folder
cd HousePriceML

Step 3: Create a Virtual Environment (Optional but Recommended)
python -m venv venv

Step 4: Install Required Libraries
pip install pandas numpy scikit-learn

Step 5: Verify Dataset
Make sure the file house_data.csv is present in the project root directory.

Step 6: Run the Python Script
python house_price_ml.py

Step 7: Provide Input
Enter the required values when prompted:
Area of the house
Number of bedrooms
Age of the house
The program will process the input and predict the house price.


Step 8: View Output
The predicted house price will be displayed in Lakhs on the terminal screen.

Example: Predicted House Price: 52.30 Lakh Rupees
