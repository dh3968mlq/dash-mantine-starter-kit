'''
    Dash / Mantine boilerplate
    Author David Harris 2024 
    # -- ... drawing on https://github.com/snehilvj/dmc-docs
'''
from dash import Dash, page_registry
import gunicorn # Necessary for Heroku?
import applayout

app = Dash(__name__, use_pages=True)
app._favicon = "favicon.png"
server = app.server  # Necessary for Heroku?

app.title = "Dash Mantine starter kit"
app.layout = applayout.get_layout(page_registry.values())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8050)
