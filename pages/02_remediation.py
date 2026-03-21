import streamlit as st

st.set_page_config(page_title="Remediation Plan", page_icon="🔒", layout="wide")

st.title("Remediation Plan")
st.write("Based on your assessment, here is your prioritised action plan.")

REMEDIATIONS = {
    "Firewall in place": {
        "priority": "Critical",
        "effort": "Low",
        "steps": [
            "Enable the built-in firewall on your router (usually in admin settings at 192.168.1.1)",
            "Ensure all office devices have their local firewall turned on",
            "Consider a business-grade router with firewall built in (e.g. Ubiquiti, Cisco Meraki)"
        ],
        "why": "A firewall is the first line of defence against external attacks. Without one, your network is directly exposed to the internet."
    },
    "Default passwords changed on network devices": {
        "priority": "Critical",
        "effort": "Low",
        "steps": [
            "Log into your router admin panel (usually 192.168.1.1 or 192.168.0.1)",
            "Change the admin password to something unique and strong",
            "Do the same for any switches, access points, or other network hardware"
        ],
        "why": "Default passwords are publicly known and are the first thing attackers try."
    },
    "Unnecessary software removed": {
        "priority": "Medium",
        "effort": "Medium",
        "steps": [
            "Audit all software installed on company devices",
            "Uninstall anything not actively used",
            "Disable browser extensions that aren't needed"
        ],
        "why": "Every piece of software is a potential attack surface. Less software means fewer vulnerabilities."
    },
    "Default credentials changed on devices": {
        "priority": "Critical",
        "effort": "Low",
        "steps": [
            "Change default usernames and passwords on all devices before deployment",
            "Create an inventory of all devices and confirm credentials have been changed",
            "Use a password manager to store unique credentials for each device"
        ],
        "why": "Attackers scan for devices using default credentials automatically."
    },
    "Admin access restricted": {
        "priority": "High",
        "effort": "Medium",
        "steps": [
            "Audit who has admin accounts across all systems",
            "Remove admin rights from anyone who doesn't strictly need them",
            "Create standard user accounts for day-to-day work, even for IT staff"
        ],
        "why": "If an admin account is compromised, the attacker gets full control. Limiting admin accounts limits damage."
    },
    "Unique passwords per account": {
        "priority": "High",
        "effort": "Low",
        "steps": [
            "Roll out a password manager (Bitwarden is free, 1Password is popular for teams)",
            "Require all staff to use unique passwords for every account",
            "Enable multi-factor authentication (MFA) on all critical accounts"
        ],
        "why": "Reused passwords mean one breach exposes all your accounts."
    },
    "Malware protection installed": {
        "priority": "High",
        "effort": "Low",
        "steps": [
            "Install antivirus on all Windows and Mac devices (Windows Defender is free and sufficient)",
            "Ensure mobile devices used for work also have protection",
            "Consider a centralised endpoint protection tool for easier management"
        ],
        "why": "Malware can steal data, encrypt files for ransom, or give attackers remote access."
    },
    "Malware protection auto-updated": {
        "priority": "Medium",
        "effort": "Low",
        "steps": [
            "Check antivirus settings and enable automatic updates",
            "Verify updates are actually happening by checking the last update date",
            "Set up alerts if protection goes out of date"
        ],
        "why": "Outdated malware protection can't detect new threats."
    },
    "Patches applied within 14 days": {
        "priority": "High",
        "effort": "Medium",
        "steps": [
            "Enable automatic updates on all operating systems",
            "Set a monthly patch review meeting to catch anything missed",
            "Prioritise patches marked Critical or High severity"
        ],
        "why": "Most successful attacks exploit known vulnerabilities that already have patches available."
    },
    "Supported OS in use": {
        "priority": "Critical",
        "effort": "High",
        "steps": [
            "Identify any devices running Windows 7, Windows 8, or other end-of-life OS",
            "Upgrade to Windows 11 or Windows 10 at minimum",
            "If hardware can't support the upgrade, replace the device"
        ],
        "why": "Unsupported operating systems no longer receive security patches, leaving known vulnerabilities permanently open."
    }
}

PRIORITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
PRIORITY_COLORS = {
    "Critical": "error",
    "High": "warning", 
    "Medium": "info",
    "Low": "success"
}

if "gaps" not in st.session_state or not st.session_state.gaps:
    st.warning("No gaps found. Please complete the Cyber Essentials assessment first.")
    st.stop()

gaps = st.session_state.gaps
sorted_gaps = sorted(gaps, key=lambda x: PRIORITY_ORDER.get(REMEDIATIONS[x]["priority"], 99))

st.subheader(f"You have {len(gaps)} items to fix")

critical = [g for g in gaps if REMEDIATIONS[g]["priority"] == "Critical"]
high = [g for g in gaps if REMEDIATIONS[g]["priority"] == "High"]
medium = [g for g in gaps if REMEDIATIONS[g]["priority"] == "Medium"]

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Critical", len(critical))
with col2:
    st.metric("High", len(high))
with col3:
    st.metric("Medium", len(medium))

st.divider()

for gap in sorted_gaps:
    r = REMEDIATIONS[gap]
    with st.expander(f"{'🔴' if r['priority'] == 'Critical' else '🟠' if r['priority'] == 'High' else '🟡'} {gap} — {r['priority']} priority | Effort: {r['effort']}"):
        st.write(f"**Why this matters:** {r['why']}")
        st.write("**Steps to fix:**")
        for i, step in enumerate(r['steps'], 1):
            st.write(f"{i}. {step}")