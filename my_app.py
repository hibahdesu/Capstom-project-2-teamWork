# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from textwrap import fill
import pickle
import requests
import json
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder

st.sidebar.markdown("# Main page 🎈")

html_style0 = """
<div>
<h1 style="color:#83C4F8;text-align:center; font-size: 48px">Employee Churn Prediction App</h1>
</div>"""
st.markdown(html_style0,unsafe_allow_html=True)

# Add image
# img = Image.open("car.jpg")
# st.image(img, caption="car")


import streamlit as st
from PIL import Image
import base64
        # overflow: hidden;
# Define the CSS style
css = """
<style>
    .rounded-image {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
        max-width: 100%;
    }
</style>
"""

# Display the CSS style
st.markdown(css, unsafe_allow_html=True)

# Display the image with rounded corners
image_path = 'ch5.png'
image_html = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}"></div>'
st.markdown(image_html, unsafe_allow_html=True)



# st.header("About The App")
html_style3 = """
<div style="padding:8px;margin-bottom:24px">
<h2 style="color:#8389f8;text-align:center;font-size:40px">About the app</h2>
</div>"""
st.markdown(html_style3,unsafe_allow_html=True)
st.markdown('Welcome to the Employee Churn Analysis App! This powerful tool helps organizations gain insights into employee turnover rates and predict potential churn.')
st.markdown('To begin exploring your employee churn data, simply upload your dataset or connect to your existing HR database. The app will guide you through the analysis and provide step-by-step instructions on how to interpret the results.')
st.markdown("By understanding the factors that contribute to employee attrition, businesses can take proactive measures to improve employee retention and create a more engaged workforce.")

# st.header('How it works')
html_style4 = """
<div style="padding:8px;margin-bottom:24px">
<h2 style="color:#8389f8;text-align:center;font-size:40px">How it works</h2>
</div>"""
st.markdown(html_style4,unsafe_allow_html=True)
st.markdown("To begin exploring your employee churn data, simply upload your employee information. The app will predict if the employee will continue working in the company or not.")
st.markdown("The app will then process this information and apply advanced prediction model to provide estimated state of the worker.")

# Add image
# img = Image.open("al.png")
# st.image(img, caption="ML")


# st.header('Features')
# st.markdown("")
# st.markdown("Whether you're looking to buy a car, sell one, this app empowers you with valuable insights.")


# Add image
# img = Image.open("car2.jpg")
# st.image(img, caption="car")

# st.header('Still Waiting! 🎈')
# st.markdown("Harry Up, and get ready to embark on a journey of car prediction and exploration. Start using the Cars Prediction App today and unlock a world of data-driven predictions to enhance your car-related decisions.")



html_style5 = """
<div style="padding:8px;">
<h2 style="color:#8389f8;text-align:center;font-size:40px">Are you an employer?</h2>
</div>"""
st.markdown(html_style5,unsafe_allow_html=True)

css2 = """
<style>
    .rounded-image {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 10px;
        max-width: 100%;
    }
</style>
"""

# Display the CSS style
st.markdown(css2, unsafe_allow_html=True)

# Display the image with rounded corners
image_path2 = 'ch7.jpg'
image_html2 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path2, "rb").read()).decode()}"></div>'
st.markdown(image_html2, unsafe_allow_html=True)
st.markdown("Are you an employer and you want to know if your employee will continue working with you or not? ")
# st.markdown("You are in the right place, you can now use our Machine learning features and find out.")

html_style6 = """
<div>
<h2 style="color:#8389f8;text-align:center;font-size:24px">You are in the right place, you can now use our Machine Learning Model and predict the situation of your employee.</h2>
</div>"""
st.markdown(html_style6,unsafe_allow_html=True)