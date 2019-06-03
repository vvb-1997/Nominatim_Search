# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:42:17 2019

@author: VBhat
"""

import pandas as pd
import numpy as np

path=r"D:\try\international\files\updated_files\GAM_INTL_data(04-09-19)_Jan-MarchData_validation_cleaned.xlsx"

xls=pd.ExcelFile(path)
data_china=pd.read_excel(xls,'POPAddress_checked')

data_china=data_china[data_china['Exact_lat']=='None']

data_china=data_china.dropna(subset=['Final_Cust_Long'])

#data_china=data_china[data_china['GAM_Region']=='AMEA']

from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=None,user_agent="my-application" )
coun=[]
for index,rows in data_china.iterrows():
    if((rows["Final_Cust_Lat"]!="not found")|(rows["Final_Cust_Long"]!="not found")):
        lat=rows['Final_Cust_Lat']
        lon=rows['Final_Cust_Long']
        location = geolocator.reverse((lat,lon),language='en')
        e=location.raw
        country=e['address']['country']
        coun.append(country)
        print(country)
        print(index)
        print("-------------") 
        data_china.loc[index,'new_Cust_Country']=e['address']['country'] 


with pd.ExcelWriter(r"D:\try\international\files\updated_files\GAM_INTL_data(04-09-19)_Jan-MarchData_validation_cleaned_pop.xlsx") as writer:  
    data_china.to_excel(writer, sheet_name='NNI')
    writer.save()


