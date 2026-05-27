import streamlit as st

def render(go):
    st.title("ページ4")
    st.write("これはページ4です。")

    if st.button("ホームへ戻る"):
        go("page1")