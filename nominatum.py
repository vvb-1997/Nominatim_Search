import pandas as pd
import os

dir="Provdie Current working directory"
os.chdir(dir)

path=os.path.join(os.getcwd(),"file","filename.xlsx")

xls=pd.ExcelFile(path)
data=pd.read_excel(xls,'Address_checked')

data=data.dropna(subset=['Final_Latitude','Final_Longitude'])

from geopy.geocoders import Nominatim
geolocator = Nominatim(timeout=None,user_agent="my-application" )
coun=[]
for index,rows in data.iterrows():
    if((rows["Final_Latitude"]!="not found")|(rows["Final_Longitude"]!="not found")):
        lat=rows['Final_Latitude']
        lon=rows['Final_Longitude']
        location = geolocator.reverse((lat,lon),language='en')
        e=location.raw
        country=e['address']['country']
        coun.append(country)
        print(country)
        print("-------------") 
        data.loc[index,'Country']=e['address']['country'] 

        
#provide path to save the dataframe in excel or csv format
if not os.path.exists(os.path.join(os.getcwd(),"file","filename_with_address.xlsx")):
    new_path=os.path.join(os.getcwd(),"file","filename_with_address.xlsx")
    os.makedirs(os.path.join(os.getcwd(),"file","filename_with_address.xlsx"))
    
with pd.ExcelWriter(new_path) as writer:  
    data.to_excel(writer, sheet_name='Updated')
    writer.save()
