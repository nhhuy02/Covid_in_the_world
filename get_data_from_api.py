import requests
import pandas as pd

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

headers = {
    "X-RapidAPI-Key": "b8c473c658msh52f73cd62ccfe35p1e5436jsnb308608f0654",
    "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    countries_stat = data.get('countries_stat', [])
    if countries_stat:
        df = pd.DataFrame(countries_stat)
        
        df.to_excel('covid_data.xlsx', index=False)
    else:
        print("Không có dữ liệu về quốc gia")
else:
    print("Không thể lấy dữ liệu từ API")
