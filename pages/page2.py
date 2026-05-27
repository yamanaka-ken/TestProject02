import streamlit as st

def render(go):
    st.title("ページ2")
    st.write("これはページ2です。")

    if st.button("ホームへ戻る"):
        go("page1")