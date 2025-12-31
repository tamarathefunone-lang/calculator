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
    html, body, .main {
        width: 100vw !important;
        height: 100vh !important;
        overflow: hidden !important;
        background-color: #FFF8DC;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
        color: black !important;
    }
    .stApp {
        overflow: hidden !important;
    }
    .stButton>button {
        background-color: unset !important;
        color: black !important;
        font-size: 48px;
        border-radius: 16px;
        height: 0.9em;
        width: 100%;
        margin: 8px 0;
    }
    #operation-row + div button,
    button[data-testid="baseButton-secondary"] {
        background-color: #FFF9C4 !important;
        color: black !important;
        border-radius: 16px !important;
    }
    .equation-box {
        background-color: #FFF8DC;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 24px;
        text-align: center;
        border: 2px solid #FFD700;
        color: black !important;
    }
    /* Responsive font size for equation/result */
    @media (max-width: 900px) {
        .equation-box { font-size: 18px !important; }
        .stButton>button { font-size: 32px !important; }
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
#col1, col2 = st.columns(2)
num1_warning = num2_warning = False
# Track last valid values
if 'last_valid_num1' not in st.session_state:
    st.session_state['last_valid_num1'] = '0'
if 'last_valid_num2' not in st.session_state:
    st.session_state['last_valid_num2'] = '0'

# Label and read-only display for the first number (keeps in sync with keypad)
st.markdown('<div style="font-size:200%; font-weight:400; color:black;">First Number</div>', unsafe_allow_html=True)

rows = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cols = st.columns(len(rows))
for i, label in enumerate(rows):
    with cols[i]:
        if st.button(label, key=f"num1_btn_{label}_{st.session_state['reset_counter']}", use_container_width=True):
            cur = st.session_state.get('last_valid_num1', '0')
            # Digit pressed
            if label.isdigit():
                # Replace leading '0' or append if less than 2 digits
                if cur == '0':
                    new = label
                else:
                    new = cur + label if len(cur) < 2 else cur
            elif label == '⌫':  # backspace
                new = cur[:-1] if len(cur) > 1 else '0'
            else:  # 'C' clear
                new = '0'
            st.session_state['last_valid_num1'] = new

# Provide a string variable compatible with the rest of the code
num1 = int(st.session_state.get('last_valid_num1', 0))


# Operation buttons in a single row, all same size and full width
st.markdown('<div style="font-size:200%; font-weight:400;">Operations</div>', unsafe_allow_html=True)

op_cols = st.columns(4)
ops = ['add', 'sub', 'mul', 'div']
for i, op in enumerate(ops):
    with op_cols[i]:
        if st.button(op_map[op], key=f"{op}_btn", use_container_width=True):
            st.session_state['selected_op'] = op
selected_symbol = op_map.get(st.session_state['selected_op'], "?")

# Label and read-only display for the second number (keeps in sync with keypad)
st.markdown('<div style="font-size:200%; font-weight:400; color:black !important;">Second Number</div>', unsafe_allow_html=True)


rows = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

cols = st.columns(len(rows))
for i, label in enumerate(rows):
    with cols[i]:
        if st.button(label, key=f"num2_btn_{label}_{st.session_state['reset_counter']}", use_container_width=True):
            cur = st.session_state.get('last_valid_num2', '0')
            # Digit pressed
            if label.isdigit():
                # Replace leading '0' or append if less than 2 digits
                if cur == '0':
                    new = label
                else:
                    new = cur + label if len(cur) < 2 else cur
            elif label == '⌫':  # backspace
                new = cur[:-1] if len(cur) > 1 else '0'
            else:  # 'C' clear
                new = '0'
            st.session_state['last_valid_num2'] = new

# Provide a string variable compatible with the rest of the code
num2 = int(st.session_state['last_valid_num2'])

enter_pressed = st.button("Enter", key="enter_btn", use_container_width=True)

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


# Single equation/result box above everything but the title
equation_str = f"{st.session_state['last_valid_num1']} {selected_symbol} {st.session_state['last_valid_num2']}"
display_str = st.session_state['result'] if st.session_state['result'] else equation_str
st.markdown(
    f"""
    <div style="
        width:100%;
        background-color:#FFB6C1;
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

reset_pressed = st.button("Reset", key="reset_btn", use_container_width=True)

# Reset logic: only reset relevant keys
if reset_pressed:
    for key in ['selected_op', 'result', 'num1', 'num2']:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state['last_valid_num1'] = '0'
    st.session_state['last_valid_num2'] = '0'
    st.session_state['reset_counter'] += 1
    st.rerun()
