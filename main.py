import importlib
import importlib.util
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
from pymongo import MongoClient
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False

# Create a Bot instance with sharding enabled
client = commands.AutoShardedBot(shard_count=2, command_prefix="!", intents=nextcord.Intents.all())

cogs_dir = "commands/cogs"

loaded_cogs = []
loaded_folders = []

for root, dirs, files in os.walk(cogs_dir):
    if root in loaded_folders:
        continue
    for filename in files:
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{root.replace('/', '.').replace(os.sep, '.')}.{filename[:-3]}"
            client.load_extension(module_name)
    if "__init__.py" in files:
        loaded_folders.append(root)


# Event: Bot is ready
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    shard_id = client.shard_id if client.shard_id is not None else 0
    shard_count = client.shard_count if client.shard_count is not None else 1
    print(f"Shard ID: {shard_id}")
    print(f"Shard Count: {shard_count}")

    # Set bot's presence with shard information
    activity = nextcord.Activity(type=nextcord.ActivityType.playing, name=f"Shard {shard_id + 1}/{shard_count}")
    await client.change_presence(activity=activity)


# Run the bot
client.run(TOKEN)







