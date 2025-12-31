"""
Copilot Calculator Streamlit App

This app allows users to perform basic arithmetic operations on two numbers.
Streamlit automatically manages the state of input widgets, so values persist and update as users interact with the UI.
"""

import streamlit as st
from calculator_backend import add, subtract, multiply, divide

# Set a playful background color and font
st.markdown(
    """
    <style>
    .main {
        background-color: #FFFBCC;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    }
    .stButton>button {
        background-color: #FFB347;
        color: white;
        font-size: 72px;
        border-radius: 16px;
        height: 1.125em;
        width: 100%;
        margin: 8px 0;
    }
    .equation-box {
        background-color: #FFF8DC;
        border-radius: 18px;
        padding: 36px;
        margin-bottom: 36px;
        text-align: center;
        border: 2px solid #FFD700;
    }
    input[type=number]::-webkit-inner-spin-button, 
    input[type=number]::-webkit-outer-spin-button { 
      -webkit-appearance: none;
      margin: 0; 
    }
    input[type=number] {
      -moz-appearance: textfield;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("2 Digit Calculator")
st.header("Let's have fun with numbers!")

# Session state for operation, result, and equation
for key, default in [('selected_op', None), ('result', ''), ('num1', 0), ('num2', 0), ('reset_counter', 0)]:
    if key not in st.session_state:
        st.session_state[key] = default

# Map for operation symbols
op_map = {'add': '➕', 'sub': '➖', 'mul': '✖️', 'div': '➗'}
selected_symbol = op_map.get(st.session_state['selected_op'], "?")



# Number input fields (restricted to 2 digits, only numbers allowed)
col1, col2 = st.columns(2)
num1_warning = num2_warning = False
# Track last valid values
if 'last_valid_num1' not in st.session_state:
    st.session_state['last_valid_num1'] = '0'
if 'last_valid_num2' not in st.session_state:
    st.session_state['last_valid_num2'] = '0'

with col1:
    num1_input = st.text_input("First Number", value=st.session_state['last_valid_num1'], key=f"num1_input_{st.session_state['reset_counter']}", max_chars=2)
    if num1_input.isdigit() and len(num1_input) <= 2:
        st.session_state['last_valid_num1'] = num1_input
        num1 = int(num1_input) if num1_input else 0
    else:
        num1_warning = True
        num1 = int(st.session_state['last_valid_num1']) if st.session_state['last_valid_num1'] else 0
    st.session_state['num1'] = num1
    st.caption("Only 2 digits allowed (0-99)")
with col2:
    num2_input = st.text_input("Second Number", value=st.session_state['last_valid_num2'], key=f"num2_input_{st.session_state['reset_counter']}", max_chars=2)
    if num2_input.isdigit() and len(num2_input) <= 2:
        st.session_state['last_valid_num2'] = num2_input
        num2 = int(num2_input) if num2_input else 0
    else:
        num2_warning = True
        num2 = int(st.session_state['last_valid_num2']) if st.session_state['last_valid_num2'] else 0
    st.session_state['num2'] = num2
    st.caption("Only 2 digits allowed (0-99)")
if num1_warning:
    st.warning("First number must be 0-99 and only 2 digits.", icon="⚠️")
if num2_warning:
    st.warning("Second number must be 0-99 and only 2 digits.", icon="⚠️")


# Operation buttons in a single row, all same size and full width
op_cols = st.columns(4)
ops = ['add', 'sub', 'mul', 'div']
for i, op in enumerate(ops):
    with op_cols[i]:
        if st.button(op_map[op], key=f"{op}_btn", use_container_width=True):
            st.session_state['selected_op'] = op
selected_symbol = op_map.get(st.session_state['selected_op'], "?")



# Enter and Reset buttons in a row
action_col1, action_col2 = st.columns(2)
with action_col1:
    enter_pressed = st.button("Enter", key="enter_btn", use_container_width=True)



with action_col2:
    reset_pressed = st.button("Reset", key="reset_btn", use_container_width=True)

# Calculation logic
if enter_pressed:
    result = None
    error_msg = ""
    if st.session_state['selected_op'] is None:
        error_msg = "Please select an operation."
    elif not (0 <= num1 <= 99 and 0 <= num2 <= 99):
        error_msg = "Both numbers must be between 0 and 99."
    elif st.session_state['selected_op'] == 'add':
        result = add(num1, num2)
    elif st.session_state['selected_op'] == 'sub':
        result = subtract(num1, num2)
    elif st.session_state['selected_op'] == 'mul':
        result = multiply(num1, num2)
    elif st.session_state['selected_op'] == 'div':
        if num2 == 0:
            error_msg = "Oops! Can't divide by zero. Try another number. 🦄"
        else:
            result = divide(num1, num2)
    if error_msg:
        st.warning(error_msg)
        st.session_state['result'] = ""
    elif result is not None:
        st.session_state['result'] = f"{num1} {selected_symbol} {num2} = {result} 🎊"
    else:
        st.session_state['result'] = ""


# Reset logic: only reset relevant keys
if reset_pressed:
    for key in ['selected_op', 'result', 'num1', 'num2']:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state['last_valid_num1'] = '0'
    st.session_state['last_valid_num2'] = '0'
    st.session_state['reset_counter'] += 1
    st.rerun()

# Single equation/result box above everything but the title
equation_str = f"{st.session_state['num1']} {selected_symbol} {st.session_state['num2']}"
display_str = st.session_state['result'] if st.session_state['result'] else equation_str
st.markdown(
    f"""
    <div style="
        width:100%;
        background-color:#FFF9C4;
        padding:16px;
        border-radius:10px;
        text-align:center;
        box-sizing:border-box;
        font-weight:600;
        font-size:20px;
    ">
        {display_str}
    </div>
    """,
    unsafe_allow_html=True,
)