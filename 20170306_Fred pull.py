# -*- coding: utf-8 -*-
"""
20170306

Script to pull macroeconomic indicator data from FRED website though fredapi
Add series name, the FRED code and Divide/None to metric_list to add a new series.

Divide is only for percentages (divide by 100)
-Rob
"""
#welcome
print("Script to pull macroeconomic data from FRED website though fredapi")
print()
print("Initializing...")
print()
#import
from fredapi import Fred
import pandas as pd

#Hello fred. Use you own api!
fred = Fred(api_key='3d13cbf62e6b9da77eae2788ab8bb3cc')

# exhaustive list of series to track
metric_list = {
    'Real GDP percent':['A191RL1Q225SBEA','Divide'],
    'Nominal GDP percent':['A191RP1Q027SBEA','Divide'],
    'Nominal GDP billions':['GDP','None'],
    'Real GDP billions':['GDPC1','None'],
    'CPI inflation all urban':['CPIAUCSL','None'],
    'Industrial Production':['INDPRO','None'],
    'Manufactuers New orders':['NEWORDER','None'],
    'Unemployment rate':['UNRATE','Divide'],
    'U6 Unemployment rate':['U6RATE','Divide'],
    'Retail Sales rsfsxmv dollars':['RSFSXMV','None'],
    'PCE inflation':['PCE','None'],
    'All Employees Total Nonfarm':['PAYEMS','None'],
    'Average Hourly Earnings of All Employees Private':['CES0500000003','None'],
    'Brent crude oil':['MCOILBRENTEU','None'],
    'Case Shiller home price index':['SPCS20RNSA','None'],
    '10-year treasury rate':['GS10','Divide'],
    '1-year treasury rate':['GS1','Divide'],
    '2-year treasury rate':['GS2','Divide'],
    '3-year treasury rate':['GS3','Divide'],
    '5-year treasury rate':['GS5','Divide'],
    'Dow Jones Industrial Average':['M1109BUSM293NNBR','None'],
    'GDP Now':['GDPNOW','Divide'],
    'US Recession Monthly':['USREC','None'],
    'US Recession Quarterly':['USRECQ','None'],
    'Consumer Sentiment':['UMCSENT','None'],
    'Share of GDP Net exports quarterly':['A019RE1Q156NBEA','Divide'],
    'Share of GDP Private domestic investments quarterly':['A006RE1Q156NBEA','Divide'],
    'Share of GDP Personal consumer expenditures quarterly':['DPCERE1Q156NBEA','Divide'],
    'Share of GDP Government expenditure quarterly':['A822RE1Q156NBEA','Divide']   
    }


# show dictionary function
def dict_fun():
    for metric in metric_list:
        print(metric, "=", metric_list[metric][0])

# get data
data_set = {}
for metric in metric_list:
    print("...getting", metric)
    # Main api call
    data_set[metric] = fred.get_series_latest_release(metric_list[metric][0])
    if metric_list[metric][1] == "Divide":
        data_set[metric] = data_set[metric]/100
    print(metric, "updated!")
    print()

# create output dataframe from dictionary
output_df = pd.DataFrame.from_dict(data_set)

# export to file
output_df.to_csv('G:/RevNetworkAnalysis/Economic & Industry Analysis/Projects/FRED data/FRED pull.csv', index = True)

# print done
print("-------------------------------Done!-------------------------------")
