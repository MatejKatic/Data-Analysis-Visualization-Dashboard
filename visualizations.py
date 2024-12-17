import plotly.express as px

def create_line_chart(df, x_col, y_col):
    fig = px.line(df, x=x_col, y=y_col, title="Line Chart")
    return fig

def create_bar_chart(df, x_col, y_col):
    fig = px.bar(df, x=x_col, y=y_col, title="Bar Chart")
    return fig

def create_heatmap(df, x_col, y_col, value_col):
    pivot_df = df.pivot_table(index=y_col, columns=x_col, values=value_col, aggfunc='mean')
    fig = px.imshow(pivot_df, title="Heatmap")
    return fig
