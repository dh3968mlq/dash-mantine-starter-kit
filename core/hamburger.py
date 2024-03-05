from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

def hamburger():
    burger = dmc.MediaQuery(      # Create the button to show the drawer only if the screen is below 1200px
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
    )
    return burger