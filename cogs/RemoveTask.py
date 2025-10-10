from discord import option
from discord.ext import commands
from discord.commands import slash_command
from datetime import datetime
import json

class remove_task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="remove_task", description="Verwijder een taak in de lijst")
    @option("task", description="Wat is de taak die je wilt verwijderen?")
    @option("time", description="Datum in dit formaat: dd-mm-jjjj (bijv. 05-10-2025)")
    @option("group",
        description="in welke groep is deze taak",
        choices=["GroepA", "GroepB"])
    async def remove_task(self, ctx, task, time, group):
        
        print(f"RemoveTask has been executed by: {ctx.author}")
        
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

        try:
            if len(config[group][valid_date]) == 1:
                del config[group][valid_date]
            else:
                config[group][valid_date].remove(task)
        except KeyError as e:
            print(f"Key not found in Json error: {e}")
            await ctx.respond("Please enter a valid task! if its still not working contact <@1192033363725402136>")
            return

        # Sla de data opnieuw op
        with open("tasks.json", "w") as file:
            json.dump(config, file, indent=4)

        await ctx.respond(f"{task} has been removed", ephemeral=True)
        
def setup(bot):
    bot.add_cog(remove_task(bot))