import streamlit as st

def render(go):
    st.title("ページ3")
    st.write("これはページ3です。")

    if st.button("ホームへ戻る"):
        go("page1")