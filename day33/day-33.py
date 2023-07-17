import requests


response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response)
print(response.status_code)
response.raise_for_status()
# 1xx: hold on 
# 2xx: here you go 
# 3xx: go away 
# 4xx: you screwed up
# 5xx : i screwed up

# data = response.json()["iss_position"]["longitude"]
# print(data)
longitude = response.json()["iss_position"]["longitude"] 
latitude = response.json()["iss_position"]["latitude"] 
iss_position = (longitude, latitude)
print(iss_position)


