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

log('Creating bot instance')
BOT = commands.Bot(('!', 'squire, '))

@BOT.command(name='roll', help='Rolls dice! (See help message for formatting details)\n(Format: [number_of_dice]d[number_of_sides] OR [disadvantage|dis|d] OR [advantage|adv|a])', aliases=['r', 'R'])
async def roll_dice(CTX, *DICE):
	REQUEST_USR = CTX.author
	log(f'Running the dice roll command for {REQUEST_USR}')
	if not DICE:
		RESPONSE = f'{REQUEST_USR.mention} needs to learn how to give the correct parameters. (No parameter not given)'
	elif DICE[0].lower() == 'dis' or DICE[0].lower() == 'd' or DICE[0].lower() == 'disadvantage':
		DICE_RESULT = [
			int(random.choice(range(1, 21)))
			for _ in range(2)
		]

		if DICE_RESULT[0] < DICE_RESULT[1]:
			RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[0]}** at **disadvantage**. [{DICE_RESULT[0]}, ~~{DICE_RESULT[1]}~~]'
		else:
			RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[1]}** at **disadvantage**. [~~{DICE_RESULT[0]}~~, {DICE_RESULT[1]}]'
	elif DICE[0].lower() == 'adv' or DICE[0].lower() == 'a' or DICE[0].lower() == 'advantage':
		DICE_RESULT = [
			int(random.choice(range(1, 21)))
			for _ in range(2)
		]

		if DICE_RESULT[0] > DICE_RESULT[1]:
			RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[0]}** at **advantage**. [{DICE_RESULT[0]}, ~~{DICE_RESULT[1]}~~]'
		else:
			RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[1]}** at **advantage**. [~~{DICE_RESULT[0]}~~, {DICE_RESULT[1]}]'
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

@BOT.command(name='quote', help='Either adds or reads off a random quote.', aliases=['q', 'Q'])
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

@BOT.command(name='dum', help='U iz dum.', aliases=['d', 'D'])
async def dum(CTX):
	REQUEST_USR = CTX.author
	log(f'Now running the dum command for {REQUEST_USR}')
	
	with open(f'{os.getcwd()}/DumQuotes.txt', 'r') as f:
		LINES = f.read().splitlines()
		SELECTED_INDEX = random.choice(range(0, len(LINES)))
		DUM_LINE = LINES[SELECTED_INDEX]

	if DUM_LINE.endswith('.gif') or DUM_LINE.endswith('.png') or DUM_LINE.endswith('.jpg'):
		await CTX.send(f'{REQUEST_USR.mention}', file=discord.File(f'{os.getcwd()}/Assets/{DUM_LINE}'))
	else:
		await CTX.send(f'{REQUEST_USR.mention} {DUM_LINE}')

@BOT.command(name='yikes', help='Declare a yikes.', aliases=['y', 'Y'])
async def yikes(CTX):
	REQUEST_USR = CTX.author
	log(f'Now running the yikes command for {REQUEST_USR}')

	with open(f'{os.getcwd()}/YikesQuotes.txt', 'r') as f:
		LINES = f.read().splitlines()
		SELECTED_INDEX = random.choice(range(0, len(LINES)))
		YIKES_LINE = LINES[SELECTED_INDEX]

		await CTX.send(f'{REQUEST_USR.mention}', file=discord.File(f'{os.getcwd()}/Assets/{YIKES_LINE}'))

@BOT.command(name='rollstats', help='Rolls 4d6 and adds the three highest. (See help message for details).\nIt will either roll the number of stat numbers specified, or that standard 6.', aliases=['rs', 'RS'])
async def roll_stats(CTX, *NUMBER):
	if not NUMBER:
		NUM_DICE = 6
	else:
		NUM_DICE = int(NUMBER[0])

	RESPONSE = ''
	COUNT = 0
	while(COUNT < NUM_DICE):
		DICE_RESULT = [
				int(random.choice(range(1, 7)))
				for _ in range(4)
			]
		DICE_RESULT.sort(reverse=True);
		DICE_TOTAL = int(DICE_RESULT[0]) + int(DICE_RESULT[1]) + int(DICE_RESULT[2])
		RESPONSE += f'{DICE_TOTAL} ['
		ROLL_COUNT = 1;
		for ROLL in DICE_RESULT:
			if ROLL_COUNT == 4:
				ROLL = f'~~{ROLL}~~]\n'
			else:
				ROLL = f'{ROLL}, '
			RESPONSE += ROLL
			ROLL_COUNT += 1

		COUNT += 1

	await CTX.send(RESPONSE)

@BOT.event
async def on_ready():
	log(f'{BOT.user.name} has connected to Discord!')

log('Sending bot to server')
BOT.run(TOKEN)