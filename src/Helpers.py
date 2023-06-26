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

def get_random_line_from_file(FILE_PATH):
    with open(FILE_PATH, 'r') as f:
        allLines = f.read().splitlines()
        selectedLineIndex = random.choice(range(0, len(allLines)))
        return allLines[selectedLineIndex]

def number_valid(INPUT_NUM, MAX_SIZE):
    return INPUT_NUM > 0 and INPUT_NUM <= MAX_SIZE
    #if INPUT_NUM < 1 or INPUT_NUM > MAX_SIZE:
    #    return False
    #else:
    #    return True