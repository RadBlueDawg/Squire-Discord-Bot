# Squire-Discord-Bot
The Squire bot for discord is something I put together for usage on my own personal D&D discord server. This README details the different commands that are available and the setup required if you want to run this bot for yourself.

## Setup
To install Squire, all you need to do is download and unzip the latest release or download the source code directly. You only need to run the Squire.py file for Squire to start, but before the bot script will be able to run you'll need to follow the additional steps in the sections below.

### Dependencies
Before the bot script can be run, you need to make sure the computer you're running it on has Python 3.9 installed. I'd recommend [setting up a Python virtual environment](https://docs.python.org/3/library/venv.html) in the folder you'll be hosting Squire in. Once you have the virtual environment setup, run `pip install -r requirements.txt` to install the required dependencies.

### Enviroment Variables
In the same folder as the one holding `Squire.py`, create a file called `.env` with the following variables in it:
* `DISCORD_TOKEN`: The bot Discord token you get from the [Discord Developer Portal](https://discordapp.com/developers/applications).
* `ASSETS_DIRECTORY`: The absolute path of the directory you're storing the assets for the `dum` and `yikes` commands. Be sure to format it the same as the system you're running the script on formats it (i.e. " \ " on Windows and " / " on Unix).
* `FEEDBACK_LINK`: The URL link to wherever you're hosting your method of collecting feedback, if you decide to collect it. I set up a simple Google form for mine.

### Required Files and Folders
For the `dum` and `yikes` commands to work you'll need to create the following files in the assets directory set in the `.env` file:
- DumQuotes.txt
- YikesQuotes.txt
