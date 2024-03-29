# Changelog
## v2.0
* Completely rewrote Squire to use the latest version of the `Discord.py` api
* Split out rolling with advantage/disadvantage into their own separate commands
* Added the ability to apply modifiers to advantage/disadvantage rolls
* Added a `requirements.txt` file to better track dependencies and make installation easier

## v1.4
* Fixed a log issue where runnning the `!roll disadvantage` command would display the higher number instead of the lower one
* Added limits to the number of dice and the number of sides for the `!roll` and `!rollstats` commands
* Changed the `!quote` command to be server unique

## v1.3
* Added the `!feedback` command
* Added a display for the current version of Squire being run
* Fixed formatting on help and error messages
* Modified the `!roll` command to interpret no number of dice to be one
* Added version dependency information to the README
* Fixed minor formatting issues in the CHANGELOG

## v1.2
* Refactored the `!roll` command to be cleaner and simpler
* Simplified the `!rollstat` command using some of the improvements to the `!roll` command
* Added the ability to add modifiers to the `!roll` command

## v1.1
* Added `ASSET_DIRECTORY` to the enviroment variables
* Added the `!rollstats` command
* Modified the commands that require assets to use the path set in the enviroment variables instead of using the current working directory of script

## v1.0
* Added the `!dum`, `!quote`, `!help`, `!roll`, and `!yikes` commands
* Added `DISCORD_TOKEN` to the enviroment variables
