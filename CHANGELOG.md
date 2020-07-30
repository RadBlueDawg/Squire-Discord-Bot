# Changelog
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
