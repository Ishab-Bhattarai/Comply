import streamlit as st

st.set_page_config(page_title="GDPR Assessment", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("GDPR — Gap Assessment")
st.write("Answer each question honestly. We'll identify where you're exposed.")

st.header("1. Lawful basis for processing")
q1 = st.radio("Do you know the lawful basis for every type of personal data you process?", ["Yes", "No", "Not sure"])
q2 = st.radio("Do you have a privacy notice on your website explaining how you use data?", ["Yes", "No", "Not sure"])

st.header("2. Consent")
q3 = st.radio("Do you obtain clear consent before sending marketing emails?", ["Yes", "No", "Not sure"])
q4 = st.radio("Can people withdraw their consent easily?", ["Yes", "No", "Not sure"])

st.header("3. Individual rights")
q5 = st.radio("Can you respond to a subject access request within 30 days?", ["Yes", "No", "Not sure"])
q6 = st.radio("Do you have a process for deleting someone's data if they request it?", ["Yes", "No", "Not sure"])

st.header("4. Data security")
q7 = st.radio("Is personal data encrypted when stored and transmitted?", ["Yes", "No", "Not sure"])
q8 = st.radio("Do you have a process for detecting and reporting data breaches within 72 hours?", ["Yes", "No", "Not sure"])

st.header("5. Data retention")
q9 = st.radio("Do you have a policy for how long you keep personal data?", ["Yes", "No", "Not sure"])
q10 = st.radio("Do you regularly delete data you no longer need?", ["Yes", "No", "Not sure"])

st.header("6. Third parties")
q11 = st.radio("Do you have data processing agreements with third parties who handle your data?", ["Yes", "No", "Not sure"])
q12 = st.radio("Do you know which countries your data is stored or processed in?", ["Yes", "No", "Not sure"])

if st.button("Show my results"):
    answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]
    questions = [
        "Lawful basis documented", "Privacy notice in place",
        "Marketing consent obtained", "Consent withdrawal process",
        "Subject access request process", "Right to erasure process",
        "Data encrypted", "Breach reporting process",
        "Retention policy in place", "Regular data deletion",
        "Data processing agreements", "Data transfer locations known"
    ]
    score = answers.count("Yes")
    total = len(answers)
    pct = int((score / total) * 100)

    st.divider()
    st.subheader(f"Your score: {score}/{total} ({pct}%)")

    if pct >= 80:
        st.success("Good GDPR posture. A few areas to tighten up.")
    elif pct >= 50:
        st.warning("Moderate risk. Several gaps need addressing.")
    else:
        st.error("High risk of non-compliance. Significant gaps identified.")

    st.subheader("Your gaps:")
    for q, a in zip(questions, answers):
        if a != "Yes":
            st.write(f"❌ {q} — {a}")
        else:
            st.write(f"✅ {q}")

    gaps = [q for q, a in zip(questions, answers) if a != "Yes"]
    if gaps:
        st.warning(f"⚠️ Maximum GDPR fine: up to £17.5 million or 4% of annual turnover — whichever is higher.")