import streamlit as st


def show_page3(move):
    st.title("Page3")

    if st.button("Page4へ"):
        move("page4")