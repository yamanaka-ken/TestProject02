import streamlit as st


def show_page1(move):
    st.title("ログイン")

    if st.button("ログイン"): #車種選択画面へ
        move("page2")

    if st.button("新規登録"): #新規登録画面へ
        move("page3")