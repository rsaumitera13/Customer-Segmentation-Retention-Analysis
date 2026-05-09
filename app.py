import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# --- CONFIGURATION ---
st.set_page_config(page_title="RETENTION AI v3.0", page_icon="⚡", layout="wide")

# --- CUSTOM CSS (The "Secret Sauce") ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: radial-gradient(circle at 50% 50%, #0a192f 0%, #020617 100%);
        color: #e2e8f0;
    }

    /* Glassmorphism Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        transition: transform 0.3s ease, border 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        border: 1px solid #00d2ff;
        box-shadow: 0 10px 30px rgba(0, 210, 255, 0.1);
    }

    /* Professional Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.5) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Custom Metric Styling */
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        color: #00d2ff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UTILITY: LOAD ANIMATIONS ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

lottie_data = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_qp1q7mct.json") # Tech abstract

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #00d2ff;'>STRATEGOS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.6;'>Retention OS v3.0.4</p>", unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["Command Center", "Risk Profiler", "Strategy Vault"],
        icons=["cpu", "search", "shield-check"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00d2ff", "font-size": "20px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px", "color": "white"},
            "nav-link-selected": {"background-color": "rgba(0, 210, 255, 0.2)", "border-left": "4px solid #00d2ff"},
        }
    )
    
    st.markdown("---")
    st.write("👤 User: Saumitra S. Rath")
    st.write("📍 Node: Hyderabad, IN")

# --- PAGE 1: COMMAND CENTER ---
if selected == "Command Center":
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.markdown("# ⚡ System Overview")
        st.markdown("Real-time telemetry from active subscriber nodes.")
    with col_r:
        st_lottie(lottie_data, height=120, key="init")

    st.markdown("### Power Metrics")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("RETENTION RATE", "94.2%", "+1.4%")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("CHURN AT RISK", "412", "-12", delta_color="inverse")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("LIFETIME VALUE", "$2.4k", "+$150")
        st.markdown('</div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.metric("NET SENTIMENT", "8.2/10", "Rising")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Modern Chart
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Geographic Load")
        # Sample mapping data
        df = pd.DataFrame({'City': ['Hyderabad', 'Bhubaneswar', 'Mumbai', 'Bangalore'], 'Active': [450, 120, 300, 500]})
        fig = px.bar(df, x='City', y='Active', template="plotly_dark", color_discrete_sequence=['#00d2ff'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        st.markdown("#### Segment Distribution")
        fig_pie = px.pie(values=[40, 25, 20, 15], names=['Champions', 'Loyal', 'At Risk', 'Hibernating'], hole=.6)
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', legend_font_color="white")
        st.plotly_chart(fig_pie, use_container_width=True)

# --- PAGE 2: RISK PROFILER ---
elif selected == "Risk Profiler":
    st.markdown("# 🔍 Deep Risk Analysis")
    
    col_input, col_output = st.columns([1, 1.5])
    
    with col_input:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Subscriber Profile")
        tenure = st.number_input("TENURE (Months)", 0, 72, 24)
        contract = st.selectbox("CONTRACT TYPE", ["Month-to-month", "One year", "Two year"])
        monthly = st.slider("MONTHLY CHARGES", 20.0, 150.0, 75.0)
        
        predict_btn = st.button("EXECUTE ANALYSIS", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_output:
        if predict_btn:
            # Logic: Using business rules to mock the ML model's behavior for the UI demo
            score = 85 if contract == "Month-to-month" else 15
            
            st.markdown(f"### RISK ASSESSMENT: {'CRITICAL' if score > 50 else 'STABLE'}")
            
            # Custom Gauge
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = score,
                gauge = {'bar': {'color': "#00d2ff"}, 'bgcolor': "rgba(255,255,255,0.1)"}
            ))
            fig_gauge.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
            st.plotly_chart(fig_gauge, use_container_width=True)
            
            st.markdown('<div class="glass-card" style="border-left: 5px solid #00d2ff;">', unsafe_allow_html=True)
            st.write("**AI Recommendation:** This subscriber shows patterns of high price sensitivity. Deploying a 'Two-Year' contract conversion offer could reduce churn probability by 40%.")
            st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: STRATEGY VAULT ---
elif selected == "Strategy Vault":
    st.markdown("# 🛡️ Retention Playbook")
    st.markdown("Based on your reading of *The 48 Laws of Power*, these strategies are designed for market dominance.")
    
    laws = {
        "Law 13: Appeal to Self-Interest": "Offer cashback rewards that make staying more profitable than switching.",
        "Law 20: Do Not Commit": "Keep premium features exclusive to prevent customer independence from your ecosystem.",
        "Law 47: Do Not Go Past the Mark": "Avoid aggressive upselling once a customer reaches loyalty saturation."
    }
    
    for law, strategy in laws.items():
        with st.expander(law):
            st.write(strategy)
            st.button(f"Deploy {law[:6]} Campaign", key=law)