from dash import html, register_page
import dash_mantine_components as dmc
from lib.lorem import lorem

register_page(__name__, title='Another Page')

layout = html.Div(
    [
        dmc.Title('This is another page', order=1),
    ] + 
    [
        dmc.Text(lorem) for i in range(10)
    ]
)