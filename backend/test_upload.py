import requests

url = "http://127.0.0.1:5000/api/upload-image"

file_path = r"D:\OneDrive\Pictures\14.jpg"

with open(file_path, "rb") as f:
    files = {"image": f}
    response = requests.post(url, files=files)

print(response.json())
