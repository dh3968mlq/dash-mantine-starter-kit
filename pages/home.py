import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div(
        children=[
            html.P(f"Main page line {i}") for i in range(60)
        ]
    ),
])