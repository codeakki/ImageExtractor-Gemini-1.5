##Invoice Extractor 

from dotenv import load_dotenv  

# load all environment variables from .env file
load_dotenv()

import streamlit as st


import os 

from PIL import Image

import google.generativeai as genai

## config api key 


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

### function to load Gemini Pro vision model and get response


def get_gemini_response(input,image,promot):
    # Load the Gemini Pro vision model
    gemini = genai.GenerativeModel("gemini-1.5-flash")

    # Get the response from the model
    response = gemini.generate_content([input,image[0],promot])

    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
      #Read the file in bytes
      bytes_data = uploaded_file.getvalue()
      image_part=[
         {
            "mime_type": uploaded_file.type,
            "data": bytes_data
         }
      ]
      return image_part
    else:
       raise FileNotFoundError("No File Uploaded")




##initalize your streamlit app 

st.set_page_config(page_title="Invoice Extractor", page_icon=":moneybag:", layout="wide")

input=st.text_input("Input Promopt: ",key="input")
uploaded_file = st.file_uploader("Upload Invoice Image", type=["jpg", "png", "jpeg"])
image=""

if uploaded_file is not None:
  image=Image.open(uploaded_file)
  st.image(image, caption='Uploaded Image.', use_column_width=True)

submit=st.button("Tell Me About the invoice ")


input_promot="""" You are an expert in undersatnding invoices. 
You will receive input image as invoice and you have to extract the information 
from the invoice also answer question based on input image."""


if submit:
        image_part=input_image_setup(uploaded_file)
        response=get_gemini_response(input_promot,image_part,input)

        st.subheader("The Response is ")
        st.write(response)
   