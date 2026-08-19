import numpy as np
from sklearn.linear_model import LinearRegression

# Training examples
# The rule is NOT directly given to the model.
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 6],
    [10, 20],
    [20, 10],
    [50, 20],
    [100, 50]
])

y = np.array([
    3,
    5,
    7,
    11,
    30,
    30,
    70,
    150
])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

# Test on numbers that were NOT in training data
test_data = np.array([
    [6, 8],
    [13, 9]
])

predictions = model.predict(test_data)

for numbers, prediction in zip(test_data, predictions):
    print(f"{numbers[0]} + {numbers[1]} = {round(prediction)}")