# Squire-Discord-Bot
The Squire bot for discord is something I put together for usage on my own personal D&D discord server. This README details the different commands that are available and the setup required if you want to run this bot for yourself.

## Setup
### Dependencies
Before the bot script can be run, you need to make sure the computer you're running it on has Python 3.7 installed. You will also need to install the following packages:
- python-dotenv
- discord.py

### Enviroment Variables
This bot does have one enviroment variable to store the Discord bot token for authentication purposes. All you need to do to get this to run properly is include a file called ".env" in the same directory as the python file with the following text inside it:

`DISCORD_TOKEN={Your-Token-Here}`

Just replace {Your-Token-Here} with whatever your bot token is (Found at [Discord's Developer Portal](https://discordapp.com/developers/applications)).

### Required Files and Folders
For the `!quote`, `!dum`, and `!yikes` commands to work you'll need to create the following files in the same directory as the script:
- Quotes.txt
- DumQuotes.txt
- YikesQuotes.txt

If you're going to use any images/gifs for the `!dum` or `!yikes` command, you'll need to add a new folder called "Assets" in the same directory as the script file.

## Command List
All commands should by prefixed with a '!' character when typed into the Discord chat. Alternatively, commands can be prefixed with the phrase "squire, " in the spirit of bossing the squire around.

[This is a parameter]

*[This is an optional parameter]*

### [dum|d|D]
The bot will call whoever typed this command in dumb in some manner, determined by randomly pulling a line from a text file called `DumQuotes.txt`. I wrote this because I made the big dum. You can have a reaction image/gif instead of a line of text, though that requires a few extra steps. Put the reaction image of your choice inside the `Assets` folder, and then put the name of the file in `DumQuotes.txt` like any other dum quote.

### [quote|q|Q] *[quote-text]*
The bot will either pull a random quote from a text file, or add a specified quote to the text file.

### help
Outputs help text for each of the commands. Whatever Discord automagically puts together.

### [roll|r|R] [number-of-dice]d[sides-on-dice] OR [disadvantage|dis|d] OR [advantage|adv|a]
This is a dice roller command. Format the parameter like you would usually see dice typed out (ex. 1d20, 8d8, etc.). The command can additionally roll two d20s with advantage or disadvantage, depending on which is specified.

### [yikes|y|Y]
The bot will display an image/gif that evokes the idea of yikes, determined by randomly choosing from a list of files.
