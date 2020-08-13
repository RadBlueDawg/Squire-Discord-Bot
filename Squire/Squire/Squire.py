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

VERSION = '1.3'
log(f"You're running Squire Discord Bot Version {VERSION}")

log('Loading enviroment variables')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ASSET_DIR = os.getenv('ASSET_DIRECTORY')
FEEDBACK_LINK = os.getenv('FEEDBACK_LINK')

log('Creating bot instance')
BOT = commands.Bot(('!', 'squire, '))

#This function randomly generates a number of values between 1 and a given number
def dice_roll(NUMBER, SIDES):
	DICE_RESULT = [
		int(random.choice(range(1, SIDES + 1)))
		for _ in range(NUMBER)
	]

	return DICE_RESULT

#This function spilts a standard dice string into an ordered array.
def split_dice_string(DICE_STR):
	DICE_SEPERATOR = DICE_STR.find('d')
	PLUS_MOD_SEPERATOR = DICE_STR.find('+')
	MINUS_MOD_SEPERATOR = DICE_STR.find('-')

	if DICE_SEPERATOR == -1:
		return None
	
	DICE_SPLIT = DICE_STR.lower().split('d')

	if PLUS_MOD_SEPERATOR != -1:
		MOD_SPLIT = DICE_SPLIT[1].split('+')
	elif MINUS_MOD_SEPERATOR != -1:
		MOD_SPLIT = DICE_SPLIT[1].split('-')
		MOD_SPLIT[1] = f'-{MOD_SPLIT[1]}'
	else:
		MOD_SPLIT = [DICE_SPLIT[1], '0']

	if DICE_SPLIT[0] == '':
		DICE_SPLIT[0] = '1'

	try:
		DICE_NUM = int(DICE_SPLIT[0])
		DICE_SIDES = int(MOD_SPLIT[0])
		DICE_MOD = int(MOD_SPLIT[1])
	except ValueError:
		return None

	return [DICE_NUM, DICE_SIDES, DICE_MOD]

#This function takes an array of integers and a modifier and formats them into a nice string
def create_dice_math_str(ROLL_ARRAY, MODIFIER):
	MATH_STR = f'({ROLL_ARRAY[0]}'

	COUNT = 1
	while (COUNT < len(ROLL_ARRAY)):
		MATH_STR = f'{MATH_STR} + {ROLL_ARRAY[COUNT]}'
		COUNT += 1

	if MODIFIER == 0:
		MATH_STR = f'{MATH_STR})'
	elif MODIFIER > 0:
		MATH_STR = f'{MATH_STR}) + {MODIFIER}'
	else:
		MATH_STR = f'{MATH_STR}) - {abs(MODIFIER)}'
	return MATH_STR

@BOT.command(name='roll', help='Rolls dice!\n\n(Format: [number_of_dice]d[number_of_sides] OR [disadvantage|dis|d] OR [advantage|adv|a])', aliases=['r', 'R'])
async def roll_dice(CTX, *DICE):
	REQUEST_USR = CTX.author
	log(f'Running the dice roll command for {REQUEST_USR}')
	if not DICE:
		RESPONSE = f'{REQUEST_USR.mention} needs to learn how to give the correct parameters. (No parameter given)'
	elif DICE[0].lower() == 'dis' or DICE[0].lower() == 'd' or DICE[0].lower() == 'disadvantage':
		DICE_RESULT = dice_roll(2, 20)
		DICE_RESULT.sort(reverse=True)
		RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[0]}** at **disadvantage**. [~~{DICE_RESULT[0]}~~, {DICE_RESULT[1]}]'
	elif DICE[0].lower() == 'adv' or DICE[0].lower() == 'a' or DICE[0].lower() == 'advantage':
		DICE_RESULT = dice_roll(2, 20)
		DICE_RESULT.sort(reverse=True)
		RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_RESULT[0]}** at **advantage**. [{DICE_RESULT[0]}, ~~{DICE_RESULT[1]}~~]'
	else:
		DICE_VALUES = split_dice_string(DICE[0])
		if not DICE_VALUES:
			RESPONSE = f'{REQUEST_USR.mention} needs to learn how to give the correct parameters. ("**{DICE[0]}**" is not valid parameter)'
		else:
			DICE_RESULT = dice_roll(DICE_VALUES[0], DICE_VALUES[1])
			DICE_TOTAL = sum(DICE_RESULT) + DICE_VALUES[2]
			MATH_STR = create_dice_math_str(DICE_RESULT, DICE_VALUES[2])
			RESPONSE = f'{REQUEST_USR.mention} rolled **{DICE_TOTAL}** on **{DICE[0]}**. [{MATH_STR}]'
	await CTX.send(RESPONSE)

