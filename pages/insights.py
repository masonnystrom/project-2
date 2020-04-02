# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd 
# Imports from this application
from app import app

yc = pd.read_csv('https://raw.githubusercontent.com/masonnystrom/project-2/master/notebooks/yc.csv')
top100 = yc[['total_funding', 'company', 'exit_value', 'yc_cohort']].sort_values(by='total_funding', ascending=False)[:100]

import plotly.express as px 
gapminder = px.data.gapminder()
fig = px.bar(top100, x="total_funding", y="company", orientation='h',
           hover_name="company", width=1200, height=2400)
fig.update_layout(
        xaxis_title="Total Funding Over Time",
        yaxis_title="Top 100 YC Companies",
        font=dict( family="Open Sans", size=16)
        ),
fig.update_layout(
    title={
        'text': "Top 100 YC Companies by Total Funding 2019",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

column1 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)
layout = dbc.Row([column1])