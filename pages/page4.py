import streamlit as st


def show_page4(move):
    st.title("Page4")

    if st.button("Page1へ戻る"):
        move("page1")