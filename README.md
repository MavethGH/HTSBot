# HTSBot
The HackThisSite Discord bot

### Capabilities
Blocks unwanted file extensions, like .exe
Implements reaction roles
Mass bans spam/scam bots

### Commands
`rr message <message>`: Sets `<message>` as the active message for reaction roles.

`rr add <emoji> <role>`: When a user reacts with `<emoji>` on the currently active message, give them `<role>`.

`removebots recent <seconds>`: Currently just bans everybody who joined since `<seconds>` ago. Will eventually make sure they are a bot before banning.

### Config
`bot` folder should contain a `config.json` with the following keys:
`GOOD_FILE_TYPES` -List of file extensions that ARE allowed, like .png or .mp4
`DEBUG_MODE` - Setting this to true makes it easier to test the bot without banning people or doing anything else permanent.