import streamlit as st
st.title("my first streamlit app[]")
st.write("welcome to my apllication")
name = st.text_input("enter your name:")
if st.chatbot("submit"):
    st.write("hello",name)