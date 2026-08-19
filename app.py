import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Machine Learns Addition",
    page_icon="🤖"
)

st.title("🤖 Teach a Machine to Add")

st.write(
    "The machine is trained using examples of numbers and their sums. "
    "The addition rule is not directly given to the model."
)

# Training data
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [5, 6],
    [10, 20],
    [20, 10],
    [50, 25],
    [100, 50]
])

y = np.array([
    3,
    5,
    7,
    11,
    30,
    30,
    75,
    150
])

# Train model
model = LinearRegression()
model.fit(X, y)

st.subheader("Training Examples")

st.write("The machine was given these examples:")

st.code("""
1 + 2 = 3
2 + 3 = 5
3 + 4 = 7
5 + 6 = 11
10 + 20 = 30
20 + 10 = 30
50 + 25 = 75
100 + 50 = 150
""")

st.subheader("Test the Machine")

col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input(
        "First number",
        value=6
    )

with col2:
    number2 = st.number_input(
        "Second number",
        value=8
    )

if st.button("Predict Sum"):

    input_data = np.array([[number1, number2]])

    prediction = model.predict(input_data)[0]

    st.success(
        f"Machine prediction: {round(prediction)}"
    )

    st.info(
        f"Actual sum: {number1 + number2}"
    )

