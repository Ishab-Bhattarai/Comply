import streamlit as st

st.set_page_config(
    page_title="Comply",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Comply")
st.subheader("Cybersecurity compliance for growing businesses")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Frameworks supported", "4")
with col2:
    st.metric("Avg. time to Essentials", "2 weeks")
with col3:
    st.metric("Questionnaires automated", "∞")

st.info("👈 Start with an assessment in the sidebar")
st.sidebar.title("Navigation")