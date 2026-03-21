import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Continuous Monitoring", page_icon="🔒", layout="wide", initial_sidebar_state="expanded")

st.title("Continuous Monitoring")
st.write("Track your compliance status across all frameworks in real time.")

if "monitoring" not in st.session_state:
    st.session_state.monitoring = {
        "Cyber Essentials": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "GDPR Assessment": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "ISO 27001": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "Penetration Test": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "Staff Training": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "Policy Review": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "Backup Testing": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
        "Incident Response Test": {"status": "Unknown", "last_reviewed": None, "expiry": None, "notes": ""},
    }

STATUS_COLORS = {
    "Compliant": "✅",
    "Expiring Soon": "🟡",
    "Overdue": "🔴",
    "Unknown": "⚪"
}

today = date.today()
alerts = []

col1, col2, col3, col4 = st.columns(4)
compliant = sum(1 for v in st.session_state.monitoring.values() if v["status"] == "Compliant")
expiring = sum(1 for v in st.session_state.monitoring.values() if v["status"] == "Expiring Soon")
overdue = sum(1 for v in st.session_state.monitoring.values() if v["status"] == "Overdue")
unknown = sum(1 for v in st.session_state.monitoring.values() if v["status"] == "Unknown")

with col1:
    st.metric("Compliant", compliant)
with col2:
    st.metric("Expiring Soon", expiring)
with col3:
    st.metric("Overdue", overdue)
with col4:
    st.metric("Unknown", unknown)

st.divider()

for control, data in st.session_state.monitoring.items():
    with st.expander(f"{STATUS_COLORS[data['status']]} {control} — {data['status']}"):
        col1, col2 = st.columns(2)
        
        with col1:
            status = st.selectbox(
                "Status",
                ["Unknown", "Compliant", "Expiring Soon", "Overdue"],
                index=["Unknown", "Compliant", "Expiring Soon", "Overdue"].index(data["status"]),
                key=f"status_{control}"
            )
            last_reviewed = st.date_input(
                "Last reviewed",
                value=data["last_reviewed"] or today,
                key=f"reviewed_{control}"
            )
        
        with col2:
            expiry = st.date_input(
                "Next review / expiry date",
                value=data["expiry"] or (today + timedelta(days=365)),
                key=f"expiry_{control}"
            )
            notes = st.text_input(
                "Notes",
                value=data["notes"],
                key=f"notes_{control}"
            )
        
        if st.button(f"Save {control}", key=f"save_{control}"):
            st.session_state.monitoring[control] = {
                "status": status,
                "last_reviewed": last_reviewed,
                "expiry": expiry,
                "notes": notes
            }
            if expiry and (expiry - today).days <= 30:
                alerts.append(f"⚠️ {control} expires in {(expiry - today).days} days")
            st.success("Saved.")
            st.rerun()

if alerts:
    st.divider()
    st.subheader("Alerts")
    for alert in alerts:
        st.warning(alert)