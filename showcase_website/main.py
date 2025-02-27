import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns([1.5, 1])

with col1:
    st.title("Col-1")

with col2:
    st.title("Col-2")
    content = """
    12345
    1234
    """

    st.info(content)

content2 = """ 
1234
1234
"""
st.write(content2)

col3, col4 = st.columns(2)

with col3:
    st.title("Col-3")

with col4:
    st.title("Col-4")
    content3 = """
    12345
    1234
    """

    st.info(content3)

content4 = """ 
1234
1234
"""
st.write(content4)