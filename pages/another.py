import dash
from dash import html

dash.register_page(__name__, title='Another Page')

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
        "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in " \
        "voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

layout = html.Div([
    html.H1('This is another page'),
    html.Div(
        children=[
            html.P(lorem) for i in range(10)
        ]
    )
])