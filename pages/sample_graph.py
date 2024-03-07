# -- From https://dash.plotly.com/tutorial
from dash import html, dash_table, dcc, callback, Output, Input, register_page, ctx
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

header_height = 50    
footer_height = 30

register_page(module=__name__,
              name="Sample Graph",
              title='Sample Graph')

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
df["lifeExp"] = df["lifeExp"].round(1)
df["gdpPercap"] = df["gdpPercap"].astype(int)

layout = [
    dmc.Container([
        dmc.Title('Example Graph', order=2),
        dmc.Text([
            "This example, taken from ",
            dmc.Anchor("https://dash.plotly.com/tutorial", 
                href="https://dash.plotly.com/tutorial", target="_blank"),
            " shows how controls can be duplicated on a custom pop-up sidebar"
        ]),
        dmc.Space(h=6),
        dmc.RadioGroup(
            [dmc.Radio(x, value=x) for x in ['pop', 'lifeExp', 'gdpPercap']],
            value='lifeExp',
            #orientation='horizontal',  # Not implemented in 0.13.0a3 ?
            id='radio-buttons-final', 
            className='bg-info rounded-1 my-2'
        ),
        dmc.Space(h=12),
        dmc.Grid(
            [
                dmc.Col(
                    dmc.Container([
                        dash_table.DataTable(
                            data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'},
                        ),
                    ]),
                    span=12, lg=6,
                    id='col-datatable',
                ),
                dmc.Col([
                    dcc.Graph(figure={}, id='my-first-graph-final'),
                    ],
                    id='col-graph',
                    span=12, lg=6,
                ),
            ],
        ), 
    ], className="page-body"),
    # -- The custom pop-up drawer. Duplicates the radio buttons
    dmc.Drawer(
        id={"type":"drawer", "page": __name__}, # Needed for the open/close callbacks
        title="Graph Controls",
        children=
        [
            dcc.Link("Home", href="/"),
        dmc.RadioGroup(
            [dmc.Radio(x, value=x) for x in ['pop', 'lifeExp', 'gdpPercap']],
            value='lifeExp',
            #orientation='horizontal',
            id='radio-buttons-popup', 
            className='bg-info rounded-1 my-2'
        ),
        ],
        styles={  # This (undocumented 21/2/24) succeeds in positioning the drawer between the header and footer
            "inner":{"top":header_height, "bottom":footer_height}
        }
    ),
]
# -------------------------------------------------------
# Handle radio buttons. Keep the two duplicates in sync
@callback(
    Output('my-first-graph-final', 'figure'),
    Output('radio-buttons-final', 'value'),
    Output('radio-buttons-popup', 'value'),
    Input('radio-buttons-final', 'value'),
    Input('radio-buttons-popup', 'value'),
)
def update_graph(col_body, col_popup):
    trigger = ctx.triggered_id
    col_chosen = col_body if trigger == 'radio-buttons-final' else col_popup
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig, col_chosen, col_chosen
