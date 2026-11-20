from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ووشانێ",
    page_icon="🎲",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default top spacing and keep the embedded game centred.
st.markdown(
    """
    <style>
      .block-container { padding-top: 0.5rem; padding-bottom: 0.5rem; }
      header[data-testid="stHeader"] { display: none; }
      footer { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("ووشانێ.html")
game_html = html_path.read_text(encoding="utf-8")
components.html(game_html, height=620, scrolling=True)
