'''
Create layout
Layout is defined in styles.css whenever it's possible and elegant
...since it keeps the code shorter and more focussed on functionality
Many things such as position and size of elements could instead be specified in the code here
'''
import dash_mantine_components as dmc
from dash import page_container, clientside_callback, Input, Output, dcc, callback
from dash_iconify import DashIconify

# -- Replicate variables (custom properties) defined in styles.css as required
header_height = 70    # px is assumed by dmc

def create_header_link(icon, href, size=22, color="indigo"):
    "Create a link in the header, e.g. to Github or to Social"
    return dmc.Anchor(    # https://www.dash-mantine-components.com/components/anchor
        dmc.ThemeIcon(    # https://www.dash-mantine-components.com/components/themeicon
            DashIconify(  # https://pypi.org/project/dash-iconify/
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
            dmc.MediaQuery(  # https://www.dash-mantine-components.com/components/mediaquery
                dmc.Title("Dash Mantine Starter Kit", order=2), # https://www.dash-mantine-components.com/components/title
                smallerThan="lg",
                styles={"display": "none"},
            ),
            dmc.MediaQuery(
                dmc.Title("DMC Starter Kit", order=3),
                largerThan="lg",
                styles={"display": "none"},
            ),
        ],
        span="content",
    )
    return hl

def create_header_right_column(nav_data):
    hr = dmc.Col(
        children=dmc.Group(
            children=[
                create_header_link(
                    "radix-icons:github-logo",
                    "https://github.com/dh3968mlq/dash-mantine-starter-kit",
                ),
                dmc.MediaQuery(
                    dmc.ActionIcon(   # https://www.dash-mantine-components.com/components/actionicon
                        DashIconify(
                            icon="radix-icons:hamburger-menu",
                            width=18,
                        ),
                        id="drawer-hamburger-button",
                        variant="outline",
                        size=36,
                    ),
                    largerThan=1200,
                    styles={"display": "none"},
                ),
            ],
            position="right",
            spacing="xl",
        ),
        span="auto",
    )
    return hr

def create_header(nav_data):
    header = dmc.Header(
        height=header_height,   # Required here, setting it in CSS is not enough
        children=[
            dmc.Space(h=12),  # styles.css sets all padding and margins within .page-header to 0
            dmc.Grid(
                children=[
                    create_header_left_column(nav_data),
                    create_header_right_column(nav_data),
                ],
                align='center',    # Vertical alignment of content to center
            ),
        ],
        className="page-header",
    )
    return header
# --------------------------------------------------------------------------------------------------
def create_side_navbar(nav_data):
    navbar = dmc.Navbar(
        children=[
            dmc.Title("Left sidebar", order=2),
            dmc.Text("Uses dmc.Navbar"),
            dmc.Text("This sidebar disappears when screen width is below 1200px"),
        ] + create_side_nav_content(nav_data),
        className="page-navbar",
    )
    return navbar

def create_navbar_drawer(nav_data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        size=300,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100vh"},
                pt=20,
                children=[
                    dmc.Title("Left side drawer", order=2),
                    dmc.Text("Uses dmc.Drawer"),
                    dmc.Text("This drawer becomes available when screen width is below 1200px"),
                ] + create_side_nav_content(nav_data),
            )
        ],
    )

def create_side_navbar_link(nav_entry):
    # Use dmc.NavLink or dmc.Anchor here, navigates without complete page
    # reloads, and so much smoother and faster than using html.A
    # Note: dmc.Navlink is always block display, use dmc.Anchor for inline display of a link
    link = dmc.NavLink(   # https://www.dash-mantine-components.com/components/navlink
            label=nav_entry["name"], 
            icon=DashIconify(icon='iconoir:page-right', height=14 ),
            href=nav_entry["path"],
            variant='subtle',
            active=True,
        )
    return link

def create_side_nav_content(nav_data):
    nav_content = [
            dmc.Text("Sidebar common content")
    ] + \
    [create_side_navbar_link(entry) for entry in nav_data]

    return nav_content

def create_aside():
    aside = dmc.Aside(
        children=[
            dmc.Title("Right SideBar", order=2),
            dmc.Text("Uses dmc.Aside"),
            dmc.Text("This sidebar disappears when screen width is below 1500px")
        ],
        className="page-aside",
    )
    return aside

def create_body():
    body = dmc.Container(    # https://www.dash-mantine-components.com/components/container
            children=page_container,
            size=5000,       # Width. A large number, effectively no limit on width. Default is 960 
            className="page-body"
    )
    return body
# -----------------------------------------------------------
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
                    create_side_navbar(nav_data),
                    create_navbar_drawer(nav_data),
                    create_aside(),
                    create_body(),
                    dcc.Location(id="main-url"),
                ],
            ),
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
    return layout
# ---------------------------------------------------------
# Display the navigation drawer
clientside_callback(
    """function(n_clicks) { return true }""",
    Output("components-navbar-drawer", "opened", allow_duplicate=True),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)

""" 
@callback(
    Output("components-navbar-drawer", "opened", allow_duplicate=True),
    Input("main-url","href"),
    prevent_initial_call=True,
)
def close_drawer(href):
    return False
 """