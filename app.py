import streamlit as st

st.title("salary prediction")

experience=st.number_input("enter the years of experience")

experience=experience*10000

if st.button("predict"):
	st.write("predicted salary:", int(experience))


name=st.text_input("enter your name")
if st.button("submit"):
	st.success(f"welcome,{name}")

