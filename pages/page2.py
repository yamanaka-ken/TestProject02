import streamlit as st


def show_page2(move):
    st.title("車種選択")

    if st.button("ログイン画面へ戻る"):
        move("page1")
    
    if st.button("車種決定"):
        move("page4")