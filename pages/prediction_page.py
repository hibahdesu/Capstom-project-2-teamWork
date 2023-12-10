# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from textwrap import fill
import pickle
import requests
import base64
import json
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder




# st.markdown("# Prediction page ")
st.sidebar.markdown("# Prediction page 🎉")
# background-color:#996600;

html_style = """
<div style="padding:8px;border-radius:40px;margin-bottom:24px">
<h2 style="color:#83C4F8;text-align:center;font-size:24px">Churn Prediction</h2>
</div>"""
st.sidebar.markdown(html_style,unsafe_allow_html=True)

html_style2 = """
<div style="padding:8px; border-radius:40px;margin-bottom:24px">
<h2 style="color:#83C4F8;text-align:center;font-size:64px">Now, you can predict with ML 🎉</h2>
</div>"""
st.markdown(html_style2,unsafe_allow_html=True)

# img2 = Image.open("ch4.png")
# st.image(img2, caption="jobs")

# Define the CSS style
# border-radius: 200px;
css = """
<style>
    .rounded-image {
        overflow: hidden;
        padding: 0px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
        margin-left: 30px;
    }
</style>
# """

# Display the CSS style
st.markdown(css, unsafe_allow_html=True)

# Display the image with rounded corners
image_path = 'ch4.jpg'
image_html = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}"></div>'
st.markdown(image_html, unsafe_allow_html=True)

# number_project=st.sidebar.selectbox("Select Num of Projects on last year", (1, 3, 4, 5, 6, 7, 8, 9,10)) 


import streamlit as st

# Define the options
options = (1,2, 3, 4, 5, 6, 7, 8, 9, 10)

# Display the select box with hover effect
number_project = st.sidebar.selectbox(
    "Select num of projects",
    options,
    format_func=lambda x: f'{x}',
    key="num_of_projects",
    help="Select the number of projects you have done last year"
)

# Apply the CSS class to the select box
# st.markdown(
#     f"""
#     <style>
#         .hover-select select[name=num_of_projects] {{
#             background-color: white;
#         }}
#         .hover-select:hover select[name=num_of_projects] {{
#             background-color: lightgray;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Display the selected option
# st.sidebar.markdown(f"Selected Option: {number_project}")



time_spend_company = st.sidebar.selectbox(
    "Select time spent",
    options,
    format_func=lambda x: f'{x}',
    key="time_spend_company",
    help="Select the time you have spent in the company"
)
# time_spend_company=st.sidebar.selectbox("Select time spent",(1, 2, 3, 4, 5, 6, 7, 8, 9,10))
# Display the slider for satisfaction level
satisfaction_level = st.sidebar.slider(
    "Select satisfaction level",
    0.00, 1.00, step=0.01,
    key="satisfaction_level",
    help="Select the level of satisfaction"
)

# Display the selected satisfaction level
# st.sidebar.markdown(f"Selected Satisfaction Level: {satisfaction_level}")

# satisfaction_level=st.sidebar.slider("Select satisfaction level", 0.00, 1.00, step=0.01)

# Display the slider for satisfaction level
last_evaluation = st.sidebar.slider(
    "Select last evaluation",
    0.00, 1.00, step=0.01,
    key="last_evaluation",
    help="Select the last evaluation"
)

# Display the selected satisfaction level
# st.sidebar.markdown(f"Select the last evaluation: {last_evaluation}")
# last_evaluation=st.sidebar.slider("Select last evaluation", 0.00, 1.00, step=0.01)
average_montly_hours = st.sidebar.slider(
    "Select month's hour",
    90, 310, step=1,
    key="average_montly_hours",
    help="Select how many hours you have spent each month"
)
# average_montly_hours=st.sidebar.slider("Select month's hour:",90 ,310, step=1)




filename = "final_rf"
model=pickle.load(open(filename, "rb"))


my_dict = {
    "satisfaction_level": satisfaction_level,
    "last_evaluation": last_evaluation,
    "number_project": number_project,
    "average_montly_hours": average_montly_hours,
    "time_spend_company": time_spend_company
}


df = pd.DataFrame.from_dict([my_dict])
df.index = ["Employee information"] * len(df)

# df['satisfaction_level'] = df['satisfaction_level'].round(2)

# Function to apply background color based on cell values
def highlight_cells(val):
    if val == 0:
        return "background-color: red; color: white"
    elif val == 1:
        return "background-color: green; color: white"
    elif val == 0.5:
        return "background-color: white"
    elif 0 < val < 0.5:
        red_value = int(255 * (0.5 - val) / 0.5)
        return f"background-color: rgb(255, {255 - red_value}, {255 - red_value})"
    else:
        green_value = int(255 * (val - 0.5) / 0.5)
        return f"background-color: rgb({255 - green_value},255, {255 - green_value})"

# Apply the custom styling to the specified columns
styled_df = df[["satisfaction_level", "last_evaluation"]].style.applymap(highlight_cells)


# Display the styled DataFrame using st.table
# st.header("The values you have chosen: ")

html_style3 = """
<div style="padding:8px;margin-bottom:24px">
<h2 style="color:#8389f8;text-align:center;font-size:40px">The values you have chosen:</h2>
</div>"""
st.markdown(html_style3,unsafe_allow_html=True)
# st.table(df.style.format('{:.2f}').applymap(highlight_cells, subset=["satisfaction_level", "last_evaluation"]))# Display the styled DataFrame using st.table

########################################################33
# Display the styled DataFrame using st.table
# st.header("The values you have chosen: ")
# st.table(df.style.format('{:.2f}').applymap(highlight_cells, subset=["satisfaction_level", "last_evaluation"]))# Display the styled DataFrame using st.table

def display_transposed_table(data):
    # Transpose the dataframe
    transposed_data = data.T

# Apply the highlight function to the first two rows
    styled_data = transposed_data.style.applymap(highlight_cells, subset=pd.IndexSlice[transposed_data.index[:2], :])

# Format the first two rows with 2 decimal places
    styled_data = styled_data.format("{:.2f}", subset=pd.IndexSlice[transposed_data.index[:2], :])

# Format the rest of the rows as integers
    styled_data = styled_data.format("{:.0f}", subset=pd.IndexSlice[transposed_data.index[2:], :])

# Display the styled DataFrame using st.table
    st.table(styled_data)



display_transposed_table(df)



#########################################################33

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)

css2 = """
<style>
    .rounded-image {
        overflow: hidden;
        margin-right: 50px;
        margin-left: 70px;
        max-width: 80%;
    }
</style>
# """

try: 
    if predict :            
        
        if (result[0] == 0):
            st.balloons()
            st.success(f'The employee is still working at the company')
            # img = Image.open("ch.jpg")
            # st.image(img, caption="stay")


            st.markdown(css2, unsafe_allow_html=True)

            # Display the image with rounded corners
            image_path2 = 'ch.jpg'
            image_html2 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path2, "rb").read()).decode()}"></div>'
            st.markdown(image_html2, unsafe_allow_html=True)


        elif (result[0] == 1):
        # st.success(f'The employee: {result[0]} the company')
            st.warning(f'The employee left the company')
            # img = Image.open("ch6.jpg")
            # st.image(img, caption="left")
            st.markdown(css2, unsafe_allow_html=True)
            # Display the image with rounded corners
            image_path3 = 'ch6.jpg'
            image_html3 = f'<div class="rounded-image"><img src="data:image/jpeg;base64,{base64.b64encode(open(image_path3, "rb").read()).decode()}"></div>'
            st.markdown(image_html3, unsafe_allow_html=True)

    else: 
        st.warning('Select values first...')
except:
    st.warning('Something went wrong, please try again.')