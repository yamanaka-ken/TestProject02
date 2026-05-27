import streamlit as st


def show_page4(move):
    st.title("カスタマイズ")

    if st.button("ログイン画面へ戻る"):
        move("page1")
    
    if st.button("車種選択に戻る"):
        move("page2")