from dash import Input, Output, State, ALL, clientside_callback

# Open the navigation drawer when the hamburger button is clicked
# (It cannot be clicked when an OffCanvas is open)
# Open custom drawer if one exists in the display, otherwise open the default drawer
# Custom drawers must be give id {"type":"drawer", "page": ...}
# https://dash.plotly.com/pattern-matching-callbacks

clientside_callback(   # https://dash.plotly.com/clientside-callbacks
    """
        function(n_clicks, custom_already_open) { 
            if (custom_already_open.length > 0) {
                return [false, [true] ]
            } else {
                return [true, [] ]
            } 
        }
    """,     # Javascript
    Output("page-default-drawer", "opened", allow_duplicate=True),
    Output({"type":"drawer", "page": ALL}, "opened", allow_duplicate=True),
    Input("drawer-hamburger-button", "n_clicks"),
    State({"type":"drawer", "page": ALL}, "opened"),
    prevent_initial_call=True,
)
