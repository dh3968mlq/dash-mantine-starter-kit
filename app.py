'''
    Dash / Mantine boilerplate for a basic responsive multi-page app
    Author David Harris 2024 
    # -- ... based on https://github.com/snehilvj/dmc-docs, author Snehil Vijay
'''
import sys
sys.path.append('./markdown2dash')

from dash import Dash, page_registry
import gunicorn                         # Necessary for Heroku?
#from lib.applayout import get_layout

from core import callback_close_drawer   # The import defines the callback, no need to reference it
from core import callback_open_drawer
from core import corelayout
from defaultlayouts import header, leftsidebar, rightsidebar, footer

app = Dash(__name__, use_pages=True)    # A multi-page app: https://dash.plotly.com/urls
app._favicon = "favicon.png"            # app.title must be set page by page
server = app.server                     # Necessary for Heroku?

text_theme = {
    "margin-top": 4,
    "margin-bottom": 4,
    "line-height": 20,   # pixels!
    "font-size": 14,
}
theme = {
    "colorScheme": "light",   # "dark" for the default dark theme. 
    "fontFamily": "'Inter', sans-serif",
    "components": {
        "Text": {"styles": {"root": text_theme}}, # Applies styles to text elements, via .mantine-Text-root
        "List": {"styles": {"item": text_theme}}, # Applies text_theme to list items
    },
}

app.layout = corelayout.createlayout(
    headercontents=header.header(),
    leftsidebarcontents=leftsidebar.side_navbar(),
    popupcontents=leftsidebar.navbar_drawer(),
    popuptitle=leftsidebar.popup_title(),
    rightsidebarcontents=rightsidebar.aside(),
    footercontents=footer.footer(),
    theme=theme
)
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8050)  
