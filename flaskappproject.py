import dash
from dash import html
import flask
from dash import Dash,html,dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import psycopg2

server = flask.Flask(__name__)

@server.route("/")
def home():
    return "Flask app"

app = dash.Dash()

#Creation of the app with a specific stylesheet
app = dash.Dash(server=server, routes_pathname_prefix="/dash/")

#Example for creating a dataframe
df_bar = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [3, 1, 2, 2, 4, 100],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
#Pulling from Saxon's postgreSQL server
database = {'user': 'postgres',
            'pass': 'bzan545saxon',
            'name': 'postgres',
            'host': 'localhost',
            'port': '5432'}

pgConnectString = f"""host={database['host']}
                      port={database['port']}
                      dbname={database['name']}
                      user={database['user']}
                      password={database['pass']}"""

pgConnection=psycopg2.connect(pgConnectString)

query = "select * from bzan545masterdata;"

df_bar2 = pd.read_sql_query(query, pgConnection)

#Figure creation for example
fig = px.bar(df_bar, x="Fruit", y="Amount", color="City", barmode="group")

#Figure creation for master file - bar chart
fig2 = px.bar(df_bar2, x="region", y="itemssold", barmode="group")

#This part creates the actual layout of the dashboard
app.layout = html.Div(children=[
    # DIV devides up the different sections of the dash
    html.Div([
        html.H1(children='Example Chart For putting in more figures'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig
        ),  
    ]),
    # New Div for the next figure
    html.Div([
        html.H1(children='Items Sold Per Region'),

        html.Div(children='''
            Example 1: This is th items sold per the different region
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
    #This is used to insert photos or pictures if need be
    html.A(
    href="INSERT PHOTO HERE TO LINK TO",
    children=[
        html.Img(
            alt="TEXT HERE",
            src="SRCE IMAGE",
        )
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=False)