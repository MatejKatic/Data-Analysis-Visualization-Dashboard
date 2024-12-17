import streamlit as st
from utils import load_data, filter_data, get_summary_statistics
from visualizations import create_line_chart, create_bar_chart, create_heatmap

st.title("Data Analysis & Visualization Dashboard")

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("Raw Data (first 5 rows):")
    st.write(df.head())

    # Assume the CSV has a 'date' column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    # Date Filters
    if 'date' in df.columns:
        start_date = st.date_input("Start Date", value=df['date'].min())
        end_date = st.date_input("End Date", value=df['date'].max())
    else:
        start_date, end_date = None, None

    # Category Filters - example if there's a 'category' column
    category_col = None
    if 'category' in df.columns:
        category_col = 'category'
        categories = df[category_col].unique().tolist()
        selected_categories = st.multiselect("Select categories:", categories, default=categories)
    else:
        selected_categories = None

    # Filter Data based on user selection
    filtered_df = filter_data(
        df,
        start_date=start_date if start_date else None,
        end_date=end_date if end_date else None,
        category_column=category_col,
        category_values=selected_categories
    )

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(get_summary_statistics(filtered_df))

    # Visualization Options
    st.subheader("Visualizations")
    chart_type = st.selectbox("Select chart type:", ["Line", "Bar", "Heatmap"])

    if chart_type == "Line":
        # For line chart, pick columns to plot
        x_col = st.selectbox("X-axis:", filtered_df.columns)
        y_col = st.selectbox("Y-axis:", filtered_df.columns)
        fig = create_line_chart(filtered_df, x_col, y_col)
        st.plotly_chart(fig)
    elif chart_type == "Bar":
        x_col = st.selectbox("X-axis:", filtered_df.columns)
        y_col = st.selectbox("Y-axis:", filtered_df.columns)
        fig = create_bar_chart(filtered_df, x_col, y_col)
        st.plotly_chart(fig)
    elif chart_type == "Heatmap":
        # For heatmap, select columns for pivot
        x_col = st.selectbox("X-axis (categories):", filtered_df.columns)
        y_col = st.selectbox("Y-axis (categories):", filtered_df.columns)
        value_col = st.selectbox("Values:", filtered_df.columns)
        fig = create_heatmap(filtered_df, x_col, y_col, value_col)
        st.plotly_chart(fig)
else:
    st.info("Please upload a CSV file to begin.")
