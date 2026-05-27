import streamlit as st


def show_page2(move):
    st.title("Page2")

    if st.button("Page1へ戻る"):
        move("page1")