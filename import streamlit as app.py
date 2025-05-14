import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Simulated data from Excel model for demo purposes
multiples = [2.5, 5, 10, 20, 30]
growth_rates = [0.1, 0.2, 0.4, 0.334687, 0.3]

# Year 5 Revenue Uplift ($B)
revenue_uplift_data = [
    [0.630000, 0.693000, 0.762300, 0.838530, 0.922383],
    [-0.892150, -0.730330, -0.460982, 0.047940, 0.073096],
    [-0.892150, -1.622480, -2.083462, -2.035523, -1.962427],
    [-1.416111, -1.053867, -0.604726, 0.057171, 0.079247],
    [np.nan, np.nan, np.nan, np.nan, np.nan]
]

revenue_df = pd.DataFrame(
    revenue_uplift_data[:len(multiples)],
    index=multiples,
    columns=growth_rates
)

# UI
st.title("Acquisition Model Dashboard")
st.subheader("Year 5 Revenue Uplift ($B)")

# Heatmap
fig = px.imshow(
    revenue_df.values,
    labels=dict(x="Growth Rate", y="Multiple", color="Revenue Uplift ($B)"),
    x=growth_rates,
    y=multiples,
    text_auto=True,
    aspect="auto"
)

st.plotly_chart(fig, use_container_width=True)

# Inputs Section
st.sidebar.header("Assumptions")
st.sidebar.number_input("Total Acquisition Capital", value=3.0)
st.sidebar.number_input("Pre Tax Gross Up Purchase Price", value=2.25)
st.sidebar.slider("% Products", 0.0, 1.0, 0.0)
st.sidebar.slider("% Services", 0.0, 1.0, 1.0)
st.sidebar.selectbox("Include Enabled Revenue?", ["Yes", "No"])
st.sidebar.number_input("Indirect Impact Multiplier", value=7)
