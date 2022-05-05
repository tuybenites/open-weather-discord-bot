import discord
from weather_api import get_current_data, get_forecast_data, get_lon_and_lat
from weather_api import get_hourly_data_graph


def embed_weather_current(bot, city, state, country):

    data = get_current_data(
        city, state, country)

    temp, temp_min, temp_max, humidity, condition, icon, date = data.values()

    condition = condition.capitalize()
    embed = discord.Embed(
        title=f"{icon} Clima em {city.capitalize()} {icon}",
        description='''" Prefiro o paraíso pelo clima
        e o inferno pela companhia. "'''.replace('\n', ''),
        color=0x00b0f5,
        url="https://github.com/tuybenites/climatempo-discord-bot"
    )

    embed.set_author(
        name=bot.user.name
    )

    embed.add_field(name="Temperatura mínima 🌡️",
                    value=f" {int(temp_min)}° C")

    embed.add_field(name="Temperatura agora 🌡️",
                    value=f" {int(temp)}° C")

    embed.add_field(name="Temperatura máxima 🌡️",
                    value=f" {int(temp_max)}° C")

    embed.add_field(name="Umidade 💧",
                    value=f" {int(humidity)}%")

    embed.add_field(name="Condição 📝",
                    value=str(condition))

    embed.add_field(name="Data 📅", value=str(date))

    # embed.set_image(url="https://i.imgur.com/sZx6LgU.png")

    lon, lat = get_lon_and_lat(city, state)
    get_hourly_data_graph(lat, lon)
    file = discord.File("temperature_graph.png", filename="graph.png")
    embed.set_image(url="attachment://graph.png")

    embed.set_footer(
        text="Dados retirados da API OpenWeather"
    )

    return embed, file


def embed_weather_forecast(bot, case):

    if case == "amanha":
        temp_min, temp_max, humidity, cond, icon, date = get_forecast_data(
            -29.820, -51.158)["tomorrow_data"].values()
    elif case == "depois_amanha":
        temp_min, temp_max, humidity, cond, icon, date = get_forecast_data(
            -29.820, -51.158)["after_tomorrow_data"].values()

    cond = cond.capitalize()
    embed = discord.Embed(
        title=f"{icon} Clima em Sapucaia do Sul {icon}",
        description='''" Prefiro o paraíso pelo clima
        e o inferno pela companhia. "'''.replace('\n', ''),
        color=0x00b0f5,
        url="https://github.com/tuybenites/climatempo-discord-bot"
    )

    embed.set_author(
        name=bot.user.name
    )
    embed.add_field(name="Umidade 💧",
                    value=f" {int(humidity)}%")

    embed.add_field(name="Temperatura Mínima 🌡️",
                    value=f" {int(temp_min)}° C")

    embed.add_field(name="Temperatura Máxima 🌡️",
                    value=f" {int(temp_max)}° C")

    embed.add_field(name="Condição 📝",
                    value=str(cond))

    embed.add_field(name="Data 📅", value=str(date))

    # embed.set_image(url="https://i.imgur.com/sZx6LgU.png")

    embed.set_footer(
        text="Dados retirados da API OpenWeather"
    )

    return embed
