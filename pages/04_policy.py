import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~/.env"))

st.set_page_config(page_title="Policy Drafting", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("AI Policy Drafting")
st.write("Generate a professional policy document in seconds.")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

company_name = st.text_input("Your company name", placeholder="e.g. Acme Ltd")
company_size = st.selectbox("Company size", ["1-10 employees", "11-50 employees", "51-200 employees", "200+ employees"])
policy_type = st.selectbox("Which policy do you need?", [
    "Acceptable Use Policy",
    "Password Policy",
    "Data Protection Policy",
    "Incident Response Policy",
    "Remote Working Policy"
])

generate_policy = st.button("Generate Policy")

if generate_policy and company_name:
    with st.spinner("Generating your policy..."):
        prompt = f"""Write a professional {policy_type} for a UK company called {company_name} with {company_size}.
        
The policy should:
- Be written in plain English
- Be appropriate for a small UK business
- Reference UK GDPR where relevant
- Include sections for: Purpose, Scope, Policy Statement, Responsibilities, and Review Date
- Be practical and realistic for a small team

Format it clearly with headers and numbered points."""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        policy = response.choices[0].message.content

        st.divider()
        st.subheader(f"{policy_type} — {company_name}")
        st.markdown(policy)

        st.download_button(
            label="Download as text file",
            data=policy,
            file_name=f"{company_name}_{policy_type.replace(' ', '_')}.txt",
            mime="text/plain"
        )

elif generate_policy and not company_name:
    st.error("Please enter your company name first.")