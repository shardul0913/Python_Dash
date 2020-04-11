import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import flask
import pandas as pd
import plotly
import random
import plotly.graph_objs as go
from collections import deque

app = dash.Dash()
app.layout = html.Div(children=[
                html.Div(children='''Dash: A web application framework for Python.'''),
                dcc.Input(id='Input',value='',type='text'),
                html.Div(id='Output-graph'),
                dcc.Graph(id='live-graph',animate=True),
                dcc.Interval(id='graph-update',interval=1000,n_intervals = 0)
                ])

@app.callback(Output(component_id='Output-graph',component_property='children'),
              [Input(component_id='Input',component_property='value')])
def graph_update(input_data):
    df = pd.read_excel('demoData.xlsx', index_col=2)
    df.index = pd.to_datetime(df.index)
    return dcc.Graph(
       id='example-graph',
       figure={
             'data':[
                         {'x': df.index, 'y': df[input_data], 'type': 'bar', 'name': 'SF'},
                         # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                     ],
             'layout':{
                         'title': 'Dash Data Visualization'
                     }
            }
    )

@app.callback(Output(component_id='live-graph',component_property='figure'),
              [Input('graph-update', 'n_intervals')])
def graph_update(input_data):
    df = pd.read_excel('demoData.xlsx', index_col=2)
    df.index = pd.to_datetime(df.index)
    return dcc.Graph(
       id='example-graph',
       figure={
             'data':[
                         {'x': df.index, 'y': df[input_data], 'type': 'bar', 'name': 'SF'},
                         # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                     ],
             'layout':{
                         'title': 'Dash Data Visualization'
                     }
            }
    )



if __name__ == '__main__':
    app.run_server(debug=True)



