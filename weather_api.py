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

# the forecast function gets the current data
# bur I created that function before the other one,
# so I will mantain in that way 'cause I'm lazy
# That function could be replaced by acessing
# the index 0 of the "response_daily" variable


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


def get_forecast_data(lat=-29.82, lon=-51.15):

    forecast_url = BASE_URL + \
        f"onecall?lat={lat}&lon={lon}&exclue=hourly,minutely" + \
        f"&lang=pt_BR&units=metric&&appid={API_KEY}"

    response = requests.get(forecast_url).json()

    responses_daily = response["daily"]

    # Getting tomorrow data
    response_daily_tomorrow = responses_daily[1]
    tomorrow_temp_min = response_daily_tomorrow["temp"]["min"]
    tomorrow_temp_max = response_daily_tomorrow["temp"]["max"]
    # tomorrow_temp_day = response_daily_tomorrow["temp"]["day"]
    tomorrow_humidity = response_daily_tomorrow["humidity"]
    tomorrow_condition = response_daily_tomorrow["weather"][0]["description"]
    tomorrow_icon = response_daily_tomorrow["weather"][0]["icon"]
    tomorrow_date = convert_timestamp_to_str(response_daily_tomorrow["dt"])

    # I made dictionaries here 'cause
    # I thought it would be better readable, maybe I was wrong

    tomorrow_data = {
        "tomorrow_temp_min": tomorrow_temp_min,
        "tomorrow_temp_max": tomorrow_temp_max,
        # "tomorrow_temp_day": tomorrow_temp_day,
        "tomorrow_humidity": tomorrow_humidity,
        "tomorrow_condition": tomorrow_condition,
        "tomorrow_icon": ICON_TO_EMOJI[tomorrow_icon],
        "tomorrow_date": tomorrow_date
    }

    # Getting after tomorrow data
    response_daily_after_tomorrow = responses_daily[2]
    after_tomorrow_temp_min = response_daily_after_tomorrow["temp"]["min"]
    after_tomorrow_temp_max = response_daily_after_tomorrow["temp"]["max"]
    # after_tomorrow_temp_day = response_daily_after_tomorrow["temp"]["day"]
    after_tomorrow_humidity = response_daily_after_tomorrow["humidity"]
    after_tomorrow_condition = response_daily_after_tomorrow["weather"][0]
    after_tomorrow_condition = after_tomorrow_condition["description"]
    after_tomorrow_icon = response_daily_after_tomorrow["weather"][0]["icon"]
    after_tomorrow_date = convert_timestamp_to_str(
        response_daily_after_tomorrow["dt"])

    after_tomorrow_data = {
        "after_tomorrow_temp_min": after_tomorrow_temp_min,
        "after_tomorrow_temp_max": after_tomorrow_temp_max,
        # "after_tomorrow_temp_day": after_tomorrow_temp_day,
        "after_tomorrow_humidity": after_tomorrow_humidity,
        "after_tomorrow_condition": after_tomorrow_condition,
        "after_tomorrow_icon": ICON_TO_EMOJI[after_tomorrow_icon],
        "after_tomorrow_date": after_tomorrow_date
    }

    full_forecast_data = {
        "tomorrow_data": tomorrow_data,
        "after_tomorrow_data": after_tomorrow_data
    }
    return full_forecast_data


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
    print(get_lon_and_lat("Sapucaia do Sul", "RS"))
