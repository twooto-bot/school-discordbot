import discord
from discord.ext import commands
from discord.commands import slash_command
from datetime import datetime, date
import json

class send_schedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="send_schedule", description="Send the schedule embed into channel")
    async def send_schedule(self, ctx):
        today = date.today()
        
        print(f"SendSchedule has been executed by: {ctx.author}")
        await ctx.respond("Sending schedule ...", ephemeral=True)

        # Load tasks safely
        try:
            with open("tasks.json", "r") as file:
                config = json.load(file)
                
                if not config:
                    await ctx.respond("Er zijn nog geen taken om te versturen", ephemeral=True)
                    return
            
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ tasks.json was not found or is invalid")
            await ctx.respond("Geen taken gevonden.", ephemeral=True)
            return

        # Remove outdated tasks safely
        keys_to_remove = []
        for group, dates in config.items():  
            for time_str in dates:
                try:
                    task_date = datetime.strptime(time_str, "%d-%m-%Y").date()
                    if task_date < today:
                        keys_to_remove.append(time_str)
                except ValueError:
                    print(f"⚠️ Invalid date in tasks.json: {time_str}, skipping...")

        for key in keys_to_remove:
            tasks = config[key]
            del config[key]
            print(f"Removed {key}: {tasks}")

        # Save updated tasks
        with open("tasks.json", "w") as file:
            json.dump(config, file, indent=4)



        for group, dates in config.items():

            if group == "GroepA":
                color = 0xED4245  # Red
            else:
                color = 0x5865F2  # Blue

            # Build the embed
            embed = discord.Embed(title=f"Graduaat Programmeren Schedule for {group}", color=color)

            for time_str, tasks in dates.items():

                embed.add_field(name=f"Datum: {time_str}", value="", inline=False)
                for task in tasks:
                    embed.add_field(name="", value=f"```{task}```", inline=False)
                
            embed.set_footer(text=f"Vives students bot hosted by twooto, command executed by {ctx.author}")
            
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(send_schedule(bot))
