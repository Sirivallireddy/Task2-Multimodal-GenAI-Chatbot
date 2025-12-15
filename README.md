# Task 2 – Multimodal GenAI Chatbot

## Overview
This project demonstrates a **multi-modal GenAI chatbot** capable of handling
both **text input and image upload** through a simple web-based interface.
The application is built using **Streamlit** to showcase the overall GenAI
workflow and multimodal interaction design.

Due to current API access and SDK limitations for live Gemini vision inference
in the Python environment, the chatbot simulates GenAI responses while
preserving the complete multimodal interaction pipeline.

This approach is commonly used during prototyping and early-stage GenAI
application development.

---

## Features
- Text-based user interaction
- Image upload support (multi-modal input)
- Simulated GenAI response generation
- Web-based interface using Streamlit
- Clear demonstration of multimodal chatbot workflow

---

## Technology Stack
- Python
- Streamlit
- Pillow (for image handling)

---

## Project Structure
Task2-Multimodal-GenAI-Chatbot/
│
├── app.py
├── requirements.txt
└── README.md


---

## How to Run the Project

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
Run the application:

streamlit run app.py
