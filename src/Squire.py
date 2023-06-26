#Squire.py
import DatabaseManager
import discord
import os
import random

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from Helpers import *

VERSION = "2.0"
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
@app_commands.describe(number_of_dice = "How many dice should be rolled?")
@app_commands.describe(number_of_sides = "How many sides should the dice have? (20 for a d20, 6 for a d6, etc.)")
@app_commands.describe(modifier = "What modifier should be applied to the final result?")
async def self(interaction: discord.Interaction, number_of_dice:int = 1, number_of_sides:int = 20, modifier:int = 0):
    if not number_valid(number_of_sides, DICE_SIZE_MAX):
        await interaction.response.send_message(f"You can't roll a dice with more than {DICE_SIZE_MAX} sides or less than 1 side. (Tried to roll a dice with {number_of_sides} sides)", ephemeral=True)
    elif not number_valid(number_of_dice, DICE_NUM_MAX):
        await interaction.response.send_message(f"You can't roll more than {DICE_NUM_MAX} dice or less than 1 dice at a time. (Tried to roll {number_to_roll} dice)", ephemeral=True)
    else:
        diceResult = dice_roll(number_of_dice, number_of_sides)
        diceTotal = sum(diceResult) + modifier
        diceMathStr = format_dice_math_str(diceResult, modifier)
        await interaction.response.send_message(f"{interaction.user.mention} rolled **{diceTotal}** on **{number_of_dice}d{number_of_sides}**. [{diceMathStr}]")

@SQUIRE.tree.command(name="roll-advantage", description="Rolls 2d20 and returns the higher value.")
@app_commands.describe(modifier = "What modifier should be applied to the final result?")
async def self(interaction: discord.Interaction, modifier:int = 0):
    diceResult = dice_roll(2, 20)
    diceResult.sort(reverse=True)
    diceTotal = diceResult[0] + modifier
    diceMathStr = format_adv_dis_math_str(diceResult, modifier)
    await interaction.response.send_message(f"{interaction.user.mention} rolled **{diceTotal}** at **advantage**. {diceMathStr}")

@SQUIRE.tree.command(name="roll-disadvantage", description="Rolls 2d20 and returns the lower value.")
@app_commands.describe(modifier = "What modifier should be applied to the final result?")
async def self(interaction: discord.Interaction, modifier:int = 0):
    diceResult = dice_roll(2, 20)
    diceResult.sort(reverse=False)
    diceTotal = diceResult[0] + modifier
    diceMathStr = format_adv_dis_math_str(diceResult, modifier)
    await interaction.response.send_message(f"{interaction.user.mention} rolled **{diceTotal}** at **disadvantage**. {diceMathStr}")

@SQUIRE.tree.command(name="roll-stats", description="Rolls 4d6 and adds the highest 3 together. By default a standard array of 6 are rolled.")
@app_commands.describe(number_to_roll = "How many stats do you want to generate?")
async def self(interaction: discord.Interaction, number_to_roll:int = 6):
        if number_valid(number_to_roll, DICE_NUM_MAX):
            formattedResponse = ''
            statNumberCount = 0
            while(statNumberCount < number_to_roll):
                diceResult = dice_roll(4, 6)
                diceResult.sort(reverse=True)
                statNumber = int(diceResult[0]) + int(diceResult[1]) + int(diceResult[2])
                formattedResponse += f"{statNumber} [{diceResult[0]} {diceResult[1]} {diceResult[2]} ~~{diceResult[3]}~~]\n"
                statNumberCount += 1
            
            await interaction.response.send_message(formattedResponse)
        else:
            await interaction.response.send_message(f"You can't roll more than {DICE_NUM_MAX} dice or less than 1 dice at a time. (Tried to roll {number_to_roll} dice)", ephemeral=True)


@SQUIRE.tree.command(name="yikes", description="For when something yikes-able has occured.")
async def self(interaction: discord.Interaction):
    yikesFile = get_random_line_from_file(f"{ASSET_DIR}/YikesQuotes.txt")
    await interaction.response.send_message(f"{interaction.user.mention}", file=discord.File(f"{ASSET_DIR}/{yikesFile}"))

SQUIRE.run(TOKEN)
