from dash import html, dcc

from data import sales_df


general_layout = html.Div([
    html.H1(children='SKU stats', style={'textAlign':'center'}),
    dcc.Dropdown(sales_df.sku.unique(), '100001', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])