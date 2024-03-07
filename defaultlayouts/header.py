import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import dcc
from core import hamburger

# -- Replicate variables (custom properties) defined in styles.css as required
header_height = 34    # The height of an h2. px is assumed by dmc (usually)

def header_link(icon, href, size=22, color="indigo"):
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
def home_link(label, order=1):
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
def header_left_column():
    hl = dmc.Col(
        children=dmc.Group
        (
            children=[
                hamburger.hamburger(),
                # dmc.MediaQuery is an alternative to using @media in CSS
                # It allows the DMC size definitions 'lg' etc. to be used
                # Included here to show how it's done
                dmc.MediaQuery(  # https://www.dash-mantine-components.com/components/mediaquery
                    home_link("Dash Mantine Responsive Template", order=2),
                    smallerThan="lg",
                    styles={"display": "none"},
                ),
                dmc.MediaQuery(
                    home_link("DMC Template", order=4),
                    largerThan="lg",
                    styles={"display": "none"},
                ),
            ],
        ),
        span="auto",
    )
    return hl
# --------------------------------------------
def header_right_column():
    hr = dmc.Col(
        children=dmc.Group(
            children=[
                header_link(
                    "radix-icons:github-logo",
                    "https://github.com/dh3968mlq/dash-mantine-starter-kit",
                ),
            ],
            position="right",
            grow=False,
        ),
        span="content",
    )
    return hr
# --------------------------------------------
def header():
    header = dmc.Header(
        height=header_height,   # Required here, setting it in CSS is not enough
        children=[
            #dmc.Space(h=4),  
            dmc.Grid(
                children=[
                    header_left_column(),
                    header_right_column(),
                ],
                justify='space-between',
                #align='center',    # Vertical alignment of content to center. (Does this work?)
            ),
        ],
        className="page-header",
    )
    return header