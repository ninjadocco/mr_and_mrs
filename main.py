import streamlit as st
import pandas

# set page layout to wide
st.set_page_config(layout="wide")

description = """The term generic brand refers to a type of consumer product on the market that lacks a widely recognized name or logo
because it typically isn't advertised. Generic brands are usually less expensive than their brand name counterparts
due to their lack of promotion, which can inflate the cost of a good or service. These brands, which are designed as
substitutes for more expensive brand name goods, are especially common in the food and pharmaceutical industry and
tend to be more popular during a recession.
"""

# standard header
st.title("Mr & Mrs Game")


st.header("Questions")


df = pandas.read_csv("data.csv", sep=",")

for index, row in df.iterrows():
    st.subheader(f'{row["number"].title()}')
    st.title(f'{row["question"].title()}')
    st.video(f'{row["link"]}')

