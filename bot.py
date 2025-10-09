import discord
import os
import json

try:
    path = os.getcwd()
    config_path = os.path.join(path, "config.json")

    with open(config_path) as main_config:
        config = json.load(main_config)
        TOKEN = config.get("TOKEN")
   
    if TOKEN == None:
        raise ValueError("there is no token set in config.js")

except FileNotFoundError:
    print("config was not found")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Loged in as {bot.user}")
    

for filename in os.listdir("cogs"):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Successfully loaded {filename}")
        except Exception as e:
            print(f"Failed to load {filename}: {e}")

bot.run(TOKEN)
