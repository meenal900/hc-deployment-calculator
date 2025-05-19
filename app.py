import streamlit as st

st.title("HC Deployment Calculator for Inbound")

# Input daily volume
daily_volume = st.number_input("Enter the inbound volume for the day", min_value=0, step=1)

# Constants
aa_bm_rate_per_hour = 21
shift_hours = 9
aa_bm_rate_shift = aa_bm_rate_per_hour * 60 * shift_hours  # total volume one AA can process in one shift

if daily_volume > 0:
    volume_per_shift = daily_volume / 2
    hc_per_shift = volume_per_shift / aa_bm_rate_shift

    st.write(f"## Results")
    st.write(f"Volume per shift: {volume_per_shift:.2f}")
    st.write(f"AA BM rate per shift (volume processed by 1 AA): {aa_bm_rate_shift}")
    st.write(f"**Ideal Headcount (HC) to deploy per shift:** {hc_per_shift:.2f}")
else:
    st.write("Please enter a valid volume greater than 0.")
