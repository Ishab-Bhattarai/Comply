import streamlit as st

st.set_page_config(page_title="Cyber Essentials Assessment", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("Cyber Essentials — Gap Assessment")
st.write("Answer each question honestly. We'll show you exactly where you stand.")

st.header("1. Firewalls")
q1 = st.radio("Do you have a firewall protecting your internet connection?", ["Yes", "No", "Not sure"])
q2 = st.radio("Do you change default passwords on routers and firewalls?", ["Yes", "No", "Not sure"])

st.header("2. Secure configuration")
q3 = st.radio("Do you remove or disable software you don't need?", ["Yes", "No", "Not sure"])
q4 = st.radio("Do you change default credentials on all new devices?", ["Yes", "No", "Not sure"])

st.header("3. Access control")
q5 = st.radio("Do you limit admin accounts to only those who need them?", ["Yes", "No", "Not sure"])
q6 = st.radio("Do you use unique passwords for each user account?", ["Yes", "No", "Not sure"])

st.header("4. Malware protection")
q7 = st.radio("Do you have antivirus or malware protection on all devices?", ["Yes", "No", "Not sure"])
q8 = st.radio("Is your malware protection kept up to date automatically?", ["Yes", "No", "Not sure"])

st.header("5. Patch management")
q9 = st.radio("Do you apply software updates within 14 days of release?", ["Yes", "No", "Not sure"])
q10 = st.radio("Do you use supported, up-to-date operating systems?", ["Yes", "No", "Not sure"])

if st.button("Show my results"):
    answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    questions = [
        "Firewall in place", "Default passwords changed on network devices",
        "Unnecessary software removed", "Default credentials changed on devices",
        "Admin access restricted", "Unique passwords per account",
        "Malware protection installed", "Malware protection auto-updated",
        "Patches applied within 14 days", "Supported OS in use"
    ]
    score = answers.count("Yes")
    total = len(answers)
    pct = int((score / total) * 100)

    st.divider()
    st.subheader(f"Your score: {score}/{total} ({pct}%)")

    if pct >= 80:
        st.success("You're in good shape for Cyber Essentials. A few gaps to close.")
    elif pct >= 50:
        st.warning("Some work needed before you'd pass Cyber Essentials.")
    else:
        st.error("Significant gaps identified. Let's build a plan.")

    st.subheader("Your gaps:")
    for q, a in zip(questions, answers):
        if a != "Yes":
            st.write(f"❌ {q} — {a}")
        else:
            st.write(f"✅ {q}")

    st.session_state.gaps = [q for q, a in zip(questions, answers) if a != "Yes"]
    if st.session_state.gaps:
        if st.button("View my remediation plan →"):
            st.switch_page("pages/02_remediation.py")