import dash_bootstrap_components as dbc
from dash import html, page_container, dcc
import dash_mantine_components as dmc

# -- Replicate variables (custom properties) defined in styles.css as required
navbar_width=300

def createlayout(
        headercontents=None,
        leftsidebarcontents=None,
        popupcontents=None,
        popuptitle="",
        rightsidebarcontents=None,
        footercontents=None,
        header_height=34,       # Must correspond to value set in styles.css
        footer_height = 24,      # Ditto
        theme={}
        ):
    contents = [
            html.Div(children=headercontents, className="page-header"),
            html.Div(
                html.Div(
                    children=page_container, 
                    className="page-inner"     # To get the bottom padding right on a narrow screen. 
                ), 
                className="page-body"
            ),
            dcc.Location(id="main-url"),
    ]

    if leftsidebarcontents is not None:
        contents.append(html.Div(children=leftsidebarcontents, className="page-navbar"))

    if popupcontents is not None:
        contents.append(
            dmc.Drawer(
                id="page-default-drawer",
                zIndex=9,
                title=popuptitle,
                size=f"{navbar_width}px",   # Have to specify width here, and have to specify px 
                #overlayBlur=3,  # Not implemented dmc 0.13.0a3?
                children=popupcontents,
                className="page-navbar-drawer",
                styles={  # This (undocumented 21/2/24) succeeds in positioning the drawer between the header and footer
                    "inner":{"top":header_height, "bottom":footer_height}
                },
            )
        )

    if rightsidebarcontents is not None:
        contents.append(html.Div(children=rightsidebarcontents, className="page-aside"))

    if footercontents is not None:
        contents.append(html.Div(children=footercontents, className="page-footer"))

    layout = dmc.MantineProvider(   # https://mantine.dev/theming/mantine-provider/
        theme=theme,         # https://www.dash-mantine-components.com/components/mantineprovider
        children= contents,
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )
 
    return layout
