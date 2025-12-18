import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# 1. Load the model you just trained
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get the "Years of Experience" from the HTML form
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    # 2. Make the prediction using the loaded model
    prediction = model.predict(final_features)
    
    # 3. Format the result (Round to 2 decimal places)
    output = round(prediction[0], 2)

    # 4. Send the result back to the HTML page
    return render_template('index.html', prediction_text='Predicted Salary: ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)