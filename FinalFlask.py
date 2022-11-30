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

#Creation of the Dash app and Route to /dash/
app = Flask('BZAN545Project')

# Pulling from PostgreSQL Server
database = {'user': 'postgres',
                'pass': 
                

                
                #INSERT PASSWORD FOR POSTGRES HERE
                'book', 
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




#New Route for the Data Table
@app.route('/singleset')
def singleset():
    pgConnection = psycopg2.connect(pgConnectString)
    query = "select * from bzan545masterdata order by random() limit 10;"
    df = pd.read_sql_query(query, pgConnection)
    pgConnection.close()
    df = pd.DataFrame.to_csv(df)
    return df

@app.route('/complete')
def complete():   
    pgConnection = psycopg2.connect(pgConnectString)
    query = "select * from bzan545masterdata;"
    df = pd.read_sql_query(query, pgConnection)
    pgConnection.close()
    df = pd.DataFrame.to_csv(df)
    return df

@app.route('/completedisplay')
def completedisplay():   
    pgConnection = psycopg2.connect(pgConnectString)
    query = "select * from bzan545masterdata;"
    df_bar3 = pd.read_sql_query(query, pgConnection)
    pgConnection.close()
    df = pd.DataFrame(df_bar3)
    return render_template("datatable.html", column_names=df.columns.values, row_data=list(df.values.tolist()), link_column="productid", zip=zip)