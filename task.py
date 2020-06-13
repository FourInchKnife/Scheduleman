from os import environ
import discord
import shlex

def makeInd(letter): ## Python magic does the same as the original thing
    lets="abcdefghijklmnopqrstuvwxyz"
    maked=eval('"\\U000'+hex(lets.index(letter)+127462)[2:]+'"')
    return maked
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game("!days and !poll"))
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        cmd=message.content[1:]
        params=cmd.split(" ",1)[:]
        if params[0] in ['days','poll','time']:
            if message.author!=client.user:
                if type(message.channel.guild.me)==type(message.author):
                    pingable=discord.AllowedMentions(everyone=message.author.permissions_in(message.channel).mention_everyone)
                else:
                    pingable=discord.AllowedMentions(everyone=True)
                await message.channel.send('{0}: {1} asked: {2}'.format(params[0],message.author.display_name,params[1]),allowed_mentions=pingable)
            await message.delete(delay=2)
        elif params[0] == 'clocktest':
            toSend=''
            for i in ['1','2','3','4','5','6','7','8','9','10','11','12']:
                toSend+=':clock{}: :clock{}30: '.format(i,i)
            await message.channel.send(toSend+'<:d20:712019129237897329>')
    elif message.author==message.channel.guild.me and message.content.startswith("days:"):
        emojiGuild=client.get_guild(712731280772694198)
        emojiIDs= [721388045915521075,721383207446118491,721383262106157097,721383310978449439,721383361398046742,721383058841796618,721383108884299797]
        for i in emojiIDs:
            nextEmoji= await emojiGuild.fetch_emoji(i)
            await message.add_reaction(nextEmoji)
        await message.add_reaction('\U0000274C')
        await message.edit(content=('filler'+message.content).split("days: ",1)[1])
    elif message.author==message.channel.guild.me and message.content.startswith("poll: "):
        await message.add_reaction('\U00002705')
        await message.add_reaction('\U0000274C')
        await message.edit(content=('filler'+message.content).split("poll: ",1)[1])
    elif message.author==message.channel.guild.me and message.content.startswith("time: "):
        await message.channel.send('This command has yet to be fully implemented \U00002639')
        await message.edit(content=('filler'+message.content).split("time: ",1)[1])
        

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
client.run(bot_token)
