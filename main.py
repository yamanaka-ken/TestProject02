import streamlit as st
from pages import page1, page2, page3

# 初期ページ設定
if "page" not in st.session_state:
    st.session_state.page = "page1"

# ページ切替関数
def go(page_name):
    st.session_state.page = page_name

# ページ描画
if st.session_state.page == "page1":
    home.render(go)

elif st.session_state.page == "page2":
    page1.render(go)

elif st.session_state.page == "page3":
    page2.render(go)