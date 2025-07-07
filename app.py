
import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Pencarian Data Mesin", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("Data_Mesin.xlsx")

df = load_data()

# Custom CSS for enhanced visual design
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
                     Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        background: linear-gradient(to bottom right, #f2f2f7, #ffffff);
        color: #1d1d1f;
    }
    .stTextInput>div>div>input {
        padding: 1rem;
        font-size: 1.2rem;
        border: 1px solid #c7c7cc;
        border-radius: 12px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stDataFrame {
        border-radius: 12px;
        background-color: white;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Pencarian Data Mesin")

# Search bar
query = st.text_input("Masukkan kata kunci (nama mesin, lokasi, serial number, dll):", "")

# Filter data
if query:
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    st.write(f"Hasil pencarian untuk: **{query}**")
else:
    results = df
    st.write("Menampilkan semua data. Silakan masukkan kata kunci untuk memfilter hasil.")

# Show dataframe
st.dataframe(results, use_container_width=True)
