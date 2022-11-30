from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from datetime import datetime
import numpy as np
import plotly.io as pio
import psycopg2
from flask import Flask, render_template
import flask

app = Dash(__name__)

df = pd.read_csv('http://127.0.0.1:5000/complete', delimiter=',')
# df = pd.read_csv("C:\\Users\\denni\\Desktop\\BZAN545ProjectModify\\bzan545masterdata.csv", header = 0)
df = pd.DataFrame(df)
df["itemssold"] = pd.to_numeric(df['itemssold'])
df1 = df.groupby('salesdate', as_index=False)['itemssold'].mean().dropna()
df2 = df.groupby(['salesdate','region'], as_index=False)['itemssold'].mean().dropna()
df3 = df.groupby(['region'], as_index=False)['itemssold'].sum()
fig = px.line(df1, x="salesdate", y="itemssold", labels=dict(salesdate="Date of Sale", itemssold="Average # of Items Sold"), template = 'plotly_dark')
fig2 = px.bar(df3, x="region", y="itemssold", color = "region", labels=dict(region="Region", itemssold="Total # of Items Sold"), template = 'plotly_dark')
app.layout = html.Div([
    html.Div(
        html.Nav(
            className = "smokey-grey",
            children = [
                html.Div(
                    className = "nav-wrapper container",
                    children = [
                        html.A(
                            className = "brand-logo center",
                            href = "#",
                            children = [
                                html.A("Sales App",
                                className = "orange-text")
                            ]
                        ),
                        html.Ul(
                            className = "right hide-on-med-and-down",
                            children = [
                                html.Li(
                                    children = [
                                        html.A("Formatted Data File",
                                        href = 'http://127.0.0.1:5000/completedisplay',
                                        target = '_blank'),
                                    ]
                                ),
                                html.Li(
                                    children = [
                                        html.A("Raw Data File",
                                        href = 'http://127.0.0.1:5000/complete',
                                        target = '_blank')
                                    ]
                                ),
                                
                            ]
                        )
                    ]
                )
            ]
        )
    ),
html.Div(
    className = "container",
    children = [
        html.Div(
        className = "card-panel smokey-grey",
        children = [
            html.Div(
    
        # className = "container",
    children = [
    html.H5('Average # of Items Sold by Region Over Time',
    className = "center orange-text"),
    dcc.Graph(id="graph"),
    html.H5("Select a Region",
    className = "titlepadding orange-text"),
    dcc.Dropdown(
        id="checklist",
        options=["a","b","c","d","e"],
        value= "a"
    )
        
    
    ]
),
        ]
        )
    ]
),
html.Div(
    className = "container",
    children = [
        html.Div(
        className = "card-panel smokey-grey",
        children = [
            html.Div(
        # className = "container",
    children = [
        html.H5(
            "Average # of Items Sold Over Time (Among All Regions)",
            className = "orange-text center"
        ),
        dcc.Graph(
            id='graph1',
            figure=fig
        )
    ]
    ),
        ]
        )
    ]
),
html.Div(
    className = "container",
    children = [
        html.Div(
        className = "card-panel smokey-grey",
        children = [
            html.Div(
        # className = "container",
    children = [
        html.H5(
            "Total Sales by Region",
            className = "orange-text center"
        ),
        dcc.Graph(
            id='graph1',
            figure=fig2
        )
    ]
    ),
        ]
        )
    ]
),
    html.Footer(
        className = "page-footer",
        children = [
            html.Div(
                className = "container",
                children = [
                    html.Div(
                        className = "row",
                        children = [
                            html.Div(
                                className = "col l6 s12",
                                children = [
                                    html.H5(
                                        className = "white-text",
                                        children = [
                                            html.H5("Sales App")
                                        ]
                                    ),
                                    html.P(
                                        className = "grey-text text-lighten-4",
                                        children = [
                                            html.P("Created for BZAN 545 Fall 2022")
                                        ]
                                    )
                                ]
                            ),
                            html.Div(
                                className ="col l4 offset-l2 s12",
                                children = [
                                    html.H5(
                                        className = "white-text",
                                        children = [
                                            html.H5("Links")
                                        ]
                                    ),
                                    html.Ul(
                                        children = [
                                            html.Li(
                                                children = [
                                                    html.A(
                                                         "Github Repo",
                                                        className = "grey-text text-lighten-3",
                                                        href = "https://github.com/GithubDennisR/BZAN545Project",
                                                        target="_blank",
                                                    )
                                                ]
                                            ),
                                           html.Li(
                                                children = [
                                                    html.A(
                                                        # "Link",
                                                        className = "grey-text text-lighten-3",
                                                        href = "#",
                                                    )
                                                ]
                                            ),
                                           html.Li(
                                                children = [
                                                    html.A(
                                                        # "Link",
                                                        className = "grey-text text-lighten-3",
                                                        href = "#",
                                                    )
                                                ]
                                            ),
                                          html.Li(
                                                children = [
                                                    html.A(
                                                        # "Link",
                                                        className = "grey-text text-lighten-3",
                                                        href = "#",
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            ),
                        ]
                    )
                ]
            ),
            html.Div(
                                className = "footer-copyright",
                                children = [
                                    html.Div(
                                        "Copyright 2022 The Winning Trivia Team",
                                        className = "container",
                                    ),
                                ]
                            )
        ]
    )
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(sregion):
    global df
    df2 = df.groupby(['salesdate','region'], as_index=False)['itemssold'].mean().dropna()
    df2['region'] = df['region'].astype('string')
    mask = df2[df2['region'] == sregion]
    fig = px.line(mask, 
        x="salesdate", y="itemssold", labels=dict(salesdate="Date of Sale", itemssold="Average # of Items Sold in Region"), template = 'plotly_dark')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)  
