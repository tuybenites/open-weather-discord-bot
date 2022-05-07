import discord
from weather_api import get_current_data, get_lon_and_lat
from weather_api import get_hourly_data_graph


def embed_weather_current(bot, city, state, country):

    data = get_current_data(
        city, state, country)

    temp, temp_min, temp_max, humidity, condition, icon, date = data.values()

    condition = condition.capitalize()
    embed = discord.Embed(
        title=f"{icon} Clima em {city.title()} {icon}",
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

    lon, lat = get_lon_and_lat(city, state)
    get_hourly_data_graph(lat, lon)
    file = discord.File("temperature_graph.png", filename="graph.png")
    embed.set_image(url="attachment://graph.png")

    embed.set_footer(
        text="Dados retirados da API OpenWeather"
    )

    return embed, file
