import versacord
from versacord.ext import commands


# Define a simple View that gives us a confirmation menu
class Confirm(versacord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @versacord.ui.button(label="Confirm", style=versacord.ButtonStyle.green)
    async def confirm(self, button: versacord.ui.Button, interaction: versacord.Interaction):
        await interaction.response.send_message("Confirming", ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @versacord.ui.button(label="Cancel", style=versacord.ButtonStyle.grey)
    async def cancel(self, button: versacord.ui.Button, interaction: versacord.Interaction):
        await interaction.response.send_message("Cancelling", ephemeral=True)
        self.value = False
        self.stop()


bot = commands.Bot()


@bot.slash_command()
async def ask(interaction):
    """Asks the user a question to confirm something."""
    # We create the view and assign it to a variable so we can wait for it later.
    view = Confirm()
    await interaction.send("Do you want to continue?", view=view)
    # Wait for the View to stop listening for input...
    await view.wait()
    if view.value is None:
        print("Timed out...")
    elif view.value:
        print("Confirmed...")
    else:
        print("Cancelled...")


bot.run("token")
