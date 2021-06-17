###########################################
########    DISCORD COUNTER BOT   #########
###########    By NordicSnow   ############
###########################################

import discord, random, sys

client = discord.Client()

#bot token
token = "<please paste discord token here>"

#Phrases for failure.
#Format <phrases> + last count + <phrases1> + username + <phrases2>
#can be as long as you want, but the total number of phrases has to be equal for all three lists
phrases = ["Uh oh, the counter just got killed at "]
phrases1 =[" with "]
phrases2 = [" being to blame! "]


#parses command line arguments
arguments = sys.argv
try:
    channelNum = int(arguments[1]) #game channel number
    victoryNum = int(arguments[2]) + 1 #number it takes to win
    try:
        initialMessageID = int(arguments[3]) #ID of rule message
    except:
        initialMessageUD = 855014284177440798 #sets ID to an arbitrary value if one is not supplied
except:
    print("Error! Please abide by this format when starting:")
    print("counter.py [game channel ID] [target number] [initial message ID (optional)]")

globalCounter = 1

#Describes which messages cannot be deleted. Accepts a discord message object.
def myMessages(m):
    return m.author != client.user and m.id != initialMessageID

#Deletes messages from channel. Accepts a discord message object and a text string describing what happened.
async def purgeMessages(m, finalString):
    global globalCounter
    await m.channel.purge(limit= (globalCounter), check=myMessages)
    phraseNum = random.randint(1, (len(phrases2)-1))
    await m.channel.send(phrases[phraseNum] + str(globalCounter) + phrases1[phraseNum] + m.author.mention + phrases2[phraseNum] + finalString + m.content + "`.")
    globalCounter = 1

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    global channelNum
    if message.author == client.user: # prevents recursive loop
            return

    if message.channel.id == channelNum:
        words = message.content.split() #splits words into a list
        global globalCounter
        try:
            #checks if game finished. If so, print victory and run reward.
            if globalCounter == victoryNum: 
                await message.channel.send("Task Completed. Nice work! Beg <@52522956294721536> for something i guess!")
                globalCounter = globalCounter + 1
                #put some reward here, idk
                return
            
            #checks if the first word of the message is a number that doesn't equal the current count
            #also checks if the count is at 1 and the first word is a number other than 1
            if int(words[0]) != (globalCounter) or (globalCounter == 1 and words[0] != '1'):
                await purgeMessages(message, " The message was: `")
                return
            #otherwise, the count is incremented by one.
            else: globalCounter = globalCounter + 1
        #if the first word is something other than one, this exception happens and the slate is wiped
        except:
            await purgeMessages(message, " The message was: `")
            return

#If a message is edited, the count is failed
@client.event
async def on_message_edit(before, after):
    global channelNum
    global globalCounter
    if before.channel.id == channelNum:
        globalCounter = globalCounter-1 #this reduces the global count by one, since a message has not been added and does not need to be deleted.
        await purgeMessages(after, " They changed their messaged to: `")
        return

#if a message is deleted, the count is also failed
@client.event
async def on_message_delete(message):
    #this makes sure that the bot isn't triggering when it deletes something itself
    if message.author == client.user:
        return
    global channelNum
    if message.channel.id == channelNum:
        await purgeMessages(message, " The message they just deleted was: `")
        return
client.run(token)
