import pandas as pd
import os

path=os.path.join("file","filename.xlsx")

xls=pd.ExcelFile(path)

data=pd.read_excel(xls,'Address_checked')

data=data[data['Exact_lat']=='None']

data=data.dropna(subset=['Final_Long'])

from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=None,user_agent="my-application" )
coun=[]
for index,rows in data.iterrows():
    if((rows["Final_Lat"]!="not found")|(rows["Final_Long"]!="not found")):
        lat=rows['Final_Lat']
        lon=rows['Final_Long']
        location = geolocator.reverse((lat,lon),language='en')
        e=location.raw
        country=e['address']['country']
        coun.append(country)
        print(country)
        print("-------------") 
        data.loc[index,'Country']=e['address']['country'] 

new_path=os.path.join("file","filename_with_address.xlsx")

with pd.ExcelWriter(new_path) as writer:  
    data.to_excel(writer, sheet_name='Updated')
    writer.save()
