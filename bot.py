from discord.ext import commands
import decouple

bot = commands.Bot("!!")

DISC_KEY = decouple.config("DISC_KEY")
API_KEY = decouple.config("API_KEY")


if __name__ == "__main__":
    bot.load_extension("manager")
    bot.load_extension("commands.messages")
    bot.run(DISC_KEY)
