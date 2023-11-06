import requests

api_url = "http://localhost:3000/info"
response = requests.get(api_url)
data = response.json()
print("Retrieved widget information:")
for widget in data:
    print(f"Widget: {widget['name']}, Color: {widget['color']}")

