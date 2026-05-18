# PassGenerator

**Student Name:** Wissam Fawaz  
**Student Number:** 240417959
**Course:** Visual Programming COM206

## 1. Introduction

### Research Question / Problem Statement
*How can we design an efficient, lightweight desktop tool to safely generate unpredictable authentication passwords by leveraging standard string pools alongside a state-managed, reactive user interface?*

Traditional password generation relies on custom, predictable pseudo-random algorithms or cluttered web-based tools that overload users with heavy configurations.

### Objective of the Project
The goal is to build a single-screen desktop application in Python using PySide6 that decouples data management from style rules. It will be featuring 3 choices and a single button for simplicity.

### Expected Outcome
A fully operational modern desktop application utilizing custom checkbox filters. The app demonstrates handling state logic with Python's conditional checks, managing UI triggers through Qt's slot/signal architecture, and rendering a flat, cohesive layout.

## 2. Methodology

As an input strategy for this application, I used `QCheckBox` elements to safely listen to configuration toggles. The program uses structural string concatenation to adjust the available characters in real-time, feeding a cryptographically secure choice loop to keep passwords random and unpredictable.

### PSEUDOCODE

START PROGRAM
Import libraries: string, secrets
Initialize baseline string: charPool = string.ascii_lowercase

Render GeneratorScreen()
LISTEN for UserClick on generate_button:
    CALL function generatePassword()
    
FUNCTION generatePassword():
    IF chk_caps is checked THEN
        charPool = charPool + string.ascii_uppercase
    END IF
    
    IF chk_numbers is checked THEN
        charPool = charPool + string.digits
    END IF
    
    IF chk_symbols is checked THEN
        charPool = charPool + string.punctuation
    END IF
    
    LOOP 16 times:
        Select secure character from charPool
        Append character to passwordString
    END LOOP
    
    Update display_field with passwordString
END FUNCTION
END PROGRAM

## 3. Technical Implementation

**Programming Language:** Python 3  
**Framework:** PySide6 (THE Official Qt for Python)

### LOGIC SNAPSHOT:

```python
def generate_password(self):
    """Assembles allowed characters and builds a secure random password."""
    char_pool = string.ascii_lowercase
    
    if self.chk_caps.isChecked():
        char_pool += string.ascii_uppercase
    if self.chk_numbers.isChecked():
        char_pool += string.digits
    if self.chk_symbols.isChecked():
        char_pool += string.punctuation

    # Generate a highly secure 16-character password using the custom pool
    password = "".join(secrets.choice(char_pool) for _ in range(16))
    self.result_field.setText(password)
```
 ## 4. HOW TO RUN
Ensure you have Python installed on your system.

Open your terminal inside the project directory root.

Run the installation command to fetch the dark theme and GUI framework dependencies:

    .\.venv\Scripts\pip install -r requirements.txt --ignore-requires-python

Launch the main program using the following terminal command:

    .\.venv\Scripts\python.exe src/main.py
    
OR BY SIMPLY DOWNLOAD THE MAIN.EXE FILE USING THIS PATH

--> dist folder --> main.exe
press on main.exe and it will start the download 

###### NOTE::::::::: Make sure your terminal is using the local environment path or it will throw a module error.
