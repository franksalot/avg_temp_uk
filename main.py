import pandas as pd
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

avg_temp = pd.read_csv('uk_avg_temperature.csv')

simple_df = avg_temp[(avg_temp.DATATYPE == 'tmax')  & (avg_temp.YEAR < 2021)]
fig = px.scatter(simple_df, x='YEAR', y='RELATIVE_TEMP', trendline='ols', color='RELATIVE_TEMP', title="AVG max temp compared to the mean temp in the UK (C)")

simple_df2 = avg_temp[(avg_temp.DATATYPE == 'tmin') & (avg_temp.YEAR < 2021)]
fig2 = px.scatter(simple_df2, x='YEAR', y='RELATIVE_TEMP',  trendline='ols', color='RELATIVE_TEMP', title="AVG min temp compared to the mean temp in the UK (C)")

fig3 = px.bar(avg_temp, x='YEAR', y='RELATIVE_TEMP', color='RELATIVE_TEMP', title="AVG max & min temp compared to the mean temp in the UK (C)")

    
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig)
        ], className="six columns"),

    html.Div([
            dcc.Graph(figure=fig2)
        ], className="six columns"),
    html.Div([
            dcc.Graph(figure=fig3)
        ], className="six columns"),
    ], className="row")
])


if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 5000))
    #app.run_server(debug=False)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
