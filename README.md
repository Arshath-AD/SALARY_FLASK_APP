# 💰 Salary Predictor AI

A Machine Learning web application that predicts an employee's estimated salary based on their years of experience.

## 🧠 Algorithm
* **Linear Regression:** Fits a straight line to the data to find the relationship between Experience and Salary.

## 📂 Project Structure
* **`model.py`:** The "Brain". Reads the data, trains the model, and saves it as `model.pkl`.
* **`app.py`:** The "Server". A Flask app that loads the model and handles web requests.
* **`templates/index.html`:** The "Frontend". A simple HTML interface for the user.
* **`Salary_Data.xls` (or .csv):** The dataset used for training.

## 🚀 How to Run
1.  **Install Requirements:**
    ```bash
    pip install pandas flask scikit-learn
    ```
2.  **Train the Model:**
    ```bash
    python model.py
    ```
    *(This creates the `model.pkl` file)*
3.  **Start the Web Server:**
    ```bash
    python app.py
    ```
4.  **Open in Browser:**
    Go to `http://127.0.0.1:5000`

## 📊 Dataset
Uses a simple dataset containing `YearsExperience` and `Salary`.