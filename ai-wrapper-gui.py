# ai-wrapper-gui
# As a study, writing a wrapper for Gemini 2; first was a command line application, this is a GUI app, eventually as a WebUI.
# Study by Ethan P.

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from PySide6.QtCore import Slot

@Slot()
def send_prompt():
    print("Button pressed!")

    #Get text from input field
    prompt = prompt_input.text()
    print(f"Prompt entered: {prompt}")

    #Simulate response
    response = f"{prompt}\nLet's delve into that tapestry of insight"
    outputarea.setText(response)

# The catalyst for PySide
app = QApplication(sys.argv)

window = QWidget()

# Dummy values so something, anything happens.
window.setWindowTitle("AI Wrapper GUI")
window.setGeometry(100, 100, 400, 300)

window.show()

sys.exit(app.exec())