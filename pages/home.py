'''
Home page
Rendered by calls to dmc components
'''
from dash import register_page, dcc, html
import dash_mantine_components as dmc
from defaultlayouts.lorem import lorem

register_page(__name__, 
              name="Home Page",
              path='/', title='Dash Mantine Template') # https://dash.plotly.com/urls

stackitemstyle = {
    "border": f"1px solid gray",
    "border-radius": 4,
    "textAlign": "center",
}

layout = dmc.Container( # One possible container for page content. Set fluid=True to avoid width restrictions
    [
        dmc.Title('A responsive site template using' +
                ' Dash and Dash Mantine Components. ', order=3),
        dmc.Center(dmc.Button(
            children=[
                dcc.Link('Code on Github', href="https://github.com/dh3968mlq/dash-mantine-starter-kit",
                    target="_blank", 
                ),
            ]
        )),
        dmc.Space(h=12),
        dmc.Image(src="/static/pexels-pixabay-262367-cropped2.jpg", #width="100%",
                 ),
        dmc.Text([
            "This template has open source (MIT License) boilerplate code for a responsive site implemented in Dash Mantine ",
            "Components, including independently scrolling sidebars on wide screens, a popup "
            "navigation menu on small screens and customisable sidebars"
        ]),
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
        dmc.Title('This page', order=2),
        dmc.Text('Is implemented in Python, using dmc components'),
        dmc.Text([
                'See the ',
                dmc.Anchor('description', href="/posts/description"),
                ' page for more details about the template'
            ]
        ),
        dmc.Title('Some Stacking Elements', order=3),
        dmc.Grid([   
            dmc.Col(html.Div(dmc.Title("Item 1", order=3), style=stackitemstyle | {"background-color" : "lightgray"}), span=12, lg=4),
            dmc.Col(html.Div(dmc.Title("Item 2", order=3), style=stackitemstyle | {"background-color" : "lightcyan"}), span=12, lg=4),
            dmc.Col(html.Div(dmc.Title("Item 3", order=3), style=stackitemstyle | {"background-color" : "lightpink"}), span=12, lg=4),
            ],
        ),
        dmc.Space(h=6),
        dmc.Divider(size=3),
        dmc.Title("Long text to show scrolling", order=2),
    ] + 
    [
        dmc.Text(lorem) for i in range(20)
    ],
    fluid=True
)