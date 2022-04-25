import discord
from weather_api import get_current_data, get_forecast_data


def embed_weather_current(bot):

    temperature, humidity, condition, icon, date = get_current_data(
        -29.820, -51.158).values()

    condition = condition.capitalize()
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
                    value=f" {humidity}%")

    embed.add_field(name="Temperatura 🌡️",
                    value=f" {temperature}° C")

    embed.add_field(name="Condição 📝",
                    value=str(condition))

    embed.add_field(name="Data 📅", value=str(date))

    embed.set_image(url="https://i.imgur.com/sZx6LgU.png")

    embed.set_footer(
        text="Dados retirados da API Climatempo"
    )

    return embed


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
                    value=f" {humidity}%")

    embed.add_field(name="Temperatura Mínima 🌡️",
                    value=f" {temp_min}° C")

    embed.add_field(name="Temperatura Mínima 🌡️",
                    value=f" {temp_max}° C")

    embed.add_field(name="Condição 📝",
                    value=str(cond))

    embed.add_field(name="Data 📅", value=str(date))

    embed.set_image(url="https://i.imgur.com/sZx6LgU.png")

    embed.set_footer(
        text="Dados retirados da API Climatempo"
    )

    return embed
