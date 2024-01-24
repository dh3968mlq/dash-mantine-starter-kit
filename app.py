# -- Author David Harris 2024 
from dash import Dash
import gunicorn # Necessary for Heroku?
import applayout

app = Dash(__name__,
        #use_pages=True,
)
server = app.server  # Necessary for Heroku?

app.title = "Dash mantine starter kit"
app._favicon = "favicon.png"
app.layout = applayout.get_layout()

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8050)
