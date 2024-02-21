import streamlit as st
from AI_hackathon import BankAssistant
# Instantiate the class
rag_palm_query_instance = BankAssistant()

import streamlit as st

st.sidebar.header('User Feedback')
feedback = st.sidebar.radio('How would you rate your experience?', ['Positive', 'Neutral', 'Negative'])
st.sidebar.header('About')
st.sidebar.info('This banking assistant was created by Teeam Bytebrewers for AI Driven Sri lanka AI Hackathon.')

st.title(f"**Banking Assistant**")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("Enter your question here:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = rag_palm_query_instance.query_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})