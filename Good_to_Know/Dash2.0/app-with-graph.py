# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Output, Input, html  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components
import plotly.express as px #importing this for graphs 

# incorporate sample data into app
df = px.data.medals_long()

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
mytitle = dcc.Markdown(children='# App that analyzes Olympic medals')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',  # initial value displayed when page first loads
                        clearable=True)

alerts = html.Div(
    [
        dbc.Alert(children = 'Test', color="info"),
        # dbc.Alert("This is a secondary alert", color="secondary"),
        # dbc.Alert("This is a success alert! Well done!", color="success"),
        # dbc.Alert("This is a warning alert... be careful...", color="warning"),
        # dbc.Alert("This is a danger alert. Scary!", color="danger"),
        # dbc.Alert("This is an info alert. Good to know!", color="info"),
        # dbc.Alert("This is a light alert", color="light"),
        # dbc.Alert("This is a dark alert", color="dark"),
    ]
)

# Customize your own Layout
app.layout = dbc.Container([mytitle, alerts, mygraph, dropdown])

# Callback allows components to interact
@app.callback(
    Output(mygraph, component_property='figure'),
    Output(alerts, component_property= 'children'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):  # function arguments come from the component property of the Input
    if user_input == 'Bar Plot':
        fig = px.bar(data_frame=df, x="nation", y="count", color="medal")
        message = 'The data for the bar graph is highly confidential'

    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="count", y="nation", color="medal",
                         symbol="medal")
        message = 'The scatter plot is believed to be first published in 1933'

    return fig, message # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(port=8053)
