from os import environ
import discord
import shlex

indicators={'a': '\U0001f1e6', 'b': '\U0001f1e7', 'c': '\U0001f1e8', 'd': '\U0001f1e9', 'e': '\U0001f1ea', 'f': '\U0001f1eb', 'g': '\U0001f1ec', 'h': '\U0001f1ed', 'i': '\U0001f1ee', 'j': '\U0001f1ef', 'k': '\U0001f1f0', 'l': '\U0001f1f1', 'm': '\U0001f1f2', 'n': '\U0001f1f3', 'o': '\U0001f1f4', 'p': '\U0001f1f5', 'q': '\U0001f1f6', 'r': '\U0001f1f7', 's': '\U0001f1f8', 't': '\U0001f1f9', 'u': '\U0001f1fa', 'v': '\U0001f1fb', 'w': '\U0001f1fc', 'x': '\U0001f1fd', 'y': '\U0001f1fe', 'z': '\U0001f1ff'}

def makeInd(letter): ## Python magic does the same as the original thing
    lets="abcdefghijklmnopqrstuvwxyz"
    maked=eval('"\\U000'+hex(lets.index(letter)+127462)[2:]+'"')
    return maked
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="!post and !poll"))
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        cmd=message.content[1:]
        params=cmd.split(" ",1)
        if params[0] in ['post','poll']:
            if message.author!=client.user:
                await message.channel.send('{0}: {2} {1} asked: {3}'.format(params[0],message.author.display_name,params[1]),allowed_mentions=discord.AllowedMentions(everyone=message.author.permissions_in(message.channel).mention_everyone))
            await message.delete(delay=2)
    elif message.author==message.channel.guild.me and message.content.startswith("post:"):
        for i in 'mtwhfs':
            await message.add_reaction(makeInd(i))
        await message.add_reaction('\U0000274C')
        await message.edit(content=message.content.split("post: ",1)[1])
    elif message.author==message.channel.guild.me and message.content.startswith("poll: "):
        await message.add_reaction('\U00002705')
        await message.add_reaction('\U0000274C')
        await message.edit(content=message.content.split("poll: ",1)[1])

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
client.run(bot_token)
