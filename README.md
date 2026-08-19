# Week 1 - Teach a Machine to Add

## Problem

The goal was to teach a machine to add numbers using examples.

The addition rule was not directly given to the machine.

## How it works

I gave the model different pairs of numbers and their sums.

For example:

1 + 2 = 3
2 + 3 = 5
5 + 6 = 11
10 + 20 = 30

I used Linear Regression to learn the relationship between the input numbers and the output.

## Testing

After training, I tested the model with numbers that were not present in the training data.

Examples:

6 + 8 = 14

13 + 9 = 22

The model was able to predict the sums correctly.

## What broke on the way

My first attempt used very few and similar training examples, so the model was not reliable for new combinations.

I improved it by adding more varied training examples.

## Technologies Used

- Python
- NumPy
- Scikit-learn
- Streamlit
- Linear Regression
