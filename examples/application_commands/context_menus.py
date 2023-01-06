import versacord
from versacord.ext import commands

TESTING_GUILD_ID = 123456789  # Replace with your testing guild id

bot = commands.Bot()


@bot.user_command(guild_ids=[TESTING_GUILD_ID])
async def member_info(interaction: versacord.Interaction, member: versacord.Member):
    await interaction.response.send_message(f"Member: {member}")


@bot.message_command(guild_ids=[TESTING_GUILD_ID])
async def my_message_command(interaction: versacord.Interaction, message: versacord.Message):
    await interaction.response.send_message(f"Message: {message}")


bot.run("token")
