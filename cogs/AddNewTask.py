from discord.ext import commands
from discord.commands import slash_command
from datetime import datetime
import json

class new_task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="new_task", description="Voeg een nieuwe taak toe aan de lijst")
    async def set(self, ctx, task, time):
        
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

            with open("tasks.json", "w") as file:
                if valid_date in config:
                    config[valid_date].append(task)
                else:
                    config[valid_date] = [task]

                sorted_tasks = dict(sorted(
                    config.items(),
                    key=lambda item: datetime.strptime(item[0], "%d-%m-%Y")
                ))

                json.dump(sorted_tasks, file, indent=4)
            
        except (FileNotFoundError, ValueError) as e:
            print(f"something went wrong in addnewtask with error: {e}")
            await ctx.respond(f"Something went wrong, try again or contact <@1192033363725402136>", ephemeral=True)
            return

        await ctx.respond(f"{task} has been added with the date {time}", ephemeral=True)
        
def setup(bot):
    bot.add_cog(new_task(bot))