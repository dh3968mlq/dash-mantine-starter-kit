'''
Create layout
Some layout is defined in styles.css
'''
import dash_mantine_components as dmc
from dash import page_container, dcc
from dash_iconify import DashIconify
from lib.lorem import lorem

# -- Replicate variables (custom properties) defined in styles.css as required
header_height = 34    # The height of an h2. px is assumed by dmc (usually)
footer_height = 24    # The height of an h5
navbar_width=300

def create_header_link(icon, href, size=22, color="indigo"):
    "Create a link in the header, e.g. to Github or to Social"
    return dmc.Anchor(    # https://www.dash-mantine-components.com/components/anchor
        dmc.ThemeIcon(    # https://www.dash-mantine-components.com/components/themeicon
            DashIconify(  # https://pypi.org/project/dash-iconify/
                icon=icon,
                width=size,
            ),
            size=size,
            style={"margin-top":"4px"}
        ),
        href=href,
        target="_blank",
    )
# --------------------------------------------
def create_home_link(label, order=1):
    topmargins = [0,0,2,4,5,6]
    return dmc.Title(
        dcc.Link(   # dcc.Link is used here because dmc.Anchor appears to inherit styling explicitly applied to dmc.Text
                    # ...and that's problematic here - we want this to be displayed as a title size, not a paragraph size
            label,
            href="/",
            style={"color":"black", "text-decoration":"none",},
        ),
        order=order,
        style={"margin-top":f"{topmargins[order-1]}px"},
    )
# --------------------------------------------
def create_header_left_column(nav_data):
    hl = dmc.Col(
        [
            # dmc.MediaQuery is an alternative to using @media in CSS
            # It allows the DMC size definitions 'lg' etc. to be used
            # Included here to show how it's done
            dmc.MediaQuery(  # https://www.dash-mantine-components.com/components/mediaquery
                create_home_link("Dash Mantine Responsive Template", order=2),
                smallerThan="lg",
                styles={"display": "none"},
            ),
            dmc.MediaQuery(
                create_home_link("DMC Template", order=4),
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
                dmc.MediaQuery(      # Create the button to show the drawer only if the screen is below 1200px
                    dmc.ActionIcon(   # https://www.dash-mantine-components.com/components/actionicon
                        DashIconify(
                            icon="radix-icons:hamburger-menu",
                            width=22,
                        ),
                        id="drawer-hamburger-button",
                        variant="outline",
                        size=22,
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
            #dmc.Space(h=4),  
            dmc.Grid(
                children=[
                    create_header_left_column(nav_data),
                    create_header_right_column(nav_data),
                ],
                #align='center',    # Vertical alignment of content to center. (Does this work?)
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
    drawer = dmc.Drawer(
        id="components-navbar-drawer",
        zIndex=9,
        size=f"{navbar_width}px",   # Have to specify width here, and have to specify px 
        #overlayBlur=3,  # Not implemented dmc 0.13.0a3?
        children=
        [
            dmc.Title("Left side drawer", order=2),
            dmc.Text("Uses dmc.Drawer"),
            dmc.Text("This drawer becomes available when screen width is below 1200px"),
        ] + create_side_nav_content(nav_data), # + 
        className="page-navbar-drawer",
        styles={  # This (undocumented 21/2/24) succeeds in positioning the drawer between the header and footer
            "inner":{"top":header_height, "bottom":footer_height}
        },
    )
    return drawer
# --------------------------------------------
def create_side_navbar_link(nav_entry):
    link = dmc.ListItem( 
            dmc.Anchor(nav_entry["name"], href=nav_entry["path"]),
            style={"padding":0, "margin":0},
        )
    return link
# --------------------------------------------
def create_side_nav_content(nav_data):
    "Common content for both versions of side navbar"
    nav_content = (
        [
            dmc.Space(h=20),
            dmc.Title("Navigation", order=4),
            dmc.Text("Auto-generated from the page registry, but appears in a rather random order"),
        ] + 
        [dmc.List(
            [create_side_navbar_link(entry) for entry in nav_data],
        )] + 
        [   dmc.Space(h=20),
            dmc.Title("Long text to show scrolling", order=4),
        ] + \
        [dmc.Text(lorem) for _ in range(6)]
    )
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
            children=page_container,
            fluid=True,     # no limit on width. Actual width is limited by margins, 
                            # set in CSS to place it within sidebars when they are visible
            className="page-body"
    )
    return body
# -----------------------------------------------------------
def create_footer():
    footer = dmc.Footer(
        height=footer_height,
        fixed=True,
        children=[
            dmc.Title("Footer area", order=5,
                      style={"color":"black", "text-decoration":"none"})
        ],
        className="page-footer",
    )
    return footer
# -----------------------------------------------------------
def get_layout(nav_data):
    text_theme = {
        "margin-top": 4,
        "margin-bottom": 4,
        "line-height": 20,   # pixels!
        "font-size": 14,
    }
    #text_theme = {}

    theme = {
        "colorScheme": "light",   # "dark" for the default dark theme. 
        "fontFamily": "'Inter', sans-serif",
        "components": {
            "Text": {     
                "styles": {
                    "root": text_theme, # Applies styles to text elements, via .mantine-Text-root
                }
            },
            "List": {
                "styles": {
                    "item": text_theme, # Applies text_theme to list items
                }
            },
        },
    }

    layout = dmc.MantineProvider(   # https://mantine.dev/theming/mantine-provider/
        theme=theme,         # https://www.dash-mantine-components.com/components/mantineprovider
        children= [
            create_header(nav_data),
            create_side_navbar(nav_data),
            create_navbar_drawer(nav_data),
            create_aside(),
            create_body(),
            create_footer(),
            dcc.Location(id="main-url"),
        ],
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
    return layout
