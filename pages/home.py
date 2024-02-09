'''
Home page
'''
from dash import register_page
import dash_mantine_components as dmc
from lib.lorem import lorem

register_page(__name__, path='/', title='Dash Mantine Starter Kit') # https://dash.plotly.com/urls

layout = dmc.Container( # One possible container for page content. Set fluid=True to avoid width restrictions
    [
        dmc.Title('Home page', order=1),
        dmc.Text(
            [
                'A template with boilerplate code for creating a basic website using',
                ' Dash and Dash Mantine components. ',
                dmc.Anchor('Code on Github', href="https://github.com/dh3968mlq/dash-mantine-starter-kit", target="_blank")
            ]
        ),
        dmc.Title('Dash and Mantine Components', order=2),
        dmc.Text(
            [
                dmc.Anchor('Dash', href="https://dash.plotly.com/", target="_blank"),
                ' allows ',
                dmc.Anchor('multi-page web apps', href="https://dash.plotly.com/urls", target="_blank"),
                ' to be programmed (almost entirely) in Python'
            ]
        ),
        dmc.Text(
            [
                dmc.Anchor('Dash Mantine Components', href="https://www.dash-mantine-components.com/", target="_blank"), 
                ' wraps the ',
                dmc.Anchor('Mantine', href="https://mantine.dev/", target="_blank"),
                ' React components library'
            ]
        ),
        dmc.Title('This template', order=2),
        dmc.Title('Implements:', order=3),
        dmc.List(
            [
                dmc.ListItem("Sidebars responsive to viewport size")
            ]
        ),
        dmc.Title('Doesn\'t implement:', order=3),
        dmc.List(
            [
                dmc.ListItem("Logins")
            ]
        ),
        dmc.Title('Implementation', order=3),
        dmc.List(
            [
                dmc.ListItem("Code is complete for Heroku deployment"),
                dmc.ListItem("Layout definition here is generally in styles.css for code clarity. "
                        "It could, mostly, equally be defined in the Python code"),
                
            ]
        ),
        dmc.Title("Some long text to show scrolling behaviour", order=2),
    ] + 
    [
        dmc.Text(lorem) for i in range(20)
    ],
    fluid=True
)