# ai-wrapper-gui
# As a study, writing a wrapper for Gemini 2; first was a command line application, this is a GUI app, eventually as a WebUI.
# Study by Ethan P.

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from PySide6.QtCore import Slot

# The catalyst for PySide
app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle("AI Wrapper GUI")
window.setGeometry(100, 100, 600, 400)

# Craft components to be laid out
prompt_label = QLabel("Enter your prompt:")
prompt_input = QLineEdit()
send_button = QPushButton("Send to AI")
output_area = QTextEdit()
output_area.setReadOnly(True)

layout = QVBoxLayout()

# Layout the components
layout.addWidget(prompt_label)
layout.addWidget(prompt_input)
layout.addWidget(send_button)
layout.addWidget(QLabel("AI Response:"))
layout.addWidget(output_area)

window.setLayout(layout)

@Slot()
def send_prompt():

    #Get text from input field
    prompt = prompt_input.text()

    #Simulate response
    response = f"{prompt}\nLet's delve into that tapestry of insight"
    output_area.setText(response)

send_button.clicked.connect(send_prompt)

window.show()
sys.exit(app.exec())