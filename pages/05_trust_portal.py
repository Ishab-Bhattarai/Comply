import streamlit as st
from datetime import date

st.set_page_config(page_title="Trust Portal", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("🔒 Trust Portal")
st.write("Share this page with customers and buyers to prove your compliance status.")

company_name = st.text_input("Company name", placeholder="e.g. Acme Ltd")

if company_name:
    st.divider()
    st.subheader(f"{company_name} — Security & Compliance Status")
    st.caption(f"Last updated: {date.today().strftime('%d %B %Y')}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Cyber Essentials")
        ce_status = st.selectbox("Status", ["✅ Certified", "🔄 In Progress", "❌ Not Started"], key="ce")
        st.markdown("### GDPR")
        gdpr_status = st.selectbox("Status", ["✅ Compliant", "🔄 In Progress", "❌ Not Started"], key="gdpr")
        st.markdown("### ISO 27001")
        iso_status = st.selectbox("Status", ["✅ Certified", "🔄 In Progress", "❌ Not Started"], key="iso")

    with col2:
        st.markdown("### Data handling")
        st.selectbox("Data encrypted at rest", ["✅ Yes", "❌ No"], key="enc_rest")
        st.selectbox("Data encrypted in transit", ["✅ Yes", "❌ No"], key="enc_transit")
        st.selectbox("Regular backups", ["✅ Yes", "❌ No"], key="backups")
        st.selectbox("Penetration tested", ["✅ Yes", "🔄 Scheduled", "❌ No"], key="pentest")

    st.divider()
    st.subheader("Preview — what buyers will see")
    st.info("This is how your trust portal will appear to customers and buyers.")

    with st.container():
        st.markdown(f"## {company_name}")
        st.caption(f"Security verified · {date.today().strftime('%d %B %Y')}")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Cyber Essentials", ce_status.split(" ")[0])
        with c2:
            st.metric("GDPR", gdpr_status.split(" ")[0])
        with c3:
            st.metric("ISO 27001", iso_status.split(" ")[0])

        st.success("This company uses Comply to manage and verify their cybersecurity compliance.")