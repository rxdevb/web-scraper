import requests
print("Hello from inside a Docker container!")
print("Fetching Google's homepage...")
try:
    response = requests.get("https://www.google.com", timeout=5)
    print(f"Successfully fetched a page with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
