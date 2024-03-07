import dash_mantine_components as dmc
from defaultlayouts.lorem import lorem
from dash import page_registry, callback, Input, Output, ctx

# -- Replicate variables (custom properties) defined in styles.css as required
header_height = 34    # The height of an h2. px is assumed by dmc (usually)
footer_height = 24    # The height of an h5
navbar_width=300

def side_nav_content(idprefix:str=""):
    "Common content for both versions of side navbar"
    nav_data = page_registry.values()
    nav_content = (
        [
            dmc.Space(h=20),
            dmc.Title("Navigation", order=4),
            dmc.Text("Auto-generated from the page registry"),
            dmc.Title("Pages", order=5),
            dmc.List(
            [side_navbar_link(entry) for entry in nav_data
               if entry["path"][:7] != "/posts/" ],
            ),
            dmc.Title("Posts", order=5),
            dmc.List(
            [side_navbar_link(entry) for entry in nav_data
               if entry["path"][:7] == "/posts/" ],
            ),
            dmc.Title("Button with callback", order=4),
            dmc.Text("The callback must handle both the fixed navbar button id and the popup button id"),
            dmc.Button("Press here", color="primary", id=f"{idprefix}-button1"),
            dmc.Text("Button has not been pressed", id=f"{idprefix}-button1-count"),
            dmc.Space(h=20),
            dmc.Title("Long text to show scrolling", order=4),
        ] + \
        [dmc.Text(lorem) for _ in range(6)]
    )
    return nav_content
# --------------------------------------------# This uses dmc.ScrollArea for scrolling. 
def side_navbar_link(nav_entry):
    link = dmc.ListItem( 
            dmc.Anchor(nav_entry["name"], href=nav_entry["path"]),
            style={"padding":0, "margin":0},
        )
    return link
# --------------------------------------------
def side_navbar():
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
                    dmc.Text("The sidebar and drawer can contain common content or different content. " + 
                            "This text is in the sidebar only, and everything below is common between the sidebar and drawer."
                    ),
                ] + side_nav_content(idprefix="bar"),
            )
        ],
        className="page-navbar",
    )
    return navbar
# --------------------------------------------
# This uses CSS overflow: scroll, instead of dmc.ScrollArea
def navbar_drawer():
    contents = [
            dmc.Text("Uses dmc.Drawer"),
            dmc.Text("This drawer becomes available when screen width is below 1200px"),
        ] + side_nav_content(idprefix="drawer")
    return contents
# --------------------------------------------
def popup_title():
    return "Left side drawer"
# --------------------------------------------
# Callback handles and updates both the sidebar and drawer instances of the button and message
@callback(    # https://dash.plotly.com/basic-callbacks
    Output("bar-button1-count", "children"),
    Output("drawer-button1-count", "children"),
    Output("bar-button1","n_clicks"),
    Output("drawer-button1","n_clicks"),
    Input("bar-button1","n_clicks"),
    Input("drawer-button1","n_clicks"),
    prevent_initial_call=True,
)
def increment_button1_clicks(nclicks_bar, nclicks_drawer):
    trigger = ctx.triggered_id
    nclicks = nclicks_bar if trigger == "bar-button1" else nclicks_drawer
    text = f"Button has been clicked {nclicks} times"
    return text, text, nclicks, nclicks

