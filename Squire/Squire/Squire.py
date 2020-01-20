#Squire.py
import os
import random
import time
import discord

from discord.ext import commands
from dotenv import load_dotenv

def log(MESSAGE):
	LOCAL_TIME = time.localtime(time.time())
	TIMESTAMP = f'{LOCAL_TIME.tm_year}-{LOCAL_TIME.tm_mon}-{LOCAL_TIME.tm_mday} {LOCAL_TIME.tm_hour}:{LOCAL_TIME.tm_min}:{LOCAL_TIME.tm_sec}'
	print(f'{TIMESTAMP} {MESSAGE}')

log('Loading enviroment variables')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ANNOUNCEMENT_CHANNEL = os.getenv('ANNOUCMENT_CHANNEL')

log('Creating bot instance')
BOT = commands.Bot(command_prefix='!')

@BOT.command(name='r', help='Rolls dice! (Format: [number_of_dice]d[number_of_sides])')
async def roll_dice(CTX, *DICE):
	REQUEST_USR = CTX.author
	log(f'Running the dice roll command for {REQUEST_USR}')
	if not DICE:
		RESPONSE = f'{REQUEST_USR.mention} needs to learn how to give the correct parameters. (No parameter not given)'
	else:
		SEPERATOR_INDEX = DICE[0].lower().find('d')

		if SEPERATOR_INDEX == -1:
			RESPONSE = f'{REQUEST_USR.mention} needs to learn how to give the correct parameters. ("**{DICE[0]}**" is not valid parameter)'
		else:
			SPLIT = DICE[0].lower().split('d')

			TEST = True
			try:
				DICE_NUM = int(SPLIT[0])
				DICE_SIDES = int(SPLIT[1])
			except ValueError:
				RESPONSE = f'{REQUEST_USR.mention} needs to learn how to give the correct parameters. ("**{DICE[0]}**" is not valid parameter)'
				TEST = False

			if TEST:
				DICE_RESULT = [
					int(random.choice(range(1, DICE_SIDES + 1)))
					for _ in range(DICE_NUM)
				]

				if len(DICE_RESULT) > 1:
					DICE_TOTAL = 0
					for NUM in DICE_RESULT:
						DICE_TOTAL = DICE_TOTAL + int(NUM)
					
					RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_TOTAL}** on **{DICE[0]}**. {DICE_RESULT}'
				else:
					RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[0]}** on a **{DICE[0]}**.'
	await CTX.send(RESPONSE)

@BOT.command(name='quote', help='Either adds or reads off a random quote.')
async def quote(CTX, *QUOTE):
	REQUEST_USR = CTX.author
	log(f'Now running the quote command for {REQUEST_USR}')

	if not QUOTE:
		with open(f'{os.getcwd()}/Quotes.txt', 'r') as f:
			LINES = f.read().splitlines()
			SELECTED_INDEX = random.choice(range(0, len(LINES)))
			RESPONSE = LINES[SELECTED_INDEX]
	else:
		QUOTE_TEXT = ' '.join(QUOTE)
		with open(f'{os.getcwd()}/Quotes.txt', 'a') as f:
			f.write(f'\n{QUOTE_TEXT}')
		RESPONSE = f'Added the quote "{QUOTE_TEXT}" to the list!' 

	await CTX.send(RESPONSE)

@BOT.command(name='dum', help='U iz dum.')
async def dum(CTX):
	REQUEST_USR = CTX.author
	log(f'Now running the dum command for {REQUEST_USR}')
	
	with open(f'{os.getcwd()}/DumQuotes.txt', 'r') as f:
		LINES = f.read().splitlines()
		SELECTED_INDEX = random.choice(range(0, len(LINES)))
		DUM_LINE = LINES[SELECTED_INDEX]

	if DUM_LINE.endswith('.gif') or DUM_LINE.endswith('.png') or DUM_LINE.endswith('.jpg'):
		await CTX.send(f'{REQUEST_USR.mention}', file=discord.File(f'Assets\{DUM_LINE}'))
	else:
		await CTX.send(f'{REQUEST_USR.mention} {DUM_LINE}')

@BOT.event
async def on_ready():
	log(f'{BOT.user.name} has connected to Discord!')

log('Sending bot to server')
BOT.run(TOKEN)