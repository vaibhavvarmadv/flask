from flask import Flask, render_template, request
import streamlit as st

def praxis():
    st.title("Learning StreamLit")

    name = st.text_input('Student Name', 'Type Here')
    num = st.text_input('Roll No', 'Type Here')

    result =""
    if st.button("Print Result"):
        st.success(f"The Student Name is {name} with number {num}")

if __name__ == "__main__":
    praxis()