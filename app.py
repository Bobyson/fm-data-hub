import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Hub")
st.write("Enhanced Data Hub")

uploaded_file = st.file_uploader("Upload file", type=["csv"])

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Raw Data Preview")
#     st.dataframe(df.head())

#     required_cols = ["Name", "Club", "Position", "Minutes", "Goals", "Assists", "Average Rating"]

#     missing = [col for col in required_cols if col not in df.columns]
#     if missing:
#         st.error(f"Missing required columns: {', '.join(missing)}")
#         st.stop()

#     for col in ["Minutes", "Goals", "Assists", "Average Rating"]:
#         df[col] = pd.to_numeric(df[col], errors="coerce")

#     st.sidebar.header("Filters")
#     clubs = st.sidebar.multiselect("Club", sorted(df["Club"].dropna().unique()))
#     positions = st.sidebar.multiselect("Position", sorted(df["Position"].dropna().unique()))
#     min_minutes = st.sidebar.slider("Minimum minutes", 0, int(df["Minutes"].max()), 0)

#     filtered_df = df.copy()

#     if clubs:
#         filtered_df = filtered_df[filtered_df["Club"].isin(clubs)]

#     if positions:
#         filtered_df = filtered_df[filtered_df["Position"].isin(positions)]

#     filtered_df = filtered_df[filtered_df["Minutes"] >= min_minutes]

#     st.subheader("Filtered Players")
#     st.dataframe(filtered_df)

#     fig = px.scatter(
#         filtered_df,
#         x="Goals",
#         y="Assists",
#         color="Club",
#         hover_data=["Name", "Position", "Minutes"],
#         title="Goals vs Assists"
#     )

#     st.plotly_chart(fig, use_container_width=True)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.subheader("Raw Data Preview")
    st.dataframe(df)

    st.write("Columns in uploaded file:")
    st.write(df.columns.tolist())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    all_cols = df.columns.tolist()

    if len(all_cols) < 2:
        st.warning("Need at least 2 columns.")
        st.stop()

    x_axis = st.selectbox("Select X-axis", all_cols)
    y_axis = st.selectbox("Select Y-axis", numeric_cols if numeric_cols else all_cols)

    color_col = st.selectbox("Color by", ["None"] + all_cols)

    fig = px.scatter(
        df,
        x=x_axis,
        y=y_axis,
        color=None if color_col == "None" else color_col,
        title=f"{y_axis} vs {x_axis}"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Upload a CSV file to begin")



