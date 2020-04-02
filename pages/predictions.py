# YC list page
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px 
# Imports from this application
from app import app

# import data
yc = pd.read_csv('https://raw.githubusercontent.com/masonnystrom/project-2/master/notebooks/yc.csv')

# create a df for every cohort
S05 = yc[yc['yc_cohort'] == 'YC S05']
W06 = yc[yc['yc_cohort'] == 'YC W06']
S06 = yc[yc['yc_cohort'] == 'YC S06']
W07 = yc[yc['yc_cohort'] == 'YC W07']
S07 = yc[yc['yc_cohort'] == 'YC S07']
W08 = yc[yc['yc_cohort'] == 'YC W08']
S08 = yc[yc['yc_cohort'] == 'YC S08']
W09 = yc[yc['yc_cohort'] == 'YC W09']
S09 = yc[yc['yc_cohort'] == 'YC S09']
W10 = yc[yc['yc_cohort'] == 'YC W10']
S10 = yc[yc['yc_cohort'] == 'YC S10']
W11 = yc[yc['yc_cohort'] == 'YC W11']
S11 = yc[yc['yc_cohort'] == 'YC S11']
W12 = yc[yc['yc_cohort'] == 'YC W12']
S12 = yc[yc['yc_cohort'] == 'YC S12']
W13 = yc[yc['yc_cohort'] == 'YC W13']
S13 = yc[yc['yc_cohort'] == 'YC S13']
W14 = yc[yc['yc_cohort'] == 'YC W14']
S14 = yc[yc['yc_cohort'] == 'YC S14']
W15 = yc[yc['yc_cohort'] == 'YC W15']
S15 = yc[yc['yc_cohort'] == 'YC S15']
W16 = yc[yc['yc_cohort'] == 'YC W16']
S16 = yc[yc['yc_cohort'] == 'YC S16']
W17 = yc[yc['yc_cohort'] == 'YC W17']
S17 = yc[yc['yc_cohort'] == 'YC S17']
W18 = yc[yc['yc_cohort'] == 'YC W18']
S18 = yc[yc['yc_cohort'] == 'YC S18']

drop_options =[S05, W06, S06, W07, S07, W08, S08, W09, S09, W10, S10,
W11, S11, W12, S12, W13, S13, W14, S14, W15, S15, W16, S16, W17, S17, W18, S18,]

cohorts = [{'label': cohort, 'value': cohort} for cohort in yc['yc_cohort'].unique().tolist()]

column1 = dbc.Col([
        dcc.Markdown(
            """
            ## List of Y-Combinator Companies
            """
        ),

        dcc.Dropdown(
            id='cohorts',
            options = cohorts,
            placeholder='Select YC cohort',
            value = 'YC S18'
        ),
        dcc.Graph(id='cohort_plot')
    ])


@app.callback(Output('cohort_plot', 'figure'), [Input('cohorts', 'value')])
def call(value):
    subset = yc[yc['yc_cohort'] == value]
    return px.bar(subset, x='total_funding', y='company', orientation='h')

layout = dbc.Row([column1])