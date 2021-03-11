import requests



response = requests.get(url="http://localhost:5033/animals")

print(response.status_code)
print(response.json())
print(response.headers)

response = requests.get(url="http://localhost:5033/animals/arms/10")

print(response.status_code)
print(response.json())
print(response.headers)

response = requests.get(url="http://localhost:5033/animals/contains/bird")

print(response.status_code)
print(response.json())
print(response.headers)
