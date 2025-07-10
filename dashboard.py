import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Internship Dashboard", layout="wide")
st.title("📊 Internship Dashboard (Internshala)")

try:
    df = pd.read_csv("internshala_jobs.csv")
except FileNotFoundError:
    st.error("⚠️ 'internshala_jobs.csv' not found.")
    st.stop()

locations = df["Location"].dropna().astype(str).unique().tolist()
location = st.sidebar.selectbox("📍 Filter by Location", ["All"] + sorted(locations))

if location != "All":
    df = df[df["Location"] == location]

def parse_stipend(val):
    try:
        if isinstance(val, str) and "₹" in val:
            return int(val.replace("₹", "").replace(",", "").split("/")[0].strip())
    except:
        return None
    return None

df["Parsed Stipend"] = df["Stipend"].apply(parse_stipend)

st.sidebar.markdown("## 💰 Stipend Filter")

if df["Parsed Stipend"].notna().any():
    min_stipend = int(df["Parsed Stipend"].min())
    max_stipend = int(df["Parsed Stipend"].max())
    if min_stipend == max_stipend:
        max_stipend += 1000

    stipend_filter = st.sidebar.slider("Minimum Stipend (INR)", min_stipend, max_stipend, min_stipend, step=500)
    df = df[df["Parsed Stipend"] >= stipend_filter]
else:
    st.sidebar.warning("No valid stipend data found.")
    stipend_filter = None

st.subheader("📄 Internship Listings")
st.dataframe(df.reset_index(drop=True))

st.subheader("📍 Top Internship Locations")
locs = df["Location"].value_counts().head(10)
st.bar_chart(locs)

if stipend_filter is not None and not df["Parsed Stipend"].dropna().empty:
    st.subheader("💰 Stipend Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Parsed Stipend"].dropna(), bins=15, kde=True, ax=ax)
    st.pyplot(fig)
else:
    st.warning("No stipend data available to plot distribution.")