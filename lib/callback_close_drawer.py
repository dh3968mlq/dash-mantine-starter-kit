from dash import callback, Output, Input

@callback(
    Output("components-navbar-drawer", "opened", allow_duplicate=True),
    Input("main-url","href"),
    prevent_initial_call=True,
)
def close_drawer(href):
    return False
