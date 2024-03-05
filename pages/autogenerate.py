'''
auto generate pages from all .md files held in ./markdown
'''
from pathlib import Path
from dash import register_page
from markdown2dash import parse

files = Path("posts").glob("*.md")

for file in files:
    filename = file.name[:-3]
    content = file.read_text()
    layout = parse(content)

    register_page(
        module=filename,
        path=f"/posts/{filename.lower()}",
        name=filename.replace("-"," ").replace("_"," "),
        layout=layout,
    )
