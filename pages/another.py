from dash import html, register_page, dcc
import dash_mantine_components as dmc
from lib.lorem import lorem

register_page(__name__, title='Another Page')

layout = dcc.Markdown('''

# This is another page

This page has been rendered from markdown 

## A sample image
                      
This is held as static content within this app
                      
![Example image](/static/sample_image.png)   
                      
## Repeated text to show scrolling

''' + 
" ".join([lorem + "\n\n" for _ in range(30)])
)