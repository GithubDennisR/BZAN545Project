from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
from datetime import datetime
import numpy as np
import plotly.io as pio
pio.templates

df = pd.read_csv("C:\\Users\\denni\\Desktop\\TempValues\\DATA1.csv", header = 0)
df = pd.DataFrame(df)
df["itemssold"] = pd.to_numeric(df['itemssold'])
app = Dash(__name__)
df1 = df.groupby('salesdate', as_index=False)['itemssold'].mean().dropna()
df2 = df.groupby(['salesdate','region'], as_index=False)['itemssold'].mean().dropna()
fig = px.line(df1, x="salesdate", y="itemssold", labels=dict(salesdate="Date of Sale", itemssold="Average # of Items Sold"), template = 'plotly_dark')
app.layout = html.Div([
    html.Div(
        html.Nav(
            className = "blue",
            children = [
                html.Div(
                    className = "nav-wrapper container",
                    children = [
                        html.A(
                            className = "brand-logo center",
                            href = "#",
                            children = [
                                html.A("Sales App")
                            ]
                        ),
                        html.Ul(
                            className = "right hide-on-med-and-down",
                            children = [
                                html.Li(
                                    children = [
                                        html.A("Raw Data File")
                                    ]
                                ),
                                html.Li(
                                    children = [
                                        html.A("Dashboard")
                                    ]
                                ),
                                
                            ]
                        )
                    ]
                )
            ]
        )
    ),
    html.Br(),
    html.Div(
        className = "container",
    children = [
        html.H5(
            "Average # of Items Sold Over Time (Among All Regions)",
            className = "black-text center"
        ),
        dcc.Graph(
            id='graph1',
            figure=fig
        )
    ]
    ),
html.Div(
    
        className = "container",
    children = [
    html.H5('Average # of Items Sold by Region Over Time',
    className = "center"),
    dcc.Graph(id="graph"),
    dcc.Dropdown(
        id="checklist",
        options=["a","b","c","d","e"],
        value= "a"
    ),
    ]
),
    html.Div(
        className = "header center orange-text custom",
        children=html.Div([
            html.H5('Overview'),
            html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''')
        ])
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
                                            html.H5("Footer Content")
                                        ]
                                    ),
                                    html.P(
                                        className = "grey-text text-lighten-4",
                                        children = [
                                            html.P("This is Text")
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
                                                        "Link",
                                                        className = "grey-text text-lighten-3",
                                                        href = "#",
                                                    )
                                                ]
                                            ),
                                           html.Li(
                                                children = [
                                                    html.A(
                                                        "Link",
                                                        className = "grey-text text-lighten-3",
                                                        href = "#",
                                                    )
                                                ]
                                            ),
                                           html.Li(
                                                children = [
                                                    html.A(
                                                        "Link",
                                                        className = "grey-text text-lighten-3",
                                                        href = "#",
                                                    )
                                                ]
                                            ),
                                          html.Li(
                                                children = [
                                                    html.A(
                                                        "Link",
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
                                        "Made by TeamWon",
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
    df = pd.read_csv("C:\\Users\\denni\\Desktop\\TempValues\\DATA1.csv", header = 0)
    df2 = df.groupby(['salesdate','region'], as_index=False)['itemssold'].mean().dropna()
    df2['region'] = df['region'].astype('string')
    mask = df2[df2['region'] == sregion]
    fig = px.line(mask, 
        x="salesdate", y="itemssold", labels=dict(salesdate="Date of Sale", itemssold="Average # of Items Sold"), template = 'plotly_dark')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    

