# ai-wrapper-gui
# As a study, writing a wrapper for Gemini 2; first was a command line application, this is a GUI app, eventually as a WebUI.
# Study by Ethan P.

import os
from google import genai

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from PySide6.QtCore import Slot

#Store API key,model name, and AI client for future use
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set. Please set it in your system's environment variables.")
MODEL_NAME = "gemini-2.0-flash"
genai_client = genai.Client(api_key=API_KEY)

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

def call_ai(prompt):
    try: # Error handling

        # Craft the API call within 'response', return the output text content
        # so that the API interaction is called and recorded by 'response' and this function outputs the textual content.
        response = genai_client.models.generate_content(
            model = MODEL_NAME,
            contents = prompt
            )

    except Exception as e:
        exception_response = f"Error generating response (f to pay respects): \"{e}\""
        return exception_response

    return response.text

@Slot()
def send_prompt():

    #Get text from input field
    user_prompt = prompt_input.text()

    ai_response = call_ai(user_prompt)
    output_area.setText(ai_response)

send_button.clicked.connect(send_prompt)

window.show()
sys.exit(app.exec())