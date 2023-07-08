import nextcord
from nextcord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @nextcord.slash_command(name="help", description="Show the list of available commands")
    async def show_help(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="Command List", description="List of available commands:", color=nextcord.Color.blue())
        
        if self.bot.user.avatar:
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)

        # Add your commands with descriptions
        commands_list = [
            {"name": "setupglobalchannel", "description": "Set up a global channel for event announcements"},
            {"name": "shareevent", "description": "Share event details to the global channel"}
        ]

        for command in commands_list:
            embed.add_field(name=command["name"], value=command["description"], inline=False)

        embed.set_footer(text="Use !help <command> for more details on a command.")

        await interaction.send(embed=embed)

def setup(client):
    client.add_cog(HelpCog(client))
