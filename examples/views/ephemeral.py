import versacord
from versacord.ext import commands


# Define a simple View that gives us a counter button
class Counter(versacord.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @versacord.ui.button(label="0", style=versacord.ButtonStyle.red)
    async def count(self, button: versacord.ui.Button, interaction: versacord.Interaction):
        number = int(button.label) if button.label else 0
        if number >= 4:
            button.style = versacord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)


# Define a View that will give us our own personal counter button
class EphemeralCounter(versacord.ui.View):
    # When this button is pressed, it will respond with a Counter view that will
    # give the button presser their own personal button they can press 5 times.
    @versacord.ui.button(label="Click", style=versacord.ButtonStyle.blurple)
    async def receive(self, button: versacord.ui.Button, interaction: versacord.Interaction):
        # ephemeral=True makes the message hidden from everyone except the button presser
        await interaction.response.send_message("Enjoy!", view=Counter(), ephemeral=True)


bot = commands.Bot()


@bot.slash_command()
async def counter(interaction):
    """Starts a counter for pressing."""
    await interaction.send("Press!", view=EphemeralCounter())


bot.run("token")
