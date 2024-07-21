import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

response_api =  requests.get('https://api.covid19india.org/state_district_wise.json')
data = response_api.text
parse_json = json.loads(data)
df = pd.DataFrame([parse_json])
 
header={"Accept":"application/json"}
response = requests.request('GET','https://api.covid19india.org/state_district_wise.json', headers=header)
df = pd.read_json(response.json())

dataframe = pd.read_json(parse_json)
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
 
response_api_1 = requests.get('https://api.frankfurter.app/latest')
response_api_2 = requests.get('https://api.frankfurter.app/2010-01-01..2011-01-31')
data = response_api.text
parse_json = json.loads(data)

df = pd.DataFrame()
df = parse_json['rates']
df = pd.read_json(data)
pd.read_json(df['rates'])
df.where('start_date'=='2010-01-04', inplace=True)
df.sort_values('amount')
plt.scatter(df['amount'], df['rates'])
plt.show()

response_api_mcu = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
data =  response_api_mcu.text
parse_json = json.loads(data)
with open( 'C://Users//roddl//OneDrive//Desktop//sample.json', 'r') as f:
    data_new = json.load(f)

df = pd.json_normalize(data_new, record_path=['ID Nation', 'Nation', 'ID Year', 'Year', 'Population', 'Slug Nation'], meta=[['ID Nation', 'Nation', 'ID Year', 'Year', 'Population', 'Slug Nation']])

data = pd.read_json(response_api_mcu.text)
plt.scatter()data['']
data = json.loads(response_api_mcu.text)
df = pd.json_normalize(data)