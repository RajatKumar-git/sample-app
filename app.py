import streamlit as st
st.title('AT Traveller App')
destination=st.text_input("Enter destination: ")
travel_date=st.date_input("Enter the travel Date:")
budget=st.number_input(input("Enter budget:"))
hotel_required=st.selectbox("Do you need hotel stay",("Yes","No"))

if st.button("submit"):
    st.write(print(f"""
    AI Travel Agent Summary
    -----------------------
    Destination \t: {destination}
    Travel Date \t: {travel_date}
    Budget  \t: {budget}
    Hotel_Required \t: {hotel_required}"""))
st.balloons()
