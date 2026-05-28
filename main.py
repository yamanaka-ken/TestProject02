import streamlit as st
from pathlib import Path

# =========================
# 1. ページ設定
# =========================
st.set_page_config(
    page_title="Sample App",
    layout="wide",
    initial_sidebar_state="collapsed"
)


from pages.page1 import show_page1
from pages.page2 import show_page2
from pages.page3 import show_page3
from pages.page4 import show_page4

# =========================
# 5. CSS適用
# =========================
st.markdown("""
<style>

/* =========================
   全体背景
========================= */
.stApp {
    background:
        linear-gradient(
            135deg,
            #0f172a,
            #111827
        );
    color: white;
}

/* =========================
   サイドバー非表示
========================= */
[data-testid="stSidebar"],
[data-testid="collapsedControl"] {
    display: none;
}

/* =========================
   メイン余白
========================= */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* =========================
   タイトル文字
========================= */
.title-text {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    color: white;
    margin-top: 10px;
    margin-bottom: 40px;
}

/* =========================
   ボタン中央寄せ
========================= */
.stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 20px;
}

/* =========================
   ボタンデザイン
========================= */
.stButton > button {
    width: 50%;
    min-width: 220px;
    height: 50px;
    border: none;
    border-radius: 12px;
    background:
        linear-gradient(
            90deg,
            #2563eb,
            #7c3aed
        );
    color: white;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.3s ease;
}

/* Hover */
.stButton > button:hover {
    opacity: 0.9;
    transform: translateY(-2px);
    box-shadow:
        0 4px 12px
        rgba(124, 58, 237, 0.3);
    color: white;
}

/* =========================
   タイトル色
========================= */
h1, h2, h3 {

    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# 7. セッション状態初期化
# =========================
if "page" not in st.session_state:
    st.session_state.page = "page1"

# =========================
# 8. ページ移動関数
# =========================
def move(page_name):

    if st.session_state.page != page_name:

        st.session_state.page = page_name

        try:
            st.rerun()

        except:
            st.experimental_rerun()

# =========================
# 9. ルーティング
# =========================
pages = {

    "page1": show_page1,
    "page2": show_page2,
    "page3": show_page3,
    "page4": show_page4
}

# =========================
# 10. 現在ページ取得
# =========================
current_page = st.session_state.page

# =========================
# 11. ページ描画
# =========================
if current_page in pages:
    pages[current_page](move)
else:
    st.error("ページが存在しません")