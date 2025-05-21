import streamlit as st
from utils import load_data, plot_ghi_distribution, plot_country_comparison, display_metrics
import os

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")
st.title("☀️ MoonLight Energy Solutions - Solar Data Insights")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COUNTRY_PATHS = {
    "Benin": os.path.join(BASE_DIR, "../data/benin_clean.csv"),
    "Sierra Leone": os.path.join(BASE_DIR, "../data/sierraleone_clean.csv"),
    "Togo": os.path.join(BASE_DIR, "../data/togo_clean.csv")
}

# Sidebar selection
st.sidebar.header("Settings")
country_selection = st.sidebar.multiselect("Select countries to view", list(COUNTRY_PATHS.keys()), default=list(COUNTRY_PATHS.keys()))

# Load data
dataframes = {name: load_data(path) for name, path in COUNTRY_PATHS.items() if name in country_selection}

# Section 1: Distribution plots
st.header("🌍 GHI Distribution by Country")
for country, df in dataframes.items():
    st.pyplot(plot_ghi_distribution(df, country))

# Section 2: Comparison boxplot
if len(dataframes) > 1:
    st.header("📊 GHI Comparison")
    st.pyplot(plot_country_comparison(dataframes))

# Section 3: Summary Statistics
st.header("📈 Summary Statistics")
for country, df in dataframes.items():
    st.subheader(f"{country}")
    display_metrics(df)


# Footer
st.markdown("""
---
Developed for MoonLight Energy Solutions | Challenge Week 1
""")