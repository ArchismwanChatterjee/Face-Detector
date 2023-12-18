import streamlit as st
from PIL import Image

import os

import google.generativeai as genai

from dotenv import load_dotenv, dotenv_values  # we can use load_dotenv or dotenv_values both perform the same task

load_dotenv()

# print(os.getenv("MY_SECRET_KEY"))

genai.configure(api_key=os.getenv("SECRET_KEY"))

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}



def main():
    st.title("Face Detector 🔍")
    
    disclaimer_message = """This is a face detector model so preferably use images accordingly for best results 🙂. As this is a AI Model the accuracy to detect the famous person correctly is approx 90% or more. So kindly donot take the results seriously."""

    # Hide the disclaimer initially
    st.write("")

    # Show the disclaimer if the button is clicked
    with st.expander("Disclaimer ⚠️", expanded=False):
       st.markdown(disclaimer_message)
    

    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

        # Process the image (example: get image dimensions)
        image = Image.open(uploaded_image)
        width, height = image.size
        st.write("Image Dimensions:", f"{width}x{height}")

        if st.button("Identify "):

            st.success("Wait a min, Detecting...")

            vision_model = genai.GenerativeModel('gemini-pro-vision')
            response = vision_model.generate_content(["Identify the famous person/persons from the image. Also provide the head count. If you are not able to detect then simply write face detected and provide the head count. Try to detect the person. Note that the person in the image might be singers ,players, actors, freedom fighters, CEO and more.",image])

            
            st.write("Results:  \n", response.text)

            st.write("As an AI Model, if there is any mistake please consider")

            st.success("Thanks for visiting 🤩!!")

            st.info("For trying out with another image just click on browse files, enjoy 😄!!!")


if __name__ == "__main__":
    main()

