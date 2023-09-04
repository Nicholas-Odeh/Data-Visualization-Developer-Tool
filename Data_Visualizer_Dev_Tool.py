import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import folium


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
response = requests.get(url)


#autosale over time
def automobile_sales_over_time(url):
        #Read data to Pandas
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    print('Data downloaded and read into a dataframe!')
        #line chart
    df_line = df.groupby('Year')['Automobile_Sales'].mean()
    plt.figure(figsize=(10, 6))
    df_line.plot(kind='line')
    plt.xlabel('Year')
    plt.ylabel('Automobile Sales Volume')
    plt.title('Automobile Sales Over Time')
    plt.grid(True)
    plt.show()


#sales difference between cars during recessions
def difference_in_sales_trend_recession(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    df_Mline = df.groupby(['Year','Vehicle_Type'], as_index=False)['Automobile_Sales'].sum()
    df_Mline.set_index('Year', inplace=True)
    df_Mline = df_Mline.groupby(['Vehicle_Type'])['Automobile_Sales']
    df_Mline.plot(kind='line')
    plt.xlabel('Year')
    plt.ylabel('Amount of Sales ')
    plt.title('Sales Trend Vehicle-wise during Recession')
    plt.legend()
    plt.grid(True)
    plt.show()



def avg_diff_in_sales_resynon(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    new_df = df.groupby('Recession')['Automobile_Sales'].mean().reset_index()
    plt.figure(figsize=(10,6))
    sns.barplot(x='Recession', y='Automobile_Sales', hue='Recession',  data=new_df)
    plt.xlabel('State of Economy')
    plt.ylabel('Average Automobile sales')
    plt.title('Average Automobile Sales during Recession and Non-Recession periods')
    plt.xticks(ticks=[0, 1], labels=['Non-Recession', 'Recession'])
    plt.show()


def gdp_vari(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    rec_data = df[df['Recession'] == 1]
    non_rec_data = df[df['Recession'] == 0]
    fig = plt.figure(figsize=(12, 6))

    #2 subploting axies
    ax0 = fig.add_subplot(1, 2, 1)  # add subplot 1 (1 row, 2 columns, first plot)
    ax1 = fig.add_subplot(1,2,2)  # add subplot 2 (1 row, 2 columns, second plot).

    #1st axis, yes recession
    sns.lineplot(x='Year', y='GDP', data=rec_data, label='Recession', ax=ax0)
    ax0.set_xlabel('Year')
    ax0.set_ylabel('GDP')
    ax0.set_title('GDP Variation during Recession Period')

    #2nd axis, no recession
    sns.lineplot(x='Year', y='GDP', data=non_rec_data, label='Non-Recession', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('GDP')
    ax1.set_title('GDP Variation during Non-Recession Period')

    plt.tight_layout()
    plt.grid(True)
    plt.show()


def season_weight(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    non_rec_data = df[df['Recession'] == 0]
    size = non_rec_data['Seasonality_Weight']
    sns.scatterplot(data=non_rec_data, x='Month', y='Automobile_Sales', size=size)
    hue ='Seasonality_Weight'
    legend = (True)
    plt.xlabel('Month')
    plt.ylabel('Automobile_Sales')
    plt.title('Seasonality impact on Automobile Sales')
    plt.show()


def consumer_sales_trust_reces(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    rec_data = df[df['Recession'] == 1]
    plt.figure(figsize=(10,6))
    plt.scatter(rec_data['Consumer_Confidence'], rec_data['Automobile_Sales'])

    plt.xlabel('Consumer confidence')
    plt.ylabel('Automobile sales')
    plt.title('Consumer Confidence and Automobile Sales during Recessions')
    plt.show()



def avg_car_price_and_sale_yes_rec(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    rec_data = df[df['Recession'] == 1]
    plt.figure(figsize=(10,6))
    plt.scatter(rec_data['Price'], rec_data['Automobile_Sales'])

    plt.xlabel('Price in USD')
    plt.ylabel('Automobile sales')
    plt.title('Relationship between Average Vehicle Price and Sales during Recessions')
    plt.show()

def avg_car_price_and_sale_yes_rec(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    Rdata = df[df['Recession'] == 1]
    NRdata = df[df['Recession'] == 0]
 # Calculate the total advertising expenditure for both periods
    RAtotal = Rdata['Advertising_Expenditure'].sum()
    NRAtotal = NRdata['Advertising_Expenditure'].sum()
# Create a pie chart for the advertising expenditure
    plt.figure(figsize=(8, 6))
    labels = ['Recession', 'Non-Recession']
    sizes = [RAtotal, NRAtotal]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Advertising Expenditure during Recession and Non-Recession Periods')
    plt.show()

def vechicle_total_share(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    Rdata = df[df['Recession'] == 1]
    VTsales = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()
    plt.figure(figsize=(8, 6))
    labels = VTsales.index
    sizes = VTsales.values
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Share of Each Vehicle Type in Total Sales during Recessions')
    plt.show()

def unemployment_vs_sales(url):
    text = io.StringIO(response.text)
    df = pd.read_csv(text)
    data = df[df['Recession'] == 1]
    plt.figure(figsize=(12, 4))
    sns.countplot(data=data, x='unemployment_rate', hue='Vehicle_Type')
    plt.xlabel('Unemployment Rate')
    plt.ylabel('Count')
    plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
    plt.legend(loc='upper right')
    plt.show()



#Calls the creation of graphs from functions
#remove the # to call for that graphs creation

#automobile_sales_over_time(url)
#difference_in_sales_trend_recession(url)
#avg_diff_in_sales_resynon(url)
#gdp_vari(url)
#season_weight(url)
#consumer_sales_trust_reces(url)
#avg_car_price_and_sale_yes_rec(url)
#vechicle_total_share(url)
#unemployment_vs_sales(url)






