import streamlit as st

st.title("HC Deployment Calculator for Inbound")

daily_volume = st.number_input("Enter the inbound volume for the day", min_value=0, step=1)

aa_bm_rate_per_hour = 21
shift_hours = 9
aa_bm_rate_shift = aa_bm_rate_per_hour * 60 * shift_hours  # 11,340

if daily_volume > 0:
    volume_per_shift = daily_volume / 2
    hc_per_shift = volume_per_shift / aa_bm_rate_shift

    # Custom CSS for card and hover effect
    card_style = """
    <style>
    .card {
        background: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        max-width: 400px;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .card h2 {
        margin: 0;
        color: #4a90e2;
    }
    </style>
    """

    card_html = f"""
    <div class="card">
        <h2>Ideal HC per shift</h2>
        <p style="font-size: 2em; font-weight: bold; margin: 10px 0;">{hc_per_shift:.2f}</p>
        <p>Volume per shift: {volume_per_shift:.2f}</p>
        <p>AA BM rate per shift: {aa_bm_rate_shift}</p>
    </div>
    """

    st.markdown(card_style + card_html, unsafe_allow_html=True)

else:
    st.write("Please enter a valid volume greater than 0.")
