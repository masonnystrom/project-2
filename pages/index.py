# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd 

# Imports from this application
from app import app

# import yc csv for data analysis
yc = pd.read_csv('https://raw.githubusercontent.com/masonnystrom/project-2/master/notebooks/yc.csv')


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## About Y-Combinator 

            YC pioneered a startup funding model where they invest 150k into a company for 7% equity. Since 2005, YC holds two classes (summer and winter)
            per year where the YC team mentors young startups for 3 months. At the end of the program, startup founders pitch their companies to
            venture capital investors in hopes of raising more capital. 

            ## YC by the Numbers
            * Over 1800 startups funded
            * YC companies have raised over 40 billion in total funding
            * YC companies have had over 250 exits totalling over 6 billion dollars

            ## What next? 
            Check out some of the charts and graphs that visualize how successful YC has been over the years. Special thanks
            to [Seed DB](https://www.seed-db.com/accelerators/view?acceleratorid=1011) for all the data. 
    

            """
        ),
        dcc.Link(dbc.Button('Check out the Top 100 YC Companies', color='primary'), href='/insights')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(yc, x="total_funding", y="yc_cohort", size="total_funding", color="yc_cohort",
           hover_name="company", width=700, height=1000)
fig.update_layout(
        xaxis_title="Total Funding Over Time",
        yaxis_title="Companies by YC Cohort",
        font=dict( family="Open Sans", size=16)
        ),
fig.update_layout(
    title={
        'text': "YC Companies by Total Funding 2019",
        'y':0.97,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

column2 = dbc.Col(
    [
        
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])