import streamlit as st

st.set_page_config(page_title="HC Deployment Calculator", layout="centered")

st.markdown(
    """
    <style>
    /* Page background and font */
    body {
        background-color: #f9fafb;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        color: #333333;
    }

    /* Plain static header, no animation, no hover */
    .header {
        font-size: 2.5rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 2.5rem;
        color: #1f2937; /* dark slate */
        user-select: none;
        /* No hover or animation */
    }

    /* Input box styling */
    .stNumberInput>div>div>input {
        font-size: 1.1rem;
        padding: 8px 12px;
        border-radius: 5px;
        border: 1.5px solid #9ca3af;
        transition: border-color 0.2s ease;
    }
    .stNumberInput>div>div>input:focus {
        border-color: #2563eb;
        outline: none;
    }

    /* Card with animation & hover */
    .card {
        background: #ffffff;
        color: #1f2937;
        border-radius: 8px;
        padding: 25px 30px;
        margin: 2rem auto;
        max-width: 420px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        user-select: none;

        /* Animation */
        opacity: 0;
        transform: translateY(20px);
        animation: fadeSlideUp 0.6s forwards;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: default;
    }
    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }

    @keyframes fadeSlideUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .card h2 {
        margin-bottom: 1rem;
        font-weight: 700;
        font-size: 1.75rem;
        color: #2563eb;
    }
    .card p {
        font-size: 1.1rem;
        margin: 0.5rem 0;
    }

    /* Ideal HC result style and hover */
    .result-value {
        font-size: 2.75rem;
        font-weight: 800;
        margin: 1rem 0 1.5rem 0;
        color: #111827;
        transition: color 0.3s ease, transform 0.3s ease;
        display: inline-block;
    }
    .result-value:hover {
        color: #2563eb; /* blue highlight */
        transform: scale(1.1);
        cursor: default;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Plain header with no animation or hover
st.markdown('<div class="header">HC Deployment Calculator for Inbound</div>', unsafe_allow_html=True)

daily_volume = st.number_input(
    "Enter the inbound volume for the day:",
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
        <h2>Ideal Headcount per Shift</h2>
        <div class="result-value">{hc_per_shift:.2f}</div>
        <p>Volume per shift: <strong>{volume_per_shift:.2f}</strong></p>
        <p>AA BM rate per shift: <strong>{aa_bm_rate_shift}</strong></p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
else:
    st.info("Please enter a valid volume greater than 0 to see results.")
