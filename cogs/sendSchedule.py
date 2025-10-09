from discord.ext import commands
from discord.commands import slash_command
import discord
import json

class send_scedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="send_schedule", description="send the schedule embed into channel")
    async def set(self, ctx):
        
        print(f"SendSchedule has been executed by: {ctx.author}")
        
        try:
            with open("tasks.json") as file:
                config = json.load(file)
            
                if not config:
                    await ctx.respond("Er zijn nog geen taken om te verstuuren", ephemeral=True)
                    return
            
        except FileNotFoundError:
            print("config was not found")

        embed = discord.Embed(
            title="graduaat programmeren schedule",
        )

        for time, tasks in config.items():
            embed.add_field(name=f"Datum: {time}", value="", inline=False)
            for task in tasks:
                print(time, task)
                embed.add_field(name="", value=f"```{task}```", inline=False)

        await ctx.send(embed=embed)

 
def setup(bot):
    bot.add_cog(send_scedule(bot))