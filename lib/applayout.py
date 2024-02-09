'''
Create layout
Some layout is defined in styles.css
'''
import dash_mantine_components as dmc
from dash import page_container, dcc
from dash_iconify import DashIconify
from lib.lorem import lorem

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
# --------------------------------------------
def create_header_left_column(nav_data):
    hl = dmc.Col(
        [
            dmc.MediaQuery(  # https://www.dash-mantine-components.com/components/mediaquery
                dmc.Title("Dash Mantine Starter Kit", order=2), # https://www.dash-mantine-components.com/components/title
                smallerThan="lg",
                styles={"display": "none"},
            ),
            dmc.MediaQuery(
                dmc.Title("DMC Template", order=3),
                largerThan="lg",
                styles={"display": "none"},
            ),
        ],
        span="content",
    )
    return hl
# --------------------------------------------
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
        ),
        span="auto",
    )
    return hr
# --------------------------------------------
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
# --------------------------------------------
# This uses dmc.ScrollArea for scrolling. 
def create_side_navbar(nav_data):
    navbar = dmc.Navbar(
        children=
        [
            dmc.ScrollArea(     # Is this undocumented at the moment? (9/2/2024)
               offsetScrollbars=True,
               pl=10,
                children=
                [
                    dmc.Title("Left sidebar", order=2),
                    dmc.Text("Uses dmc.Navbar"),
                    dmc.Text("This sidebar is replaced with a pop-up drawer when screen width is below 1200px"),
                ] + create_side_nav_content(nav_data),
            )
        ],
        className="page-navbar",
    )
    return navbar
# --------------------------------------------
# This uses CSS overflow: scroll, instead of dmc.ScrollArea
def create_navbar_drawer(nav_data):
    return dmc.Drawer(
        id="components-navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        size=300,
        children=
        [
            dmc.Title("Left side drawer", order=2),
            dmc.Text("Uses dmc.Drawer"),
            dmc.Text("This drawer becomes available when screen width is below 1200px"),
        ] + create_side_nav_content(nav_data),
        className="page-navbar-drawer",
    )

# --------------------------------------------
def create_side_navbar_link(nav_entry):
    # Use dmc.NavLink or dmc.Anchor here, navigates without complete page
    # reloads, and much faster than using html.A
    # dmc.Navlink is always block display, use dmc.Anchor for inline display of a link
    link = dmc.NavLink(   # https://www.dash-mantine-components.com/components/navlink
            label=nav_entry["name"], 
            icon=DashIconify(icon='iconoir:page-right', height=14 ),
            href=nav_entry["path"],
            variant='subtle',
            active=True,
        )
    return link
# --------------------------------------------
def create_side_nav_content(nav_data):
    "Common content for both versions of side navbar"
    nav_content = [
            dmc.Title("Sidebar common content", order=3)
    ] + \
    [create_side_navbar_link(entry) for entry in nav_data] + \
    [dmc.Title("Long text to show scrolling", order=3)] + \
    [dmc.Text(lorem) for _ in range(6)]
    return nav_content
# --------------------------------------------
def create_aside():
    aside = dmc.Aside(
        children=
            dmc.ScrollArea(
                offsetScrollbars=True,
                pl=20,
                children=[

            dmc.Title("Right SideBar", order=2),
            dmc.Text("Uses dmc.Aside"),
            dmc.Text("This sidebar disappears when screen width is below 1500px")
        ] + \
        [dmc.Title("Long text to show scrolling", order=3)] + \
        [dmc.Text(lorem) for _ in range(6)]
            ),
        className="page-aside",
    )
    return aside
# --------------------------------------------
def create_body():
    body = dmc.Container(   # https://www.dash-mantine-components.com/components/container
            #children=dmc.ScrollArea(
            #    offsetScrollbars=True,
                children=page_container,
            #),
            fluid=True,  # no limit on width. Actual width is limited by margins, set in CSS to place it within side areas
            className="page-body"
    )
    return body
# -----------------------------------------------------------
def get_layout(nav_data):
    theme = {
                "fontFamily": "'Inter', sans-serif",
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
