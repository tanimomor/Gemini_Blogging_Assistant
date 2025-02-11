import streamlit as st

st.set_page_config(layout="wide")

st.title('Blogcraft: Your Personal Blogging Assistant')

st.subheader('Welcome to Blogcraft! 🚀')

with st.sidebar:
    st.title("Input your blog details")
    st.subheader("Enter details of the blog you want to generate")

    blog_title = st.text_input("Blog Title", "")

    keywords = st.text_input("Keywords (Comma seperated)", "")

    num_of_words = st.slider("Number of words", min_value = 250, max_value=2000, step=100)
