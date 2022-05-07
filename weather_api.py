import requests
from datetime import datetime
from bot import API_KEY
import matplotlib.pyplot as plt

BASE_URL = "https://api.openweathermap.org/data/2.5/"

ICON_TO_EMOJI = {
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": u"\U0001F327",
    "10d": u"\U0001F326",
    "11d": "⛈",
    "13d": "❄️",
    "50d": u"\U0001F32B",
    "01n": u"\U0001F311",
    "02n": u"\U0001F311" + " ☁",
    "03n": "☁️",
    "04n": "️️☁☁",
    "09n": u"\U0001F327",
    "10n": "☔️",
    "11n": "⛈",
    "13n": "❄️",
    "50n": u"\U0001F32B"
}


def convert_timestamp_to_str(timestamp):
    date = datetime.fromtimestamp(timestamp)
    date_str = datetime.strftime(date, r"%d/%m/%Y - %H:%M")

    return date_str


def get_hour_timestamp(timestamp):
    date = datetime.fromtimestamp(timestamp)
    date_str = datetime.strftime(date, r"%d/%H")

    return date_str


def get_current_data(city, state, country):

    current_url = BASE_URL + f"weather?q={city},{state},{country}" + \
        f"&exclue=hourly,minutely&lang=pt_BR&units=metric&&appid={API_KEY}"

    response = requests.get(current_url).json()
    main_response = response["main"]
    current_temp = main_response["temp"]
    temp_min = main_response["temp_min"]
    temp_max = main_response["temp_max"]
    current_humidity = main_response["humidity"]
    current_condition = response["weather"][0]["description"]
    current_icon = response["weather"][0]["icon"]
    current_date = convert_timestamp_to_str(response["dt"])

    current_data = {
        "current_temp": current_temp,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "current_humidity": current_humidity,
        "current_condition": current_condition,
        "current_icon": ICON_TO_EMOJI[current_icon],
        "current_date": current_date
    }

    return current_data


def get_hourly_data_graph(lat=-29.820, lon=-51.158):
    full_url = BASE_URL + \
        f"onecall?lat={lat}&lon={lon}&exclue=minutely" + \
        f"&lang=pt_BR&units=metric&&appid={API_KEY}"

    data_x = []
    data_y = []
    responses = requests.get(full_url).json()
    day, _ = get_hour_timestamp(responses["hourly"][0]["dt"]).split('/')
    for response in responses["hourly"]:
        new_day, new_hour = get_hour_timestamp(response["dt"]).split('/')
        new_hour = int(new_hour)
        if day == new_day:
            data_x.append(new_hour)
            temp = response["temp"]
            data_y.append(int(temp))

    x_min = data_x[0] + 0.5
    x_max = 24 + 0.5
    plt.xlim(x_min, x_max)
    plt.grid(True)
    plt.xlabel("Horário")
    plt.ylabel("Temperatura em °C")
    plt.scatter(data_x, data_y)
    plt.savefig("temperature_graph.png")
    plt.close()


def get_lon_and_lat(city, state) -> tuple:
    full_url = BASE_URL + f"weather?q={city},{state},BR&&appid={API_KEY}"
    response = requests.get(full_url).json()
    lon, lat = response["coord"].values()
    return lon, lat


if __name__ == "__main__":
    print(get_current_data("Ribeirão Preto", "RS", "BR"))
