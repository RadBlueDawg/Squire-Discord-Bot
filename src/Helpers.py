#Helpers.py
import random
import time

def current_timestamp():
	localTime = time.localtime(time.time())	
	timestamp = f'{localTime.tm_year}-{localTime.tm_mon}-{localTime.tm_mday}({localTime.tm_hour}-{localTime.tm_min}-{localTime.tm_sec})'
	return timestamp

def console_log(MESSAGE):
	logMessage = f'{current_timestamp()} {MESSAGE}'
	print(logMessage)

def dice_roll(NUMBER, SIDES):
    diceResult = [
        int(random.choice(range(1, SIDES + 1)))
        for _ in range(NUMBER)
    ]

    return diceResult

def format_adv_dis_math_str(ROLL_ARRAY, MODIFIER):
    diceMathStr = f"[({ROLL_ARRAY[0]} ~~{ROLL_ARRAY[1]}~~)"

    if MODIFIER > 0:
        diceMathStr = f"{diceMathStr} + {MODIFIER}"
    elif MODIFIER < 0:
        diceMathStr = f"{diceMathStr} - {abs(MODIFIER)}"

    return f"{diceMathStr}]"

def format_dice_math_str(ROLL_ARRAY, MODIFIER):
    diceMathStr = f"({ROLL_ARRAY[0]}"
    
    diceCount = 1
    while (diceCount < len(ROLL_ARRAY)):
        diceMathStr = f"{diceMathStr} + {ROLL_ARRAY[diceCount]}"
        diceCount += 1
    
    diceMathStr = f"{diceMathStr})"
    if MODIFIER > 0:
        diceMathStr = f"{diceMathStr} + {MODIFIER}"
    elif MODIFIER < 0:
        diceMathStr = f"{diceMathStr} - {abs(MODIFIER)}"

    return diceMathStr

def get_random_line_from_file(FILE_PATH):
    with open(FILE_PATH, 'r') as f:
        allLines = f.read().splitlines()
        selectedLineIndex = random.choice(range(0, len(allLines)))
        return allLines[selectedLineIndex]

def number_valid(INPUT_NUM, MAX_SIZE):
    return INPUT_NUM > 0 and INPUT_NUM <= MAX_SIZE