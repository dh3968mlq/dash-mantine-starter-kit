from dash import clientside_callback, Input, Output, State

# Display the navigation drawer when the hamburger button is clicked
clientside_callback(   # https://dash.plotly.com/clientside-callbacks
    """function(n_clicks, is_already_open) { return !is_already_open }""",     # Javascript
    Output("components-navbar-drawer", "opened", allow_duplicate=True),
    Input("drawer-hamburger-button", "n_clicks"),
    State("components-navbar-drawer", "opened"),
    prevent_initial_call=True,
)
