# CounterBot
 A discord minigame.

This is a bot for a discord server that allows you to set up a target that your users need to reach. Each message must start with a number that supersedes the last message. This starts at one and can go on as long as you choose. Users are allowed to write anything they want as long as their message begins with a number.

If someone goes out of order, edits, or deletes their message then the channel will be wiped and the game resets (with the final count and the killer displayed).

This is a fun game and has been enjoyed on our server. I'd recommend a 30 second (or longer, depending on how active your server is) chat cooldown to stop people from singlehandedly finishing the count.

To host it, first open the file in a text editor and include a discord bot token in the indicated spot (if you don't know how to get one [look here](https://www.writebots.com/discord-bot-token/)). Then, install ``discord`` via pip from a command line. Then, start the program by typing in 

``python3 counter.py [game channel ID] [target number] [initial message ID (optional)])`` 

The initial message is optional, but allows you to write an explanation ahead of time that the bot will ignore.

If you need any help hit up my email.