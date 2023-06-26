#Squire.py
import DatabaseManager
import discord
import os
import random

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from Helpers import *

VERSION = "2.0-alpha"
console_log(f"You're running Squire Discord Bot version {VERSION}")

console_log("Loading environment variables")
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
ASSET_DIR = os.getenv("ASSET_DIRECTORY")
FEEDBACK_LINK = os.getenv("FEEDBACK_LINK")
DICE_NUM_MAX = 100 #One hundred dice per roll should be plenty for any actual use case
DICE_SIZE_MAX = 1000000000 #If you need a dice with more than 1 billion sides, go write your own bot
console_log('Loading database')
DATA = DatabaseManager.Squire_Data()

console_log("Creating bot instance")
SQUIRE = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@SQUIRE.event
async def on_ready():
    await SQUIRE.change_presence(activity=discord.Game(name=f"v{VERSION}"))
    console_log(f"{SQUIRE.user.name} has connected to Discord!")
    try:
        synced = await SQUIRE.tree.sync()
        console_log(f"Synced {len(synced)} command(s)")
    except Exception as e:
        console_log(e)

@SQUIRE.tree.command(name="dum", description="U iz dum")
async def self(interaction: discord.Interaction):
    dumLine = get_random_line_from_file(f"{ASSET_DIR}/DumQuotes.txt")

    if dumLine.endswith(".gif") or dumLine.endswith(".png") or dumLine.endswith(".jpg"):
        await interaction.response.send_message(f"{interaction.user.mention}", file=discord.File(f"{ASSET_DIR}/{dumLine}"))
    else:
        await interaction.response.send_message(f"{interaction.user.mention} {dumLine}")

@SQUIRE.tree.command(name="feedback", description="Have feedback on Squire? Find out how to let me know!")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"Got feedback for Squire? You can sumbit it at the following link: {FEEDBACK_LINK}", ephemeral=True)

@SQUIRE.tree.command(name="quote", description="Either adds or reads off a random quote")
@app_commands.describe(new_quote = "A new quote to add to the server.")
async def self(interaction: discord.Interaction, new_quote: str = None):
    if interaction.guild is None:
        await interaction.response.send_message("You can't use the quote command in a direct message chat!")
    elif new_quote is not None:
        DATA.addQuote(interaction.guild.id, interaction.user.id, new_quote)
        await interaction.response.send_message(f'Added the quote "{newQuoteFixedFormatting}" to the list!')
    else:
        availableQuotes = DATA.getQuotes(interaction.guild.id)
        if len(availableQuotes) == 0:
            await interaction.response.send_message("No quotes have been added on this server yet!")
        else:
            selectedQuoteIndex = random.choice(range(0, len(availableQuotes)))
            await interaction.response.send_message(availableQuotes[selectedQuoteIndex][0])

@SQUIRE.tree.command(name="roll", description="Roll the dice!")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("WIP", ephemeral=True)

@SQUIRE.tree.command(name="roll-stats", description="Rolls 4d6 and adds the highest 3 together. By default a standard array of 6 are rolled.")
async def self(interaction: discord.Interaction):
        await interaction.response.send_message("WIP", ephemeral=True)    

@SQUIRE.tree.command(name="yikes", description="For when something yikes-able has occured.")
async def self(interaction: discord.Interaction):
    yikesFile = get_random_line_from_file(f"{ASSET_DIR}/YikesQuotes.txt")
    await interaction.response.send_message(f"{interaction.user.mention}", file=discord.File(f"{ASSET_DIR}/{yikesFile}"))

SQUIRE.run(TOKEN)