#Imports
import dash
from dash import html
import flask
from dash import Dash,html,dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from flask import Flask, render_template
import psycopg2

#Server/Flask App Creation
server = flask.Flask(__name__)

#Base Server Route Created 
@server.route("/")
def index():
    #Returns a Template Home Page Created in HTML
    return render_template("index.html")

#Creation of the Dash app and Route to /dash/
app = dash.Dash(server=server, routes_pathname_prefix="/dash/")

# Pulling from PostgreSQL Server
database = {'user': 'postgres',
                'pass': 
                

                
                #INSERT PASSWORD FOR POSTGRES HERE
                '062400Ds', 
                #INSERT PASSWORD FOR POSTGRES HERE


            'name': 'postgres',
            'name': 'postgres',
            'host': 'localhost',
            'port': '5432'}

pgConnectString = f"""host={database['host']}
                      port={database['port']}
                      dbname={database['name']}
                      user={database['user']}
                      password={database['pass']}"""

pgConnection = psycopg2.connect(pgConnectString)

query = "select * from bzan545masterdata;"

df_bar2 = pd.read_sql_query(query, pgConnection)

#Data Manipulation
df_bar2['itemssold'] = df_bar2['itemssold'].astype(int)
df_bar2['salesdate'] = pd.to_datetime(df_bar2['salesdate'])

dffig1 = df_bar2.groupby(by='region',as_index=False).sum()

dffig2 = df_bar2.groupby(by= 'salesdate').sum().reset_index()

dffig3 = df_bar2.sort_values(by = 'salesdate')

#Figure creation for Example 1
fig = px.bar(dffig1, x="region", y="itemssold", title = 'Items Sold by Region', color =  'region')

#Figure creation for Example 2
fig2 = px.line(dffig2,x="salesdate", y= 'itemssold', title="Items sold over time")

#This part creates the actual layout of the dashboard
app.layout = html.Div(children=[
    # DIV devides up the different sections of the dash
    html.Div([
        html.H1(children='Dashboard Application', style = {"text-align":"center", "background":"#ff8200", "padding":"20px", "border": "4px solid #58595b", "color" : "white"}), 
        html.Div([
            html.A(children = [
            html.Button(children = "Back Home", style= {
            "border":  "2px solid #58595b",
            "color": "#58595b",
            "padding": "10px 20px",
            "text-align": "right",
            "text-decoration": "none",
            "display": "inline-block",
            "font-size": "20px",
            "margin": "4px 2px",
            "cursor": "pointer",
            "background-color": "white",
            'text-align': "right",
            'font-family': "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif"})
            ], href = '/')],
            style= {"text-align":"center"})]),

    # DIV devides up the different sections of the dash
    html.Div([
        html.H1(children='Items Sold Per Region'),

        html.Div(children='''
            Example 1: This is the number of items sold per different region.
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig
        ),  
    ]),
    # New Div for the next figure
    html.Div([
        html.H1(children='Total Items Sold Over Time'),

        html.Div(children='''
            Example 2: This is the amount of items sold over the given period of time
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
], style={'marginBottom': 50, 'marginTop': 25, 'font-family': "'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif"})

#Runs application
if __name__ == "__main__":
    app.run_server(debug=True)

#New Route for the Data Table
@server.route('/data', methods=("POST", "GET"))
def datatable():
    #Grabs data from database updated daily and creates PostgresSQL Table
    database = {'user': 'postgres',
                'pass': 
                

                
                #INSERT PASSWORD FOR POSTGRES HERE
                '062400Ds', 
                #INSERT PASSWORD FOR POSTGRES HERE


            'name': 'postgres',
            'host': 'localhost',
            'port': '5432'}
    pgConnectString = f"""host={database['host']}
                      port={database['port']}
                      dbname={database['name']}
                      user={database['user']}
                      password={database['pass']}"""

    pgConnection = psycopg2.connect(pgConnectString)

    query = "select * from bzan545masterdata;"

    df_bar3 = pd.read_sql_query(query, pgConnection)
    df = pd.DataFrame(df_bar3)

    #Returns in an HTML format decided by datatable.html
    return render_template("datatable.html", column_names=df.columns.values, row_data=list(df.values.tolist()), link_column="productid", zip=zip)

