from discord.ext import commands
from discord.commands import slash_command
import discord
from discord import option
from datetime import datetime
import json

class new_task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="new_task", description="Voeg een nieuwe taak toe aan de lijst")
    @option("task", description="Wat is de taak die je wilt toevoegen?")
    @option("time", description="Datum in dit formaat: dd-mm-jjjj (bijv. 05-10-2025)")
    @option("group",
        description="Voor welke groep is deze taak?",
        choices=["GroepA", "GroepB"])
    async def set(self, ctx, task, time, group):
        
        print(f"AddNewTask has been executed by: {ctx.author}")
        
        try:
            parsed_date  = datetime.strptime(time, "%d-%m-%Y")
            valid_date = parsed_date.strftime("%d-%m-%Y")
        except ValueError:
            await ctx.respond("❌ Invalid date! Please use the format **dd-mm-yyyy** (e.g., 05-10-2025).",ephemeral=True)
            return
        
        try:
            with open("tasks.json", "r") as file:
                config = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            config = {}  

        # Zorg dat de groep en datum bestaan
        if group not in config:
            config[group] = {}

        if valid_date not in config[group]:
            config[group][valid_date] = []

        # Voeg de taak toe
        config[group][valid_date].append(task)

        # Sorteer de data per groep op datum
        for groep in config:
            config[groep] = dict(sorted(
                config[groep].items(),
                key=lambda item: datetime.strptime(item[0], "%d-%m-%Y")
            ))

        # Sla de data opnieuw op
        with open("tasks.json", "w") as file:
            json.dump(config, file, indent=4)

        await ctx.respond(f"{task} has been added with the date {time}", ephemeral=True)
        
def setup(bot):
    bot.add_cog(new_task(bot))