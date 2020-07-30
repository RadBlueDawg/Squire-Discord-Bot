# Squire-Discord-Bot
[![BCH compliance](https://bettercodehub.com/edge/badge/RadBlueDawg/Squire-Discord-Bot?branch=master)](https://bettercodehub.com/)

The Squire bot for discord is something I put together for usage on my own personal D&D discord server. This README details the different commands that are available and the setup required if you want to run this bot for yourself.

## Setup
### Dependencies
Before the bot script can be run, you need to make sure the computer you're running it on has Python 3.7 installed. You will also need to install the following packages:
- python-dotenv (0.14.0 or greater)
- discord.py (1.3.4 or greater)

### Enviroment Variables
This bot has three enviroment variables. The first is used to store the Discord bot token for authentication purposes, while the second is the path to the folder containing the assets for the commands that require external files. All you need to do to get this to run properly is include a file called ".env" in the same directory as the python file with the following text inside it:

`DISCORD_TOKEN={Your-Token-Here}`

`ASSETS_DIRECTORY={Asset-Dir-Path-Here}`

`FEEDBACK_LINK={Feedback-Form-URL-Here}`

Replace {Your-Token-Here} with whatever your bot token is (Found at [Discord's Developer Portal](https://discordapp.com/developers/applications)). Replace {Asset-Dir-Path-Here} with the path to the directory that will contain all of the external assets. Be sure to format it as the system you're running the script on formats it (i.e. "\" on Windows and "/" on Unix). Replace {Feedback-Form-URL-Here} with the URL of a form you'll be using to collect feedback, if you have one. I set up a simple Google Form for mine.

### Required Files and Folders
For the `!quote`, `!dum`, and `!yikes` commands to work you'll need to create the following files in the assets directory set in the `.env` file:
- Quotes.txt
- DumQuotes.txt
- YikesQuotes.txt

If you're going to use any images/gifs for the `!dum` or `!yikes` command, you'll need to add a new folder called "Assets" in the same directory as the script file.

## Command List
All commands should by prefixed with a '!' character when typed into the Discord chat. Alternatively, commands can be prefixed with the phrase "squire, " in the spirit of bossing the squire around.

[This is a parameter]

*[This is an optional parameter]*

### dum|d|D
The bot will call whoever typed this command in dumb in some manner, determined by randomly pulling a line from a text file called `DumQuotes.txt`. I wrote this because I made the big dum. You can have a reaction image/gif instead of a line of text, though that requires a few extra steps. Put the reaction image of your choice inside the `Assets` folder, and then put the name of the file in `DumQuotes.txt` like any other dum quote.

### feedback|fb|FB
The bot will respond with a message that includes the URL to the feedback form set in the `.env` file.

### help
Outputs help text for each of the commands. Whatever Discord automagically puts together.

### quote|q|Q *[quote-text]*
The bot will either pull a random quote from a text file, or add a specified quote to the text file.

### roll|r|R [number-of-dice]d[sides-on-dice]*[modifier]* OR [disadvantage|dis|d] OR [advantage|adv|a]
This is a dice roller command. Format the parameter like you would usually see dice typed out (ex. 1d20, 8d8+6, 2d6-4, etc.). The command can additionally roll two d20s with advantage or disadvantage, depending on which is specified.

### rollstats|rs|RS *[number-of-stat-rolls]*
This is a special diceroller command. For each 'stat,' 4d6 are rolled and the highest three are added together. The command will roll the number of stats indicated, or a standard 6 by default.

### yikes|y|Y
The bot will display an image/gif that evokes the idea of yikes, determined by randomly choosing from a list of files.
