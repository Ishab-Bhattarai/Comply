import streamlit as st

st.set_page_config(page_title="Pricing – Comply", page_icon="💷", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&display=swap');

* { font-family: 'Syne', sans-serif; }

.pricing-header {
    text-align: center;
    padding: 3rem 0 2rem;
}
.pricing-header h1 {
    font-size: 3.2rem;
    font-weight: 800;
    color: #f5c518;
    letter-spacing: -1px;
    margin-bottom: 0.5rem;
}
.pricing-header p {
    color: #aaa;
    font-size: 1.1rem;
}

.plan-card {
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-radius: 12px;
    padding: 2rem;
    height: 100%;
    position: relative;
    transition: border-color 0.2s;
}
.plan-card.featured {
    border-color: #f5c518;
    background: #1e1c0f;
}
.plan-card .badge {
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    background: #f5c518;
    color: #000;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 3px 14px;
    border-radius: 20px;
    text-transform: uppercase;
}
.plan-name {
    font-size: 1.1rem;
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}
.plan-price {
    font-family: 'DM Mono', monospace;
    font-size: 2.8rem;
    font-weight: 500;
    color: #f5c518;
    line-height: 1;
    margin-bottom: 0.2rem;
}
.plan-price span {
    font-size: 1rem;
    color: #888;
}
.plan-desc {
    color: #888;
    font-size: 0.85rem;
    margin-bottom: 1.5rem;
    min-height: 2.5rem;
}
.feature-list {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem;
}
.feature-list li {
    color: #ccc;
    font-size: 0.9rem;
    padding: 0.4rem 0;
    border-bottom: 1px solid #2a2a2a;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.feature-list li .check { color: #f5c518; }
.feature-list li .cross { color: #555; }

.cta-free {
    display: block;
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #444;
    border-radius: 8px;
    background: transparent;
    color: #aaa;
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    text-align: center;
    cursor: pointer;
    text-decoration: none;
}
.cta-paid {
    display: block;
    width: 100%;
    padding: 0.75rem;
    border: none;
    border-radius: 8px;
    background: #f5c518;
    color: #000;
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 800;
    text-align: center;
    cursor: pointer;
    text-decoration: none;
}

.faq-section {
    max-width: 680px;
    margin: 4rem auto 2rem;
}
.faq-section h2 {
    color: #f5c518;
    font-size: 1.6rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    text-align: center;
}
.faq-item {
    border-bottom: 1px solid #2a2a2a;
    padding: 1rem 0;
}
.faq-q { color: #fff; font-weight: 700; font-size: 0.95rem; }
.faq-a { color: #888; font-size: 0.88rem; margin-top: 0.4rem; }

.guarantee {
    text-align: center;
    color: #666;
    font-size: 0.85rem;
    margin-top: 3rem;
    padding-bottom: 2rem;
}
.guarantee strong { color: #f5c518; }
</style>

<div class="pricing-header">
    <h1>Simple, honest pricing.</h1>
    <p>No hidden fees. Cancel anytime. Start free.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="plan-card">
        <div class="plan-name">Free</div>
        <div class="plan-price">£0 <span>/mo</span></div>
        <div class="plan-desc">See where you stand. No card required.</div>
        <ul class="feature-list">
            <li><span class="check">✓</span> Cyber Essentials gap assessment</li>
            <li><span class="check">✓</span> Instant compliance score</li>
            <li><span class="check">✓</span> Gap summary report</li>
            <li><span class="cross">✗</span> Remediation plan</li>
            <li><span class="cross">✗</span> Policy templates</li>
            <li><span class="cross">✗</span> Evidence tracker</li>
            <li><span class="cross">✗</span> Trust portal</li>
        </ul>
        <a href="/assessment" class="cta-free">Start free assessment →</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="plan-card featured">
        <div class="badge">Most popular</div>
        <div class="plan-name">Essentials</div>
        <div class="plan-price">£49 <span>/mo</span></div>
        <div class="plan-desc">Everything you need to pass Cyber Essentials.</div>
        <ul class="feature-list">
            <li><span class="check">✓</span> Everything in Free</li>
            <li><span class="check">✓</span> Full remediation plan</li>
            <li><span class="check">✓</span> Policy templates (GDPR, AUP, more)</li>
            <li><span class="check">✓</span> Evidence tracker</li>
            <li><span class="check">✓</span> GDPR compliance module</li>
            <li><span class="cross">✗</span> Trust portal</li>
            <li><span class="cross">✗</span> Staff training module</li>
        </ul>
        <a href="mailto:ishab.bhattarai@gmail.com?subject=Comply Essentials Plan" class="cta-paid">Get started — £49/mo</a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="plan-card">
        <div class="plan-name">Pro</div>
        <div class="plan-price">£149 <span>/mo</span></div>
        <div class="plan-desc">For businesses serious about certification.</div>
        <ul class="feature-list">
            <li><span class="check">✓</span> Everything in Essentials</li>
            <li><span class="check">✓</span> Public trust portal</li>
            <li><span class="check">✓</span> Staff security training</li>
            <li><span class="check">✓</span> Continuous monitoring</li>
            <li><span class="check">✓</span> Multi-framework support</li>
            <li><span class="check">✓</span> Priority support</li>
            <li><span class="check">✓</span> Audit-ready exports</li>
        </ul>
        <a href="mailto:ishab.bhattarai@gmail.com?subject=Comply Pro Plan" class="cta-paid">Get started — £149/mo</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="faq-section">
    <h2>Common questions</h2>
    <div class="faq-item">
        <div class="faq-q">Do I need a credit card to start?</div>
        <div class="faq-a">No. The free plan requires no payment details at all.</div>
    </div>
    <div class="faq-item">
        <div class="faq-q">What is Cyber Essentials?</div>
        <div class="faq-a">A UK government-backed certification that proves your business is protected against common cyber threats. Many contracts and tenders now require it.</div>
    </div>
    <div class="faq-item">
        <div class="faq-q">Can I cancel anytime?</div>
        <div class="faq-a">Yes. No lock-in, no cancellation fees. Cancel from your account at any time.</div>
    </div>
    <div class="faq-item">
        <div class="faq-q">I'm not sure which plan is right for me.</div>
        <div class="faq-a">Start with the free assessment — it'll show your gaps and make the right plan obvious.</div>
    </div>
</div>

<div class="guarantee">
    <strong>30-day money-back guarantee.</strong> If Comply doesn't help your business, we'll refund you. No questions asked.
</div>
""", unsafe_allow_html=True)