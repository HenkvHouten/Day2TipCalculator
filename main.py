import streamlit as st

st.title("Bill Calculator")

with st.form(key="bill_calculator_form"):
    bill = st.number_input("What was the total bill? EUR ", min_value=0.0, step=1.0)
    tip = st.number_input("How much tip would you like to give? 10, 12, or 15? ", min_value=0, step=1)
    group = st.number_input("How many people to split the bill? ", min_value=1, step=1)

    submit_button = st.form_submit_button(label="Calculate")

if submit_button:
    calculated_tip = bill * (tip / 100)
    total_bill = bill + calculated_tip
    bill_per_person = round(total_bill / group, 2)

    st.success(f"Each person should pay: EUR {bill_per_person}")