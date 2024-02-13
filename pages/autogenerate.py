from pathlib import Path
from dash import dcc, register_page
from dmcmarkdown import markdown as dmcmd

files = Path("markdown").glob("*.md")

for file in files:
    filename = file.name[:-3]
    content = file.read_text()
    layout = dmcmd.Markdown(content, fluid='lg')

    register_page(
        filename,
        layout=layout,
    )
