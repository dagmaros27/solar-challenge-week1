import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """Load dataset from a given CSV path."""
    return pd.read_csv(path, parse_dates=["Timestamp"])

def plot_ghi_distribution(data: pd.DataFrame, country_name: str):
    """Plot histogram of GHI for a given country."""
    fig, ax = plt.subplots()
    sns.histplot(data["GHI"], kde=True, ax=ax, bins=30)
    ax.set_title(f'GHI Distribution in {country_name}')
    ax.set_xlabel('GHI (W/m²)')
    ax.set_ylabel('Frequency')
    return fig

def plot_country_comparison(dfs: dict):
    """Create a boxplot comparing GHI across countries."""
    all_data = pd.concat(
        [df.assign(Country=name) for name, df in dfs.items()],
        axis=0
    )
    fig, ax = plt.subplots()
    sns.boxplot(x="Country", y="GHI", data=all_data, ax=ax)
    ax.set_title("GHI Comparison Across Countries")
    return fig

def display_metrics(df: pd.DataFrame):
    """Display mean, median, and standard deviation for GHI, DNI, and DHI."""
    metrics = df[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"]).T
    st.dataframe(metrics.style.format("{:.2f}"))
