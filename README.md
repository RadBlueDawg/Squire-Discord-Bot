# Squire-Discord-Bot
The Squire bot for discord is something I put together for usage on my own personal D&D discord server. In this README, I'll detail the different commands that are available and the setup required if you want to run this bot for yourself.

## Setup
This bot does have one enviroment variable to store the Discord bot token for authentication purposes. All you need to do to get this to run properly is include a file called ".env" in the same directory as the python file with the following text inside it:

`DISCORD_TOKEN={Your-Token-Here}`

Just replace {Your-Token-Here} with whatever your bot token is (Found at [Discord's Developer Portal](https://discordapp.com/developers/applications)).

Also, for the `!quote` and `!dum` commands to work you'll need to create the following two files in the same directory as the script:
- Quotes.txt
- DumQuotes.txt

If you're going to use any images/gifs for the `!dum` command, you'll need to add a new folder called "Assets" in the same directory as the script file.

## Command List
All commands should by prefixed with a '!' character when typed into the Discord chat.

### dum
The bot will call whoever typed this command in dumb in some manner, determined by randomly pulling a line from a text file called `DumQuotes.txt`. I wrote this because I made the big dum. You can have a reaction image/gif instead of a line of text, though that requires a few extra steps. Put the reaction image of your choice inside the `Assets` folder, and then put the name of the file in `DumQuotes.txt` like any other dum quote.

### quote
The bot will either pull a random quote from a text file, or add a specified quote to the text file.

### help
Outputs help text for each of the commands. Whatever Discord automagically puts together.

### r [number-of-dice]d[sides-on-dice]
This is a dice roller command. Format the parameter like you would usually see dice typed out (ex. 1d20, 8d8, etc.).
