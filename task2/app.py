import streamlit as st
from PIL import Image

st.title("Multi-Modal GenAI Chatbot (Demo)")

question = st.text_input("Enter your question")
image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if st.button("Submit"):
    if image_file:
        image = Image.open(image_file)

        response = f"""
        🖼️ Image received successfully.

        User question:
        "{question}"

        Simulated Gemini Response:
        The image appears to be a real-world scene. Based on the visual content,
        the system can identify objects, context, and provide a meaningful
        description or explanation related to the user query.
        """
    else:
        response = f"""
        🤖 Simulated Gemini Response:

        You asked:
        "{question}"

        This response demonstrates how a GenAI chatbot would generate
        a contextual answer using a large language model.
        """

    st.subheader("Response")
    st.write(response)
