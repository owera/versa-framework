import versa
from versa.ext import commands

intents = versa.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")


bot.run("token")
