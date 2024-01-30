import dash
from dash import html
from lib.lorem import lorem

dash.register_page(__name__, title='Another Page')

layout = html.Div([
    html.H1('This is another page'),
    html.Div(
        children=[
            html.P(lorem) for i in range(10)
        ]
    )
])