from pathlib import Path
from dash import dcc, register_page

files = Path("markdown").glob("*.md")

for file in files:
    filename = file.name[:-3]
    content = file.read_text()
    layout = dcc.Markdown(content)

    register_page(
        filename,
        layout=layout,
    )
