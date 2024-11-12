import streamlit as st 
import pandas as pd


st.header("Streamlit Core Features")
st.subheader("Text Elements")
st.text("This is a simple text element.")

# Data display
st.subheader("Data Display")
st.write("Here is a simple table:")

df = pd.DataFrame({
    "Date": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "Amount": [120, 360, 765]
})

st.table(df)

st.bar_chart(df)

st.table({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})

# Charts
st.subheader("Charts")
st.line_chart([1,2,3,4])

st.title("Interactive wedgets Example")

# Checkbox
if st.checkbox("Show/Text"):
    st.write("Checkbox is checked!")
    
# Selectbox
option = st.selectbox("Category", ["Rent", "Food"], label_visibility="collapsed")
st.write(f"You selected: {option}")

# Multiselect
options = st.multiselect("Select multiple numbers", [1, 2, 3, 4, 5])
st.write(f"You selected: {options}")