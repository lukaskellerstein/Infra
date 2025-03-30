import requests
import os

API_URL = os.environ.get("API_URL", "api") 
API_PORT = int(os.environ.get("API_PORT", 8000))

API_URL = f"http://{API_URL}:{API_PORT}"

car = {"make": "Toyota", "model": "Corolla", "year": 2021}
response = requests.post(f"{API_URL}/cars", json=car)
if response.ok:
    print("Created:", response.json())
else:
    print("API Error:", response.status_code, response.text)

cars = requests.get(f"{API_URL}/cars").json()
print("All cars:", cars)