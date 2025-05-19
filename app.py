import streamlit as st

st.set_page_config(page_title="HC Deployment Calculator", page_icon="📊", layout="centered")

# Custom CSS for the whole app
st.markdown(
    """
    <style>
    /* Background gradient for header */
    .header {
        background: linear-gradient(90deg, #4f46e5, #3b82f6);
        padding: 25px 0;
        text-align: center;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
        margin-bottom: 40px;
        user-select: none;
    }

    /* Center all content */
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Styled input box */
    .stNumberInput>div>div>input {
        font-size: 1.25rem;
        padding: 12px 15px;
        border-radius: 10px;
        border: 2px solid #3b82f6;
        transition: border-color 0.3s ease;
    }
    .stNumberInput>div>div>input:focus {
        border-color: #4f46e5;
        outline: none;
    }

    /* Card styling */
    .card {
        background: #1e3a8a;  /* Dark blue */
        color: white;
        border-radius: 15px;
        padding: 30px 40px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(30, 58, 138, 0.5);
        max-width: 450px;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: default;
        user-select: none;
    }
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(30, 58, 138, 0.8);
    }
    .card h2 {
        margin: 0 0 15px 0;
        color: #a5b4fc;  /* lighter blue */
        font-size: 2.3rem;
    }
    .card p {
        font-size: 1.25rem;
        margin: 8px 0;
        font-weight: 500;
    }
    .result-value {
        font-size: 3rem;
        font-weight: 900;
        margin: 15px 0 25px 0;
        color: #facc15; /* amber/yellow for highlight */
        letter-spacing: 1.5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header">HC Deployment Calculator for Inbound</div>', unsafe_allow_html=True)

# Main content container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

daily_volume = st.number_input(
    "Enter the inbound volume for the day",
    min_value=0,
    step=1,
    help="Input the total number of inbound volumes expected today.",
)

aa_bm_rate_per_hour = 21
shift_hours = 9
aa_bm_rate_shift = aa_bm_rate_per_hour * 60 * shift_hours  # 11,340

if daily_volume > 0:
    volume_per_shift = daily_volume / 2
    hc_per_shift = volume_per_shift / aa_bm_rate_shift

    card_html = f"""
    <div class="card">
        <h2>Ideal HC per Shift</h2>
        <div class="result-value">{hc_per_shift:.2f}</div>
        <p>Volume per shift: <strong>{volume_per_shift:.2f}</strong></p>
        <p>AA BM rate per shift: <strong>{aa_bm_rate_shift}</strong></p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
else:
    st.info("Please enter a valid volume greater than 0 to see results.")

st.markdown('</div>', unsafe_allow_html=True)
