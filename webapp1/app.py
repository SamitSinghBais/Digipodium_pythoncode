from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import numpy as np

app = Flask(__name__)
def load_data():
    df = px.data.gapminder()
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphs')
def view_graphs():
    return render_template('graphs_html')

@app.route('/analysis')
def view_analysis1():
    df = load_data()
    country = 'India'
    cdf = df.query('counrty == @country').copy()
    if cdf.shape[0] == 0:
        print('no data in cpuntry:{}'.format(country))
    else:
        fig = px.bar(cdf,x='year',)
    return render_template('expression')

@app.route('/upload/image')
def fill_form():
    return render_template('expression')






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 