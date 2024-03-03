import dash_mantine_components as dmc
from defaultlayouts.lorem import lorem

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

