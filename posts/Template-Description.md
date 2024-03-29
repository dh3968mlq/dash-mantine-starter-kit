## Template description

Code on [Gitgub](https://github.com/dh3968mlq/dash-mantine-starter-kit)

![Example image](/static/pexels-pixabay-147411_cropped.png)   

[Dash](https://dash.plotly.com/) allows [multi-page web apps](https://dash.plotly.com/)
to be programmed (almost entirely) in Python

[Dash Mantine Components](https://www.dash-mantine-components.com/)
wraps the [Mantine](https://mantine.dev/) React components library

### This template

* Implements a basic responsive design
* Draws on the much more complex [code for the Dash Mantine Components Documentation](https://github.com/snehilvj/dmc-docs)
* Is implemented almost entirely in Python using
    * [Dash](https://dash.plotly.com/urls)
    * [Dash Pages](https://dash.plotly.com/urls) to create a multi-page app
    * [Dash Mantine Components](https://www.dash-mantine-components.com/)
* Uses the Dash Mantine Components default light theme
    * A one-line change is needed to change it to the dark theme
* Responds to screen size. On narrower screens:
    * The right sidebar disappears
    * The left sidebar is replaced by a pop-up drawer
    * The title becomes shorter and smaller
* Allows flexible control of the sidebar content
    * The left sidebar can share some, all or none of its content with the pop-up that replaces it on a small screen
    * Pages can have customised left or right sidebars and/or pop-ups
* Shows a simple Plotly interactive graph
    * On narrow screens, controls can be moved to, or duplicated on, the pop-up sidebar 
* Autogenerates content from Markdown files
    * This uses [DH's fork of markdown2dash](https://github.com/dh3968mlq/markdown2dash),
included as a Git submodule at present
* Is configured for deployment on Heroku
* Is not configured as a PyPI package. 
    * Just download any code you're interested in and modify it as you please

### This page

The content of this page is stored as *posts/Template-Description.md* and is automatically 
converted for display by *pages/autogenerate.py*, execution of which is 
triggered on load by the Dash multi-page mechanism.


