from dash import register_page, dcc
import dash_mantine_components as dmc
from defaultlayouts.lorem import lorem
from markdown2dash import parse

register_page(module=__name__,
              name="Sample Page",
              title='Sample Page')

layout = parse('''

## Sample Page

This page has been rendered from markdown 
using [DH's fork of markdown2dash](https://github.com/dh3968mlq/markdown2dash)

## A sample image
                      
This is held as static content within this app
                      
![Example image](/static/pexels-pixabay-147411_cropped.png)   
                      
## Repeated text to show scrolling

''' + 
" ".join([lorem + "\n\n" for _ in range(30)])
)