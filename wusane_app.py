from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ووشانێ",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Give the game the available width without Streamlit's default page padding.
st.markdown(
    """
    <style>
      .block-container {
        max-width: 1000px;
        padding: 0.5rem;
      }
      header[data-testid="stHeader"] { display: none; }
      footer { display: none; }
      iframe[data-testid="stIFrame"] { height: 780px; }
      @media (min-width: 596px) {
        iframe[data-testid="stIFrame"] { height: 560px; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("ووشانێ.html")
game_html = html_path.read_text(encoding="utf-8")
components.html(game_html, height=780, scrolling=True)
