from discord.ext import commands
from embeds import embed_weather_current, embed_weather_forecast


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clima", help="Não receber parâmetros")
    async def send_current_weather(self, ctx,
                                   state="RS", country="BR",
                                   *city):
        state = state.replace(',', '')
        city = ' '.join(city)
        embed_weather = embed_weather_current(self.bot,
                                              city, state, country)
        await ctx.channel.send(embed=embed_weather)

    @commands.command(name="previsao", help="""
    Parâmetros: amanha, depois_amanha""")
    async def send_tomorrow_weather(self, ctx, message):
        if message in ["amanha", "depois_amanha"]:
            embed_weather = embed_weather_forecast(self.bot, message)
            await ctx.channel.send(embed=embed_weather)
        else:
            await ctx.channel.send("Parâmetro inválido. !!help para ajuda")

    @commands.command(name="RS", help="XXX")
    async def send_rs_weather(self, ctx, *city):
        try:
            city = ' '.join(city)
            embed = embed_weather_current(self.bot, city, "RS", "BR")
            await ctx.channel.send(embed=embed)
        except Exception:
            await ctx.channel.send(("""Ocorre um erro.
Digite !!help para obter ajuda"""))


def setup(bot):
    bot.add_cog(Messages(bot))
