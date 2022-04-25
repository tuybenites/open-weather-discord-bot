from discord.ext import commands
from embeds import embed_weather_current, embed_weather_forecast


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clima")
    async def send_current_weather(self, ctx):
        embed_weather = embed_weather_current(self.bot)
        await ctx.channel.send(embed=embed_weather)

    @commands.command(name="previsao")
    async def send_tomorrow_weather(self, ctx, message):
        if message in ["amanha", "depois_amanha"]:
            embed_weather = embed_weather_forecast(self.bot, message)
            await ctx.channel.send(embed=embed_weather)
        else:
            await ctx.channel.send("Parâmetro inválido. !!help para ajuda")


def setup(bot):
    bot.add_cog(Messages(bot))
