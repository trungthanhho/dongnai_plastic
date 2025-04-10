import requests
from datetime import datetime

# API Key cá nhân
api_key = "c62d144bbb6476ae2a4a0c7c3f24831e"
city = "Bien Hoa"

# URL API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Convert timestamp -> datetime
    timestamp = data['dt']
    date = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    print(f"🗓 Ngày giờ: {date}")
    print(f"🌤 Thời tiết tại {city}:")
    print(f"  - Nhiệt độ: {temp}°C")
    print(f"  - Mô tả: {desc}")
    print(f"  - Độ ẩm: {humidity}%")
    print(f"  - Gió: {wind} m/s")
else:
    print("Lỗi khi gọi API. Mã lỗi:", response.status_code)
