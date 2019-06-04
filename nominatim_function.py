import pandas as pd

def Nominatim(data,new_path):
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

  with pd.ExcelWriter(new_path) as writer:  
      data.to_excel(writer, sheet_name='Updated')
      writer.save()
