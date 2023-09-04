
#By: Nicholas Odeh
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

data = pd.read_csv('historical_automobile_sales.csv')  # Replace with your dataset file

app = dash.Dash(__name__)

#title of Dashbord
app.title = "Automobile Sales Statistics Dashboard"

# unique years for the select-year dropdown
years_list = data['Year'].unique()

app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard", style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 24}),

    #drop-down menus
    dcc.Dropdown(id='dropdown-statistics',
                 options=[
                     {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                     {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                 ],
                 placeholder='Select a report type',
                 style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlignLast': 'center'}),

    # TASK 2.2: Add a second dropdown menu for selecting the year
    dcc.Dropdown(id='select-year', options=[{'label': year, 'value': year} for year in years_list],
                 placeholder='Select a year', disabled=False,
                 style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlignLast': 'center'}),

    # Line chart to display automobile sales over time
    dcc.Graph(id='automobile-sales-line-chart')
])


#Callbacks to enable/disable the input container and display the line chart
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_value):
    return False if selected_value == 'Yearly Statistics' else True


@app.callback(
    Output(component_id='automobile-sales-line-chart', component_property='figure'),
    Input(component_id='dropdown-statistics', component_property='value'),
    Input(component_id='select-year', component_property='value')
)
def update_automobile_sales_chart(selected_report, selected_year):
    if selected_report == 'Yearly Statistics':
        # Filter data based on the selected year if needed
        if selected_year:
            filtered_data = data[data['Year'] == int(selected_year)]
        else:
            filtered_data = data

        #Plotly Express line chart
        fig = px.line(filtered_data, x='Year', y='Automobile_Sales', title='Automobile Sales Over Time')
        return fig
    elif selected_report == 'Recession Period Statistics':
        # Filter data for recession years (Recession = 1)
        recession_data = data[data['Recession'] == 1]

        # Recession period statistics line chart
        fig = px.line(recession_data, x='Year', y='Automobile_Sales', title='Automobile Sales During Recessions')
        return fig
    else:
        return px.line()  # Returns a empty line chart


if __name__ == '__main__':
    app.run_server(debug=True)












