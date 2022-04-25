from discord.ext import commands
from weather_api import get_current_data
from weather_api import get_forecast_data


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clima")
    async def send_current_weather(self, ctx):
        data = get_current_data(-29.820, -51.158)
        await ctx.channel.send(data)

    @commands.command(name="previsao")
    async def send_tomorrow_weather(self, ctx, message):
        if message == "amanha":
            data = get_forecast_data(-29.820, -51.158)["tomorrow_data"]
            await ctx.channel.send(data)
        elif message == "depois_amanha":
            data = get_forecast_data(-29.820, -51.158)["after_tomorrow_data"]
            await ctx.channel.send(data)
        else:
            await ctx.channel.send(("""Algo deu errado.
            Escolha um parâmetro adequado""").replace(" ", ''))

    @commands.command(name="depois_amanha")
    async def send_after_tomorrow_weather(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Messages(bot))
