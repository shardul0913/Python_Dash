import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import flask

app = dash.Dash()
app.layout = html.Div(children=[
                dcc.Input(id='input',value='Enter Text',type='text'),
                html.Div(id='output')
               ])


if __name__ == '__main__':
    app.run_server(debug=True)



