import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Cleaner Lite", layout="wide")
st.title("CSV Cleaner Lite")
st.write("Upload a CSV file and clean your data in one click.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Original Data Preview")
    st.dataframe(df.head())

    st.subheader("Quick Stats")
    st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
    st.write(f"Missing values: {df.isnull().sum().sum()}")

    st.subheader("Clean Options")
    drop_duplicates = st.checkbox("Remove duplicate rows")
    drop_na = st.checkbox("Drop rows with missing values")
    normalize_columns = st.checkbox("Normalize column headers (lowercase + underscores)")

    if st.button("Clean My Data"):
        if drop_duplicates:
            df = df.drop_duplicates()
        if drop_na:
            df = df.dropna()
        if normalize_columns:
            df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        st.success("Data cleaned!")
        st.dataframe(df.head())

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Cleaned CSV", data=csv, file_name="cleaned.csv", mime="text/csv")
