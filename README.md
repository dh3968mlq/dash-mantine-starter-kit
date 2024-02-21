# dash-mantine-starter-kit

A starter template app for a responsive multi-page app using Dash Mantine components

Author: David Harris 2024, based on Snehil Vijay's dmc-docs app at https://github.com/snehilvj/dmc-docs 

[Dash](https://dash.plotly.com/) allows [multi-page web apps](https://dash.plotly.com/)
to be programmed (almost entirely) in Python

[Dash Mantine Components](https://www.dash-mantine-components.com/)
wraps the [Mantine](https://mantine.dev/) React components library

This app is deployed on [Heroku](https://dash-mantine-boilerplate-19ffeb1d6cdb.herokuapp.com/). (It may take a few seconds to wake up)

### This template

* Implements a basic responsive design
* Draws on the much more complex [code for the Dash Mantine Components Documentation](https://github.com/snehilvj/dmc-docs)
* Is implemented entirely in Python (except for a one-line example of a Javascript clientside callback) using
    * [Dash](https://dash.plotly.com/urls)
    * [Dash Pages](https://dash.plotly.com/urls) to create a multi-page app
    * [Dash Mantine Components](https://www.dash-mantine-components.com/)
* Uses the Dash Mantine Components default light theme
    * A one-line change is needed to change it to the dark theme
* Responds to screen size. On narrower screens:
    * The right sidebar disappears
    * The left sidebar is replaced by a pop-up drawer
    * The title becomes shorter and smaller
* Autogenerates content from Markdown files
    * This uses [DH's fork of markdown2dash](https://github.com/dh3968mlq/markdown2dash),
included as a Git submodule at present
* Is configured for deployment on Heroku
