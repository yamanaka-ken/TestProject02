import streamlit as st

def render(go):
    st.title("ホーム")
    st.write("ここはホームページです。")

    if st.button("ページ2へ"):
        go("page2")

    if st.button("ページ3へ"):
        go("page3")

    if st.button("ページ4へ"):
        go("page4")