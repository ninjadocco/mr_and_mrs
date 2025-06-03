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
add_bg_from_local('23bd8e3d1a0bec700d6ba3af66b0a49a.jpg')

footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/ninjadocco/mr_and_mrs/blob/main/photo.png?raw=true" target="_blank">Bonus picture</a></p>
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/ninjadocco/mr_and_mrs/blob/main/photo.png?raw=true" target="_blank">Bonus bonus picture</a></p>
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/ninjadocco/mr_and_mrs/blob/main/photo.png?raw=true" target="_blank">Chris Docherty</a></p>

</div>
"""
st.markdown(footer, unsafe_allow_html=True)

st.title("GEMMA'S HEN DO!")


st.header("Mr & Mrs Game")


df = pandas.read_csv("data.csv", sep=",")

for index, row in df.iterrows():
    st.subheader(f'{row["number"].title()}')
    st.title(f'{row["question"].title()}')
    st.video(f'{row["link"]}')

