import versa


class MyInteraction(versa.Interaction):
    async def send_embed(self, *, title: str, description: str):
        """Easily send a basic embed."""
        embed: versa.Embed = versa.Embed(
            title=title,
            description=description,
        )
        embed.set_author(name=self.user.display_name, icon_url=self.user.display_avatar)
        await self.send(embed=embed)


class Client(versa.Client):
    def get_interaction(self, data, *, cls=versa.Interaction):
        # when you override this method, you pass your new Interaction
        # subclass to the super() method, which tells the bot to
        # use the new MyInteraction class
        return super().get_interaction(data, cls=MyInteraction)


client = Client()
TESTING_GUILD_ID = 123456789  # Replace with your testing guild id


@client.slash_command(guild_ids=[TESTING_GUILD_ID])
async def create_embed(interaction: MyInteraction, title: str, description: str):
    await interaction.send_embed(title=title, description=description)


client.run("token")
