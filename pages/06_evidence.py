import streamlit as st
from datetime import date

st.set_page_config(page_title="Evidence Collection", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("Evidence Collection")
st.write("Upload and tag evidence to prove your compliance controls are working.")

CONTROLS = [
    "Firewall in place",
    "Default passwords changed",
    "Unnecessary software removed",
    "Admin access restricted",
    "Unique passwords per account",
    "Malware protection installed",
    "Patches applied within 14 days",
    "Supported OS in use",
    "Privacy notice in place",
    "Data encrypted",
    "Breach reporting process",
    "Retention policy in place",
    "Data processing agreements signed",
]

if "evidence" not in st.session_state:
    st.session_state.evidence = []

with st.form("evidence_form"):
    st.subheader("Upload evidence")
    control = st.selectbox("Which control does this evidence support?", CONTROLS)
    description = st.text_input("Description", placeholder="e.g. Screenshot of Windows Defender active on all devices")
    evidence_type = st.selectbox("Evidence type", [
        "Screenshot", "Policy document", "Configuration export",
        "Email confirmation", "Certificate", "Report", "Other"
    ])
    uploaded_file = st.file_uploader("Upload file", type=["png", "jpg", "pdf", "docx", "txt", "csv"])
    notes = st.text_area("Notes (optional)", placeholder="Any additional context...")
    submitted = st.form_submit_button("Save evidence")

    if submitted and uploaded_file and description:
        st.session_state.evidence.append({
            "control": control,
            "description": description,
            "type": evidence_type,
            "filename": uploaded_file.name,
            "date": date.today().strftime("%d %B %Y"),
            "notes": notes
        })
        st.success(f"Evidence saved for: {control}")

st.divider()
st.subheader("Your evidence library")

if not st.session_state.evidence:
    st.info("No evidence uploaded yet. Use the form above to start building your audit trail.")
else:
    for i, e in enumerate(st.session_state.evidence):
        with st.expander(f"📎 {e['control']} — {e['description']} ({e['date']})"):
            st.write(f"**Type:** {e['type']}")
            st.write(f"**File:** {e['filename']}")
            st.write(f"**Date added:** {e['date']}")
            if e['notes']:
                st.write(f"**Notes:** {e['notes']}")

    st.divider()
    controls_with_evidence = set(e['control'] for e in st.session_state.evidence)
    covered = len(controls_with_evidence)
    total = len(CONTROLS)
    pct = int((covered / total) * 100)
    st.subheader(f"Coverage: {covered}/{total} controls evidenced ({pct}%)")
    st.progress(pct / 100)

    st.subheader("Controls still needing evidence:")
    for c in CONTROLS:
        if c not in controls_with_evidence:
            st.write(f"❌ {c}")
        else:
            st.write(f"✅ {c}")