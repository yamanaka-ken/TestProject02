import streamlit as st

from pages.page1 import show_page1
from pages.page2 import show_page2
from pages.page3 import show_page3
from pages.page4 import show_page4

st.set_page_config(
    page_title="Sample",
    initial_sidebar_state="collapsed"
)

# サイドバー非表示
st.markdown("""
<style>

/* サイドバー本体を消す */
[data-testid="stSidebar"] {
    display: none;
}

/* 開閉ボタンも消す */
[data-testid="collapsedControl"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

# 現在ページ
if "page" not in st.session_state:
    st.session_state.page = "page1"


def move(page_name):
    st.session_state.page = page_name
    st.rerun()


page = st.session_state.page

if page == "page1":
    show_page1(move)

elif page == "page2":
    show_page2(move)

elif page == "page3":
    show_page3(move)

elif page == "page4":
    show_page4(move)