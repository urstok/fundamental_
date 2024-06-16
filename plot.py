import subprocess
import os
import pandas as pd
import plotly.graph_objects as go

# Function to read CSV file and plot the consolidated balance sheet data as a bar chart
def plot_balance_sheet(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file, index_col=0)

    # Transpose the DataFrame to have dates as rows and items as columns
    df = df.T

    # Create a list of balance sheet components
    balance_sheet_components = df.columns.tolist()

    # Create a figure for the consolidated bar chart
    fig = go.Figure()

    # Add a bar trace for each balance sheet component
    for component in balance_sheet_components:
        fig.add_trace(go.Bar(x=df.index, y=df[component], name=component))

    # Update the layout of the graph
    fig.update_layout(
        title='Consolidated Balance Sheet Components Over Time',
        xaxis_title='Dates',
        yaxis_title='Amount',
        barmode='group',  # Arrange bars in groups
        template='plotly_dark'
    )

    # Show the graph
    fig.show()
