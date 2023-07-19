import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

try:
#To get Website data from url
    response=requests.get("https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/")

# parsing the Html
    Html=BeautifulSoup(response.content,'html.parser')
    lastJson=[]
    Contents=Html.find('div',class_="articleContentBody")
    allcontent=Contents.find_all('div',class_="row countdown-item")

    for content in allcontent:
        title=content.find('h2').a.text
        year=content.find('h2').find('span',class_="subtle start-year").text
        rating=content.find('h2').find('span',class_="tMeterScore").text
        ranking=content.find('div',class_="countdown-index").text.split("#")
        lastJson.append({"Ranking":ranking[1],"Title":title,"Year":year,"Rating":rating})
    
    #Convert Json data Excel file
    lastJson=json.dumps(lastJson)
    Df_json=pd.read_json(lastJson)
    Df_json.to_excel('rottentomatoes_Netflix_tvshows.xlsx',sheet_name="Top100 Tv shows")
    # print(lastJson)
        

except Exception as e:
    print(e)




   

# print(content)
