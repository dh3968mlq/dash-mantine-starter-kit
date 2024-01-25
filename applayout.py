import dash_mantine_components as dmc
from dash import html, dcc, page_container
from dash_iconify import DashIconify

def create_header():
    header = dmc.Header(
        height=70,   # Required, make this equal to --header-height
        fixed=True, 
        #px=25,
        className="page-header",
        children=[
            html.H1("Header Section")
        ],
    )
    return header
# --------------------------------------------------------------------------------------------------
def create_side_navbar():
    navbar = dmc.Navbar(
        fixed=True,
        position={"top": 70},   # --header-height
        width={"base": 300},    # -- navbar-width
        className="page-navbar",
        children=[
            html.H3("Side Navbar Section")
        ],
    )
    return navbar
# --------------------------------------------------------------------------------------------------
def create_body():
    body = dmc.Container(
            children=page_container,
            className="page-body"
    )
    return body
# --------------------------------------------------------------------------------------------------
def get_layout():
    layout = dmc.MantineProvider(
        children=dmc.NotificationsProvider(
                [
                    create_header(),
                    create_side_navbar(),
                    create_body(),
                ],
            ),
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
    return layout
