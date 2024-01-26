import dash
from dash import html

dash.register_page(__name__, title='Archive Page')

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
])