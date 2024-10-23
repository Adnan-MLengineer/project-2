"""
# **Importing the Dependencies**
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""# **Data Collection and Analysis**"""

# Loading the diabetes dataset to a pandas dataframe
diabetes_dataset = pd.read_csv('/content/diabetes.csv')

diabetes_dataset.head()

# Number of rows and columns in this datasets
diabetes_dataset.shape

# Getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""# **0 represents no diabetic patients and 1 represents diabetic patients**"""

diabetes_dataset.groupby('Outcome').mean()

# Separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

"""# **Data Standardization**"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X, Y)

"""# **Train Test Split**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

"""# **Training the Model**"""

classifier = svm.SVC(kernel = 'linear')

# Training the Support Vector Machine Classifier
classifier.fit(X_train, Y_train)

"""# **Model Evaluating: Accuracy score**"""

# Accuracy score on training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print(f'accuracy score of the training data: {training_data_accuracy}')

# Accuracy score on test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print(f'accuracy score of the test data: {test_data_accuracy}')

"""# **Making a Predective System**"""

input_data = (1,189,60,23,846,30.1,0.398,59)

# Changing input_data into a numpy_array
input_data_as_numpy_array = np.asarray(input_data)

# Reshaping the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

