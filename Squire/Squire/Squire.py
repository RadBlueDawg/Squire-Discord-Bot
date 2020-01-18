#Squire.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv


print(f'Loading enviroment variables...')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

print(f'\nCreating bot instance...')
BOT = commands.Bot(command_prefix='!')

@BOT.command(name='r', help='Rolls dice! (Format: [number_of_dice]d[number_of_sides])')
async def roll_dice(CTX, *DICE):
	REQUEST_USR = CTX.author.mention
	if not DICE:
		RESPONSE = f'{REQUEST_USR} needs to learn how to give the correct parameters. (No parameter not given)'
	else:
		SEPERATOR_INDEX = DICE[0].lower().find('d')

		if SEPERATOR_INDEX == -1:
			RESPONSE = f'{REQUEST_USR} needs to learn how to give the correct parameters. ("**{DICE[0]}**" is not valid parameter)'
		else:
			SPLIT = DICE[0].lower().split('d')

			TEST = True
			try:
				DICE_NUM = int(SPLIT[0])
				DICE_SIDES = int(SPLIT[1])
			except ValueError:
				RESPONSE = f'{REQUEST_USR} needs to learn how to give the correct parameters. ("**{DICE[0]}**" is not valid parameter)'
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
					
					RESPONSE = f'{REQUEST_USR} rolled **{DICE_TOTAL}** on **{DICE[0]}**. {DICE_RESULT}'
				else:
					RESPONSE = f'{REQUEST_USR} rolled **{DICE_RESULT[0]}** on a **{DICE[0]}**.'

	await CTX.send(RESPONSE)

@BOT.command(name='dum', help='U iz dum.')
async def dum(CTX):
	REQUEST_USR = CTX.author.mention
	await CTX.send(f'{REQUEST_USR} is the big dum.')

@BOT.event
async def on_ready():
	print(f'\n{BOT.user.name} has connected to Discord!')

print(f'\nSending bot to server...')
BOT.run(TOKEN)