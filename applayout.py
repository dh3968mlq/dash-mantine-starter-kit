import dash_mantine_components as dmc
from dash import html, page_container
from dash_iconify import DashIconify

# -- These replicate custom properties in styles.css
navbar_width = 300    # px is assumed by dmc
aside_width = 300
header_height = 70

def create_header():
    header = dmc.Header(
        height=header_height,   # Required
        fixed=True, 
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
        position={"top": header_height},
        width={"base": navbar_width}, 
        className="page-navbar",
        children=[
            html.H3("Side Navbar Section")
        ],
    )
    return navbar
# --------------------------------------------------------------------------------------------------
def create_aside():
    aside = dmc.Aside(
        fixed=True,
        position={"top": header_height, "right": 0},
        width={"base": aside_width}, 
        className="page-aside",
        children=[
            html.H3("Aside section")
        ],
    )
    return aside
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
                    create_aside(),
                    create_body(),
                ],
            ),
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
    return layout
