import requests
import json



#input('輸入縣市名：')
where = '新北市'
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-4CCAB314-7BBA-452F-BAF2-8207CB312747'
re = requests.get(url)
alldata = re.json()
data = alldata['records']['location']
for i in data:
  if i['locationName']==where:
    city = i['locationName']
    start = i['weatherElement'][0]['time'][0]['startTime'][0:16]
    end = i['weatherElement'][0]['time'][0]['endTime'][0:16]
    now_weather = i['weatherElement'][0]['time'][0]['parameter']['parameterName']
    pop = i['weatherElement'][1]['time'][0]['parameter']['parameterName'] + '%'
    low = i['weatherElement'][2]['time'][0]['parameter']['parameterName']
    high = i['weatherElement'][4]['time'][0]['parameter']['parameterName'] + '℃'

#print(city+' 目前天氣：'+now_weather+'\n氣溫約'+low+'~'+high+'\n降雨機率：'+pop)
msg = f'{city}\n{start}~{end}\n天氣：{now_weather}\n氣溫約{low}~{high}\n降雨機率：{pop}'

print(msg)

