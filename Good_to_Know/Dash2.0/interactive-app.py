# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Output, Input  # pip install dash
import dash_bootstrap_components as dbc    # pip install dash-bootstrap-components

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
mytext = dcc.Markdown(children='yooo', style={'color':''})
myinput = dbc.Input(value="This is soo coool")
radio = dcc.RadioItems(options = ['red','blue','green'])
# Customize your own Layout
app.layout = dbc.Container([mytext, myinput, radio])

# Callback allows components to interact
@app.callback(
    Output(mytext, component_property='children'),
    Output(mytext, component_property='style'),
    Input(myinput, component_property='value'),
    Input(radio, component_property='value')
)
def update_title(user_input, user_color):  # function arguments come from the component property of the Input

    return user_input, {'color':user_color}  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(port=8052)
