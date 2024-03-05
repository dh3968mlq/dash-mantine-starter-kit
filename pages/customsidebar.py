from dash import register_page, dcc
from markdown2dash import parse
import dash_mantine_components as dmc

register_page(module=__name__, 
              name="Page with customised sidebar",
              title='Dash Bootstrap Template')

header_height = 34    
footer_height = 24

layout = dmc.Container( 
        children=[
            dmc.Container(
            parse('''

## A page with a custom sidebar

An example page that has a custom sidebar and pop-up drawer.
                         
Some content here is rendered from Markdown, some (such as the image below) in Python

'''
            ) + [
        dmc.Image(src="/static/pexels-pixabay-262367-cropped2.jpg"),        
        ],
        className='page-body'
    ),
    # --- The custom sidebar. Just add it to the content with a 'page-navbar' class
    dmc.Container(
        children=[
            dmc.Title("Custom sidebar layout", order=4),
            dmc.Text("This page has a custom left sidebar layout that replaces the default." +
                   "It is also possible to have a custom right sidebar. This page hides the default by using blank content"
            )
        ],
        className='page-navbar'
    ),
    # -- The custom pop-up drawer
    dmc.Drawer(
        id={"type":"drawer", "page": __name__},
        title="Custom Drawer",
        children=
        [
            dmc.Text("This page has a custom left pop-up that replaces the default."),
            dmc.Text("Uses dbc.Offcanvas"),
            dcc.Link("Home", href="/"),
        ],
    #    style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
    #        "top":f"{header_height}px",
    #        "bottom":f"{footer_height}px",
    #    }
    ),
    # -- Custom right sidebar. This just hides the default
    dmc.Container(children="", className="page-aside")
        ]
) #]