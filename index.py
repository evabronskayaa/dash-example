from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

from app import app
from data import sales_df


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    df = sales_df[sales_df.sku == value]

    return px.line(df, x='date', y='unit_sold')


if __name__ == '__main__':
    app.run(debug=True)