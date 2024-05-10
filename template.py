####################################################################
#                                                                  #
#    Credit: therealOri  |  https://github.com/therealOri          #
#                                                                  #
####################################################################

####################################################################################
#                                                                                  #
#                            Imports & definitions                                 #
#                                                                                  #
####################################################################################
import asyncio
import discord
import os
from discord import app_commands
import datetime
from libs import rnd
import tomllib
import logging



#Load our config for main
with open('config.toml', 'rb') as fileObj:
    config = tomllib.load(fileObj) #dictionary/json




__authors__ = '@therealOri'
token = config["TOKEN"]
guild_id = config["guild_id"]
MY_GUILD = discord.Object(id=guild_id)
bot_logo = config["bot_logo"]
author_logo = None



hex_red=0xFF0000
hex_green=0x0AC700
hex_yellow=0xFFF000 # I also like -> 0xf4c50b

# +++++++++++ Imports and definitions +++++++++++ #














####################################################################################
#                                                                                  #
#                             Normal Functions                                     #
#                                                                                  #
####################################################################################
def clear():
    os.system("clear||cls")



def random_hex_color():
    hex_digits = '0123456789abcdef'
    hex_digits = rnd.shuffle(hex_digits)
    color_code = ''
    nums = rnd.randint(0, len(hex_digits)-1, 6)
    for _ in nums:
        color_code += hex_digits[_]
    value =  int(f'0x{color_code}', 16)
    return value

# +++++++++++ Normal Functions +++++++++++ #













####################################################################################
#                                                                                  #
#                   Async Functions, buttons, modals, etc.                         #
#                                                                                  #
####################################################################################
async def status():
    while True:
        status_messages = ['my internals', '/help for help', 'your navigation history', 'myself walking on the grass', 'Global Global Global', 'base all your 64', 'your security camera footage', 'myself walking on the moon', 'your browser search history']
        smsg = rnd.choice(status_messages)
        activity = discord.Streaming(type=1, url='https://www.youtube.com/watch?v=4xDzrJKXOOY', name=smsg)
        await tmp.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(60) #Seconds

# +++++++++++ Async Functions, buttons, modals, etc. +++++++++++ #












####################################################################################
#                                                                                  #
#                                Client Setup                                      #
#                                                                                  #
####################################################################################
class TMP(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        #self.tree.copy_global_to(guild=MY_GUILD)  # This copies your commands over to your guild for immediate access for testing while you wait for discord to register all of the commands.
        await self.tree.sync(guild=None)



intents = discord.Intents.default()
tmp = TMP(intents=intents)
# +++++++++++ Client Setup +++++++++++ #










####################################################################################
#                                                                                  #
#                                   Events                                         #
#                                                                                  #
####################################################################################
@tmp.event
async def on_ready():
    global author_logo
    me = await tmp.fetch_user(254148960510279683)
    author_logo = me.avatar
    tmp.loop.create_task(status())

    clear()
    print(f'Logged in as {tmp.user} (ID: {tmp.user.id})')
    print('------')

# +++++++++++ Events +++++++++++ #













####################################################################################
#                                                                                  #
#                             Regular Commands                                     #
#                                                                                  #
####################################################################################
@tmp.tree.command(description='Shows you what commands you can use.')
async def help(interaction: discord.Interaction):
    rnd_hex = random_hex_color()
    embed = discord.Embed(title='Commands  |  Help\n-=-=-=-=-=-=-=-=-=-=-=-=-=-', colour=rnd_hex, timestamp=datetime.datetime.now(datetime.timezone.utc))
    embed.set_thumbnail(url=bot_logo)
    embed.add_field(name='\u200B\n/help', value="Shows you this help message.", inline=True)
    embed.add_field(name='\u200B\n/ping ', value="Checks the bots connection & if it is responsive.", inline=True)
    embed.add_field(name="\u200B\n", value="\u200B\n-=-=-=-=-=-=-=-=-=-=-=-=-=-", inline=False)
    embed.set_footer(text=__authors__, icon_url=author_logo)
    await interaction.response.send_message(embed=embed, ephemeral=True)




@tmp.tree.command(description='Test to see if the bot is responsive.')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"⏱️ Pong! ⏱️\nConnection speed is {round(tmp.latency * 1000)}ms", ephemeral=True)

# +++++++++++ Regular Commands +++++++++++ #


















if __name__ == '__main__':
    clear()
    tmp.run(token, reconnect=True, log_level=logging.INFO) #log_handler is also an option for if you have your own way of handling logging, etc.
