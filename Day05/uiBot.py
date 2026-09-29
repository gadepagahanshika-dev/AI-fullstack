import ollama
import streamlit as st
with st.sidebar:
    st.title("Chat Settings ⚙️")
    personalities = {
        "kid" : "Answer the questions like you are explaining to a 5 year old kid. give answer in 2 lines only.",
        "Friend" : "Answer the questions in a friendly and casual manner. give answer in 2 lines only.",
        "Professor" : "Answer the questions in a professional and academic manner. give answer in 2 lines only.",
    }
    personality = st.selectbox("select a personality", personalities.keys())
    uploaded_file = st.file_uploader("upload  a file")
    try:
        if uploaded_file:
            st.success("File uploaded successfully!✅")
            if st.button("Read file"):
                context = uploaded_file.read().decode("utf-8")
            st.text(context)
    except:
        st.error("Error")
    if st.button("Clear Chat"):
                st.session_state.msgs = []
                st.success("chat history cleared")
st.markdown(":orange[Welcome to my ChatBot app 😊]")
if "msgs" not in st.session_state:
    st.session_state.msgs = []
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question= st.chat_input("You:")
if question:
    st.session_state.msgs.append(
            {"role": "user",
            "content": question}
        )
    with st.chat_message("user"):
        st.write(question)
    
    with st.spinner("Thinking..."):
        response =  ollama.chat(
            model="llama3.2:3b",
            messages=[
                {"role" : "System", "content": personalities[personality]}]
                 + st.session_state.msgs)
    st.session_state.msgs.append(
            {"role": "assistant",
            "content": response["message"]["content"] }
        )
    with st.chat_message("Assistant"):
        st.write(response["message"]["content"])
    