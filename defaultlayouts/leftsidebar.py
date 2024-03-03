import dash_mantine_components as dmc
from defaultlayouts.lorem import lorem
from dash import page_registry

# -- Replicate variables (custom properties) defined in styles.css as required
header_height = 34    # The height of an h2. px is assumed by dmc (usually)
footer_height = 24    # The height of an h5
navbar_width=300

# This uses dmc.ScrollArea for scrolling. 
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
                ] + side_nav_content(),
            )
        ],
        className="page-navbar",
    )
    return navbar
# --------------------------------------------
# This uses CSS overflow: scroll, instead of dmc.ScrollArea
def navbar_drawer():
    contents = [
            dmc.Title("Left side drawer", order=2),
            dmc.Text("Uses dmc.Drawer"),
            dmc.Text("This drawer becomes available when screen width is below 1200px"),
        ] + side_nav_content()
    return contents
# --------------------------------------------
def popup_title():
    return ""
# --------------------------------------------
def side_navbar_link(nav_entry):
    link = dmc.ListItem( 
            dmc.Anchor(nav_entry["name"], href=nav_entry["path"]),
            style={"padding":0, "margin":0},
        )
    return link
# --------------------------------------------
def side_nav_content():
    "Common content for both versions of side navbar"
    nav_data = page_registry.values()
    nav_content = (
        [
            dmc.Space(h=20),
            dmc.Title("Navigation", order=4),
            dmc.Text("Auto-generated from the page registry, but appears in a rather random order"),
        ] + 
        [dmc.List(
            [side_navbar_link(entry) for entry in nav_data],
        )] + 
        [   dmc.Space(h=20),
            dmc.Title("Long text to show scrolling", order=4),
        ] + \
        [dmc.Text(lorem) for _ in range(6)]
    )
    return nav_content
# --------------------------------------------
def aside():
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
