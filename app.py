<<<<<<< HEAD
import streamlit as st
from bot import repondre

st.title("Mon Chatbot")

# Initialiser l'historique de conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher les messages précédents
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if prompt := st.chat_input("Écris ton message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtenir la réponse du bot
    _, _, reponse = repondre(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reponse})
    with st.chat_message("assistant"):
=======
import streamlit as st
from bot import repondre

st.title("Mon Chatbot")

# Initialiser l'historique de conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher les messages précédents
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if prompt := st.chat_input("Écris ton message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtenir la réponse du bot
    _, _, reponse = repondre(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reponse})
    with st.chat_message("assistant"):
>>>>>>> c28d3c9d8d1eb8ad704793ee4cedca9b5342313c
        st.markdown(reponse)