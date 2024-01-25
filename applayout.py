'''
Create layout
Layout is defined in styles.css whenever it's possible and elegant
...since it keeps the code shorter and more focussed on functionality
Many things such as position and size of elements could instead be specified in the code here
'''
import dash_mantine_components as dmc
from dash import html, page_container
from dash_iconify import DashIconify

# -- These replicate variables (custom properties) defined in styles.css as required
header_height = 70    # px is assumed by dmc

def create_header():
    header = dmc.Header(
        height=header_height,   # Required here, setting it in CSS is not enough
        className="page-header",
        children=[
            html.H1("Header Section")
        ],
    )
    return header
# --------------------------------------------------------------------------------------------------
def create_side_navbar():
    navbar = dmc.Navbar(
        className="page-navbar",
        children=[
            html.H3("Side Navbar Section")
        ],
    )
    return navbar
# --------------------------------------------------------------------------------------------------
def create_aside():
    aside = dmc.Aside(
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
    layout = dmc.MantineProvider(   # https://mantine.dev/theming/mantine-provider/
        theme={},         # https://www.dash-mantine-components.com/components/mantineprovider
        children=dmc.NotificationsProvider( # https://www.dash-mantine-components.com/components/notification
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
