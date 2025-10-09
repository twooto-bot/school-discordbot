from discord.ext import commands
from discord.commands import slash_command
from datetime import datetime
import json

class new_task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="new_task", description="Voeg een nieuwe taak toe aan de lijst")
    async def set(self, ctx, task, time):
        try:
            with open("tasks.json", "r") as file:
                config = json.load(file)
                print(config)

            with open("tasks.json", "w") as file:
                if time in config:
                    config[time].append(task)
                else:
                    config[time] = [task]

                sorted_tasks = dict(sorted(
                    config.items(),
                    key=lambda item: datetime.strptime(item[0], "%d-%m-%Y")
                ))

                json.dump(sorted_tasks, file, indent=4)
            
        except FileNotFoundError:
            print("config was not found")

        await ctx.respond(f"{task} has been added with the date {time}", ephemeral=True)
        
def setup(bot):
    bot.add_cog(new_task(bot))