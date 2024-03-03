import dash_mantine_components as dmc

# -- Replicate variables (custom properties) defined in styles.css as required
footer_height = 24    # The height of an h5


def footer():
    footer = dmc.Footer(
        height=footer_height,
        fixed=True,
        children=[
            dmc.Title("Footer area", order=5,
                      style={"color":"black", "text-decoration":"none"})
        ],
        className="page-footer",
    )
    return footer
