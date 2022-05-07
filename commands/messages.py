from discord.ext import commands
from embeds import embed_weather_current


class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="BR", help="XXXX")
    async def send_br_weather(self, ctx, estate, *city):
        pass

    @commands.command(name="RS", help="XXXX")
    async def send_rs_weather(self, ctx, *city):
        try:
            city = ' '.join(city).title()
            embed, file = embed_weather_current(self.bot, city, "RS", "BR")
            await ctx.channel.send(file=file, embed=embed)
        except Exception as error:
            print(error)
            await ctx.channel.send(("""Ocorre um erro.
Digite !!help para obter ajuda"""))


def setup(bot):
    bot.add_cog(Messages(bot))
