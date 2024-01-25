import datetime
from collections import defaultdict

import dash_mantine_components as dmc
from dash import Output, Input, clientside_callback, html, dcc, page_container, State
from dash_iconify import DashIconify

def get_layout():
    layout = dmc.MantineProvider(
        dmc.MantineProvider(
            theme={
                "fontFamily": "'Inter', sans-serif",
                "primaryColor": "indigo",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                },
            },
            inherit=True,
            children=[
                html.H2("Hello World"),
                page_container
            ],
        ),
        theme={"colorScheme": "light"},
        id="mantine-docs-theme-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
    return layout
