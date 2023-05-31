import streamlit as st
import pandas
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


st.set_page_config(layout="wide")
add_bg_from_local('zoUiZ7.jpg')



# set page layout to wide


# standard header
st.title("Mr & Mrs Game")


st.header("Questions")


df = pandas.read_csv("data.csv", sep=",")

for index, row in df.iterrows():
    st.subheader(f'{row["number"].title()}')
    st.title(f'{row["question"]}')
    st.video(f'{row["link"]}')

