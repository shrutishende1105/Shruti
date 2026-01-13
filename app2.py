import streamlit as st

st.title("some basic comands like slider button etc")
age=st.slider("enter your age",1,100)
city=st.selectbox("select your city",["new york","los angeles","chicago","houston","phoenix"])
if st.button("submit"):
    st.write("your age is", age)
    st.write("your city is", city)