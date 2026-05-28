import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

logo_path = BASE_DIR / "img" / "sample.png"

def show_page1(move):

    # =========================
    # CSS
    # =========================
    st.markdown("""
    <style>

    /* タイトル */
    .title-text {

        text-align: center;

        font-size: 48px;
        font-weight: 700;

        color: white;

        margin-top: 10px;
        margin-bottom: 40px;
    }

    /* input */
    .stTextInput input {

        height: 50px;

        border-radius: 12px;

        background-color: #0f172a;

        color: white;

        border: 1px solid #334155;

        padding-left: 20px;
    }

    /* placeholder */
    .stTextInput input::placeholder {

        color: #94a3b8;
    }

    /* login card */
    div[data-testid="stVerticalBlockBorderWrapper"] {

        background-color: #1e293b;

        padding: 40px;

        border-radius: 20px;

        border: none;

        box-shadow:
            0 8px 24px rgba(0,0,0,0.3);
    }

    /* ボタン */
    .stButton button {

        width: 100%;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # ロゴ
    # =========================
    col1, col2, col3 = st.columns([4,1,4])

    with col2:

        st.image(
            str(logo_path),
            width=80
        )

    # =========================
    # タイトル
    # =========================
    st.markdown("""
    <div class="title-text">
        Sample App
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # ログインエリア
    # =========================
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        # ここだけ囲まれる
        with st.container(border=True):

            st.text_input(
                label="username",
                placeholder="ユーザー名",
                label_visibility="collapsed"
            )

            st.text_input(
                label="password",
                placeholder="パスワード",
                type="password",
                label_visibility="collapsed"
            )

            if st.button("ログイン"):

                move("page2")

            if st.button("新規登録"):

                move("page3")