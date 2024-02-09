from dash import callback, Output, Input

# -- Close the sidebar drawer when a link is clicked (when the URL changes)
@callback(    # https://dash.plotly.com/basic-callbacks
    Output("components-navbar-drawer", "opened", allow_duplicate=True),
    Input("main-url","href"),
    prevent_initial_call=True,
)
def close_drawer(href):
    return False
