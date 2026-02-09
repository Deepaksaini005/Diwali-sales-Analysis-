import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Diwali Sales Dashboard",
    page_icon="🪔",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.block-container {
    padding-top: 2rem;
}
.metric-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.section {
    background: rgba(255, 255, 255, 0.06);
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 25px;
}
h1, h2, h3 {
    color: #f8fafc;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATA LOAD ----------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        r"C:\Users\saini\Downloads\Diwali Sales Data.csv",
        encoding="unicode_escape"
    )
    df.drop(columns=["Status", "unnamed1"], inplace=True)
    df.dropna(subset=["Amount"], inplace=True)
    df.rename(columns={"Amount": "Sales Amount"}, inplace=True)
    df["Sales Amount"] = df["Sales Amount"].astype(int)
    return df

data = load_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🎛 Filters")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=data["Gender"].unique(),
    default=data["Gender"].unique()
)

state_filter = st.sidebar.multiselect(
    "Select State",
    options=data["State"].unique(),
    default=data["State"].unique()
)

filtered_data = data[
    (data["Gender"].isin(gender_filter)) &
    (data["State"].isin(state_filter))
]

# ---------------- TITLE ----------------
st.title("🪔 Diwali Sales Dashboard")
st.caption("Modern • Clean • Business Ready")

# ---------------- KPI CARDS ----------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>💰 Total Sales</h3>
        <h2>₹ {filtered_data['Sales Amount'].sum():,}</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <h3>🧾 Orders</h3>
        <h2>{filtered_data.shape[0]}</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <h3>👥 Customers</h3>
        <h2>{filtered_data['User_ID'].nunique()}</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <h3>📦 Avg Order</h3>
        <h2>₹ {int(filtered_data['Sales Amount'].mean())}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- GENDER DISTRIBUTION ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("👫 Gender Distribution")

fig, ax = plt.subplots()
gender_count = filtered_data["Gender"].value_counts()
sns.barplot(x=gender_count.index, y=gender_count.values, ax=ax)
ax.bar_label(ax.containers[0])
st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SALES vs AGE GROUP ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("💰 Sales by Age Group")

fig, ax = plt.subplots()
sns.barplot(
    data=filtered_data,
    y="Age Group",
    x="Sales Amount",
    estimator=np.sum,
    ax=ax
)
ax.bar_label(ax.containers[0])
st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TOP STATES ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader("📍 Top 10 States")

top_states = filtered_data["State"].value_counts().head(10)

fig, ax = plt.subplots()
sns.barplot(x=top_states.index, y=top_states.values, ax=ax)
ax.bar_label(ax.containers[0])
plt.xticks(rotation=30)
st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.success("✨ Dashboard Loaded Successfully")
st.markdown("**Built by Deepak Saini | Streamlit • Python • Data Analytics**")
st.balloons()
