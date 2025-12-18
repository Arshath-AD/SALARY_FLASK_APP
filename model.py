import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

# 1. Load your Excel dataset
# CHANGE 'Salary_Data.xlsx' to your exact file name!
df = pd.read_csv('Salary_Data.xls') 


# 2. Separate Features (X) and Target (y)
# Ensure your Excel column headers match these names exactly:
X = df[['YearsExperience']] 
y = df['Salary']

# 3. Train the Model
regressor = LinearRegression()
regressor.fit(X, y)

# 4. Save the trained model
pickle.dump(regressor, open('model.pkl', 'wb'))

print("Success! Excel model trained and saved as 'model.pkl'")