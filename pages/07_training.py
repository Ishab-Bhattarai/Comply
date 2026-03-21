import streamlit as st
from datetime import date

st.set_page_config(page_title="Employee Training", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("Employee Training & Attestations")
st.write("Assign training modules to staff and track who has completed them.")

MODULES = {
    "Phishing Awareness": {
        "duration": "10 mins",
        "description": "How to spot and report phishing emails, suspicious links, and social engineering attacks.",
        "questions": [
            ("What should you do if you receive a suspicious email?", 
             ["Click the link to check if it's safe", "Report it to IT and delete it", "Forward it to colleagues", "Ignore it"],
             "Report it to IT and delete it"),
            ("Which of these is a sign of a phishing email?",
             ["It comes from your manager", "It has urgent language and asks for your password", "It has a company logo", "It arrives on Monday morning"],
             "It has urgent language and asks for your password"),
            ("What is social engineering?",
             ["Building software systems", "Manipulating people into revealing confidential information", "Network configuration", "Data backup"],
             "Manipulating people into revealing confidential information"),
        ]
    },
    "Password Security": {
        "duration": "8 mins",
        "description": "Best practices for creating and managing strong passwords across work accounts.",
        "questions": [
            ("What makes a strong password?",
             ["Your name and birth year", "A long mix of letters, numbers and symbols", "The word 'password'", "Your company name"],
             "A long mix of letters, numbers and symbols"),
            ("How often should you reuse passwords?",
             ["It's fine to reuse them", "Only reuse between personal accounts", "Never reuse passwords", "Reuse if they're strong enough"],
             "Never reuse passwords"),
            ("What is a password manager?",
             ["A person who manages passwords", "A tool that stores and generates strong passwords securely", "A type of antivirus", "A browser setting"],
             "A tool that stores and generates strong passwords securely"),
        ]
    },
    "Data Protection Basics": {
        "duration": "12 mins",
        "description": "Understanding GDPR, personal data handling, and your responsibilities as an employee.",
        "questions": [
            ("What is personal data?",
             ["Any data stored on a computer", "Information that can identify a living person", "Financial records only", "Company documents"],
             "Information that can identify a living person"),
            ("What should you do if you accidentally send personal data to the wrong person?",
             ["Hope nobody notices", "Report it to your data protection officer immediately", "Send an apology email", "Delete the sent email"],
             "Report it to your data protection officer immediately"),
            ("How long can you keep personal data?",
             ["Forever", "Only as long as necessary for its purpose", "10 years minimum", "Until the customer asks"],
             "Only as long as necessary for its purpose"),
        ]
    },
    "Device & Remote Working Security": {
        "duration": "10 mins",
        "description": "Keeping devices secure when working from home or in public places.",
        "questions": [
            ("What should you do before leaving your laptop unattended in a cafe?",
             ["Nothing, it's fine", "Lock the screen or shut it down", "Leave your bag next to it", "Log out of email only"],
             "Lock the screen or shut it down"),
            ("Is it safe to use public WiFi for work?",
             ["Yes, always", "Only for emails", "No, use a VPN or mobile hotspot instead", "Only if the cafe looks reputable"],
             "No, use a VPN or mobile hotspot instead"),
            ("What should you do if your work device is lost or stolen?",
             ["Buy a replacement and say nothing", "Report it to IT immediately", "Wait to see if it turns up", "Only report it if it had sensitive files"],
             "Report it to IT immediately"),
        ]
    }
}

if "completions" not in st.session_state:
    st.session_state.completions = {}

if "active_module" not in st.session_state:
    st.session_state.active_module = None

if "answers" not in st.session_state:
    st.session_state.answers = {}

employee_name = st.text_input("Your name", placeholder="e.g. Jane Smith")

if employee_name:
    st.divider()
    
    completed = [m for m in MODULES if f"{employee_name}_{m}" in st.session_state.completions]
    total = len(MODULES)
    pct = int((len(completed) / total) * 100)
    
    st.subheader(f"Training progress: {len(completed)}/{total} modules complete ({pct}%)")
    st.progress(pct / 100)
    
    st.divider()
    
    for module_name, module in MODULES.items():
        key = f"{employee_name}_{module_name}"
        is_complete = key in st.session_state.completions
        
        status = "✅ Complete" if is_complete else "⬜ Not started"
        
        with st.expander(f"{status} — {module_name} ({module['duration']})"):
            st.write(module['description'])
            
            if is_complete:
                completion = st.session_state.completions[key]
                st.success(f"Completed on {completion['date']} — Score: {completion['score']}/{len(module['questions'])}")
            else:
                st.write("**Knowledge check:**")
                q_answers = []
                all_answered = True
                
                for i, (question, options, correct) in enumerate(module['questions']):
                    answer = st.radio(
                        question,
                        options,
                        key=f"{key}_q{i}",
                        index=None
                    )
                    q_answers.append((answer, correct))
                    if answer is None:
                        all_answered = False
                
                if all_answered:
                    if st.button(f"Submit {module_name}", key=f"submit_{key}"):
                        score = sum(1 for a, c in q_answers if a == c)
                        if score == len(module['questions']):
                            st.session_state.completions[key] = {
                                "date": date.today().strftime("%d %B %Y"),
                                "score": score
                            }
                            st.success(f"Passed! {score}/{len(module['questions'])} correct. Module complete.")
                            st.rerun()
                        else:
                            st.error(f"{score}/{len(module['questions'])} correct. Review your answers and try again.")

    if len(completed) == total and employee_name:
        st.divider()
        st.success(f"🎉 {employee_name} has completed all training modules.")
        st.write(f"**Attestation:** I, {employee_name}, confirm I have completed all required security awareness training on {date.today().strftime('%d %B %Y')}.")
        if st.button("Sign attestation"):
            st.balloons()
            st.success("Attestation recorded.")