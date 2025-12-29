# Goal

Build a basic calculator app using:
- **Python** for backend (logic and data manipulation)
- **Streamlit** for UI/frontend (UI screens for user interaction)

## Environment Setup

1. **Open terminal**
2. **Create virtual environment**
   ```bash
   python3 -m venv dev
   ```
3. **Activate virtual environment**
   ```bash
   source dev/bin/activate
   ```
4. **Install required Python libraries for the project**
   ```bash
   pip install streamlit
   ```

## 1. Scaffold the Project Structure

- Open the GitHub Copilot Chat window (`View > Chat`) to define your workspace:
- **Request the Library:**  
  Ask Copilot:  
  `"What command should I run in the Visual Studio Terminal to install Streamlit?"`
- **Generate the File:**  
  Use the command:  
  `/new create a single-file Streamlit application named app.py`  
  in the chat. Review the proposed file structure and click **Create Workspace** or **Save** to generate the file.

## 2. Design the User Interface (UI)

- Position your cursor in `app.py` and use Inline Chat (`Cmd + I`) to describe the layout:
  - **Header:**  
    Prompt:  
    `"Create a title for the web app called 'Copilot Calculator' using Streamlit's header functions."`
  - **Inputs:**  
    Prompt:  
    `"Add two numerical input boxes that allow decimal values and a sidebar or dropdown menu to select an operation (Add, Subtract, Multiply, Divide)."`

## 3. Implement the Calculation Logic

- Highlight the UI variables you just created and use Inline Chat to link them to math logic:
  - **Conditional Logic:**  
    Prompt:  
    `"Write a conditional block that performs the selected operation on the two input numbers when a 'Calculate' button is pressed."`
  - **Output Display:**  
    Prompt:  
    `"Show the final result in a success message box or a large text format below the button."`

## 4. Robustness and Validation

- Refine the code by prompting for specific edge cases:
  - **Error Prevention:**  
    Highlight the division section and prompt:  
    `"Add a check to ensure the second number is not zero before dividing, and display a warning message if it is."`
  - **Code Documentation:**  
    Highlight the entire script and prompt:  
    `"Add docstrings and comments explaining how the Streamlit state handles these inputs."`

## 5. Execution and Verification

- **Launch Command:**  
  Ask Copilot Chat:  
  `"How do I run this Streamlit app from the Visual Studio terminal?"`  
  (It will likely suggest `streamlit run app.py`).
- **Troubleshooting:**  
  If the browser window doesn't open correctly, copy the terminal error and paste it into Copilot Chat with the prompt:  
  `"Fix this execution error."`
