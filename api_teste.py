import requests
import json
import csv
import pandas as pd
from PIL import Image
from io import BytesIO

#VARIABLES--------------------------------------------------------------------------
name_json = "fechamento_dias_USD_BRL.json"


#URL REQUESTS------------------------------------------------------------------------ 
json_request = requests.get('https://economia.awesomeapi.com.br/json/USD-BRL/3')
img_request = 'https://images.pexels.com/lib/api/pexels-white.png'


#CREATE A FILE BASED ON A JSON API--------------------------------------------------- WORKED
def create_json_file_with_api(url,name_json):
    with open(name_json, 'w') as f:
        json.dump(url.json(), f, indent=4)
        print("The json file is created")


#OPEN IMAGE FROM API ---------------------------------------------------------------- WORKED
def img_with_api(img_api):
    response = requests.get(img_api)
    img_api = Image.open(BytesIO(response.content))
    img_api.show()

#TRANSFORMING JSON IN CSV ------------------------------------------------------- WORKED
def trans_json_to_scv(name_json):
    dfcsv = pd.read_json (r'' + name_json)
    dfcsv.to_csv (r'json_csv.csv', index = None)


#TRANSFORMING CSV IN JSON ------------------------------------------------------- FAILED
def trans_csv_to_json():
    dfjson = pd.read_csv (r'json_csv.csv')
    dfjson.to_json (r'csv_json.json')


#FUNCTIONS -------------------------------------------------------------------------    
# create_json_file_with_api(json_request,name_json)

#img_with_api(img_request)

#trans_json_to_scv(name_json)

trans_csv_to_json()