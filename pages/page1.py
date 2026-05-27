import streamlit as st


def show_page1(move):
    st.title("Page1")

    if st.button("Page2へ"):
        move("page2")

    if st.button("Page3へ"):
        move("page3")