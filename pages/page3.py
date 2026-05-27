import streamlit as st


def show_page3(move):
    st.title("新規登録")

    if st.button("ログイン画面へ戻る"):
        move("page1")

    if st.button("登録"):
        move("page2")