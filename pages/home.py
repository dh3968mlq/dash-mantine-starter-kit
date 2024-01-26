import dash
from dash import html

dash.register_page(__name__, path='/', title='Dash Mantime Starter Kit')

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut " \
        "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in " \
        "voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

layout = html.Div([
    html.H1('Home page'),
    html.P(
        [
            'A template with boilerplate code for creating a basic website using',
            ' Dash and Dash Mantine components. ',
            html.A('Code on Github', href="https://github.com/dh3968mlq/dash-mantine-starter-kit")
        ]
    ),
    html.H2('Dash and Mantine Components'),
    html.P(
        [
            html.A('Dash', href="https://dash.plotly.com/", target="_blank"),
              ' allows ',
            html.A('multi-page web apps', href="https://dash.plotly.com/urls", target="_blank"),
              ' to be programmed (almost entirely) in Python'
        ]
    ),
    html.P(
        [
            'Dash Mantine Components', 
            'wraps the ',
            'Mantine',
            ' React components library'
        ]
    ),
    html.H2('This template'),
    html.H3('Implements:'),
    html.Ul(
        [
            html.Li("Sidebars responsive to viewport size")
        ]
    ),
    html.H3('Doesn\'t implement:'),
    html.Ul(
        [
            html.Li("Logins")
        ]
    ),
    html.H3('Implementation'),
    html.Ul(
        [
            html.Li("Code is complete for heroku depolyment"),
            html.Li("Layout definition here is generally in styles.css for code clarity. "
                    "It could, mostly, equally be defined in the Python code"),
            
        ]
    ),
    html.H2("Some long text to show scrolling behaviour"),
    html.Div(
        children=[
            html.P(lorem) for i in range(10)
        ]
    ),
])