@BOT.command(name='quote', help='Either adds or reads off a random quote.\n\nYou can call the command alone to have Squire read off a quote, or follow the command with a phrase to add it to the list of quotes.', aliases=['q', 'Q'])
async def quote(CTX, *QUOTE):
	REQUEST_USR = CTX.author
	log(f'Running the quote command for {REQUEST_USR}')

	if not QUOTE:
		with open(f'{ASSET_DIR}/Quotes.txt', 'r') as f:
			LINES = f.read().splitlines()
			SELECTED_INDEX = random.choice(range(0, len(LINES)))
			RESPONSE = LINES[SELECTED_INDEX]
	else:
		QUOTE_TEXT = ' '.join(QUOTE)
		with open(f'{ASSET_DIR}/Quotes.txt', 'a') as f:
			f.write(f'\n{QUOTE_TEXT}')
		RESPONSE = f'Added the quote "{QUOTE_TEXT}" to the list!' 

	await CTX.send(RESPONSE)

@BOT.command(name='dum', brief='U iz dum.', help='U iz dum.\n\nResponds with either an image or quote calling the requester dumb.', aliases=['d', 'D'])
async def dum(CTX):
	REQUEST_USR = CTX.author
	log(f'Running the dum command for {REQUEST_USR}')
	
	with open(f'{ASSET_DIR}/DumQuotes.txt', 'r') as f:
		LINES = f.read().splitlines()
		SELECTED_INDEX = random.choice(range(0, len(LINES)))
		DUM_LINE = LINES[SELECTED_INDEX]

	if DUM_LINE.endswith('.gif') or DUM_LINE.endswith('.png') or DUM_LINE.endswith('.jpg'):
		await CTX.send(f'{REQUEST_USR.mention}', file=discord.File(f'{ASSET_DIR}/{DUM_LINE}'))
	else:
		await CTX.send(f'{REQUEST_USR.mention} {DUM_LINE}')

@BOT.command(name='yikes', help='Declare a yikes.\n\nSquire will reply with an image/gif that evokes the idea of yikes.', aliases=['y', 'Y'])
async def yikes(CTX):
	REQUEST_USR = CTX.author
	log(f'Running the yikes command for {REQUEST_USR}')

	with open(f'{ASSET_DIR}/YikesQuotes.txt', 'r') as f:
		LINES = f.read().splitlines()
		SELECTED_INDEX = random.choice(range(0, len(LINES)))
		YIKES_LINE = LINES[SELECTED_INDEX]

		await CTX.send(f'{REQUEST_USR.mention}', file=discord.File(f'{ASSET_DIR}/{YIKES_LINE}'))

@BOT.command(name='rollstats', help='Rolls 4d6 and adds the three highest.\n\nIt will either roll the number of stat numbers specified, or that standard 6.', aliases=['rs', 'RS'])
async def roll_stats(CTX, *NUMBER):
	REQUEST_USR = CTX.author
	log(f'Running the roll stats command for {REQUEST_USR}')
	if not NUMBER:
		NUM_DICE = 6
	else:
		NUM_DICE = int(NUMBER[0])

	RESPONSE = ''
	COUNT = 0
	while(COUNT < NUM_DICE):
		DICE_RESULT = dice_roll(4, 6)
		DICE_RESULT.sort(reverse=True)
		DICE_TOTAL = int(DICE_RESULT[0]) + int(DICE_RESULT[1]) + int(DICE_RESULT[2])
		RESPONSE += f'{DICE_TOTAL} ['
		ROLL_COUNT = 1
		for ROLL in DICE_RESULT:
			if ROLL_COUNT == 4:
				ROLL = f'~~{ROLL}~~]\n'
			else:
				ROLL = f'{ROLL}, '
			RESPONSE += ROLL
			ROLL_COUNT += 1

		COUNT += 1

	await CTX.send(RESPONSE)

@BOT.command(name='feedback', help='Replies with the feedback link.\n\nUse the link to report any bugs or request a feature.', aliases=['fb', 'FB'])
async def feedback(CTX):
	REQUEST_USR = CTX.author
	log(f'Running the feedback command for {REQUEST_USR}')

	RESPONSE = f'Got feedback for Squire? You can sumbit it at the following link: {FEEDBACK_LINK}'
	await CTX.send(RESPONSE);

@BOT.event
async def on_ready():
	await BOT.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'v{VERSION} (Try !help)'))
	log(f'{BOT.user.name} has connected to Discord!')

log('Sending bot to server')
BOT.run(TOKEN)
