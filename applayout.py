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

def create_header_link(icon, href, size=22, color="indigo"):
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )

def create_header_left_column(nav_data):
    hl = dmc.Col(
            [
                dmc.MediaQuery(
                    html.H2("Dash Mantime Starter Kit"),
                    smallerThan="lg",
                    styles={"display": "none"},
                ),
                dmc.MediaQuery(
                    html.H3("DMC Starter Kit"),
                    largerThan="lg",
                    styles={"display": "none"},
                ),
            ],
            span="content",
    )
    return hl

def create_header_right_column(nav_data):
    hr = dmc.Col(
        span="auto",
        children=dmc.Group(
            position="right",
            spacing="xl",
            children=[
                html.P("Hello"),
                create_header_link(
                    "radix-icons:github-logo",
                    "https://github.com/dh3968mlq/dash-mantine-starter-kit",
                ),
            ],
        ),
    )
    return hr

def create_header(nav_data):
    header = dmc.Header(
        height=header_height,   # Required here, setting it in CSS is not enough
        children=dmc.Grid(
            children=[
                create_header_left_column(nav_data),
                create_header_right_column(nav_data),
            ],
            align='center',    # Vertical alignment of content to center
        ),
        className="page-header",
    )
    return header
# --------------------------------------------------------------------------------------------------
def create_side_navbar():
    navbar = dmc.Navbar(
        children=[
            html.H2("Left sidebar"),
            html.P("Uses dmc.Navbar"),
            html.P("This sidebar disappears when screen width is below 1200px")
        ],
        className="page-navbar",
    )
    return navbar
# --------------------------------------------------------------------------------------------------
def create_aside():
    aside = dmc.Aside(
        children=[
            html.H2("Right SideBar"),
            html.P("Uses dmc.Aside"),
            html.P("This sidebar disappears when screen width is below 1500px")
        ],
        className="page-aside",
    )
    return aside
# --------------------------------------------------------------------------------------------------
def create_body():
    body = dmc.Container(    # https://www.dash-mantine-components.com/components/container
            children=page_container,
            size=5000,       # Width. A large number, effectively no limit on width. Default is 960 
            className="page-body"
    )
    return body
# --------------------------------------------------------------------------------------------------
def get_layout(nav_data):
    theme = {
                "fontFamily": "'Inter', sans-serif",
                "primaryColor": "indigo",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                    "Alert": {"styles": {"title": {"fontWeight": 500}}},
                    "AvatarGroup": {"styles": {"truncated": {"fontWeight": 500}}},
                },
            }

    layout = dmc.MantineProvider(   # https://mantine.dev/theming/mantine-provider/
        theme=theme,         # https://www.dash-mantine-components.com/components/mantineprovider
        children=dmc.NotificationsProvider( # https://www.dash-mantine-components.com/components/notification
                [
                    create_header(nav_data),
                    create_side_navbar(),
                    create_aside(),
                    create_body(),
                ],
            ),
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
    return layout
