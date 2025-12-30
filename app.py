"""
Copilot Calculator Streamlit App

This app allows users to perform basic arithmetic operations on two numbers.
Streamlit automatically manages the state of input widgets, so values persist and update as users interact with the UI.
"""

import streamlit as st
from calculator_backend import add, subtract, multiply, divide

st.title("2 Digit Calculator")
st.header("2 Digit Calculator")
st.write("This is a simple calculator application.")

# Streamlit's number_input widgets automatically store and update their values in the app's state.
num1 = st.number_input("Enter first number", value=0.0, format="%f")
num2 = st.number_input("Enter second number", value=0.0, format="%f")

# The selectbox in the sidebar also maintains its state, reflecting the user's current selection.
operation = st.sidebar.selectbox(
    "Select operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Check for division by zero and display a warning if needed.
if operation == "Divide" and num2 == 0.0:
    st.warning("Cannot divide by zero. Please enter a non-zero second number.")

# When the calculate button is pressed
if st.button("Calculate"):
    result = None
    symbol = ""
    # Perform the calculation based on the selected operation
    try:
        if operation == "Add":
            result = add(num1, num2)
            symbol = "+"
        elif operation == "Subtract":
            result = subtract(num1, num2)
            symbol = "-"
        elif operation == "Multiply":
            result = multiply(num1, num2)
            symbol = "×"
        elif operation == "Divide":
            symbol = "÷"
            result = divide(num1, num2)
    except ValueError as e:
        st.error(str(e))

    # If the result is successfully calculated, display it
    if result is not None:
        # Show a Bootstrap-like success box
        st.success(f"{num1:g} {symbol} {num2:g} = {result:g}")
        # Also show a larger, prominent text below the button
        st.markdown(
            f"<div style='font-size:32px; font-weight:700; margin-top:10px;'>{num1:g} {symbol} {num2:g} = {result:g}</div>",
            unsafe_allow_html=True,
        )
