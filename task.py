from os import environ
import discord
import shlex

def hasRole(name='@everyone',list=[]):
    list2=[]
    for i in range(len( list)):
        list2.append(list[i].name)
    if name in list2:
        return True
    else:
        return False
indicators={'a': '\U0001f1e6', 'b': '\U0001f1e7', 'c': '\U0001f1e8', 'd': '\U0001f1e9', 'e': '\U0001f1ea', 'f': '\U0001f1eb', 'g': '\U0001f1ec', 'h': '\U0001f1ed', 'i': '\U0001f1ee', 'j': '\U0001f1ef', 'k': '\U0001f1f0', 'l': '\U0001f1f1', 'm': '\U0001f1f2', 'n': '\U0001f1f3', 'o': '\U0001f1f4', 'p': '\U0001f1f5', 'q': '\U0001f1f6', 'r': '\U0001f1f7', 's': '\U0001f1f8', 't': '\U0001f1f9', 'u': '\U0001f1fa', 'v': '\U0001f1fb', 'w': '\U0001f1fc', 'x': '\U0001f1fd', 'y': '\U0001f1fe', 'z': '\U0001f1ff'}
days='mtwhfs'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="sm!"))
@client.event
async def on_message(message):
    if message.content.startswith('sm!'):
        cmd=message.content.split('!',1)[1]
        sep=shlex.split(cmd)
        params={}
        params['cmd']=sep[0]
        for i in sep[1:]:
            try:
                params[i.split('=',1)[0]]=i.split('=',1)[1]
            except IndexError:
                params[i.split('=',1)[0]]=True
        if params['cmd'] in ['post','poll']:
            try:
                if params['-ping']:
                    ping=message.channel.guild.default_role.mention
            except KeyError:
                params['-ping']=False
                ping=''
            try:
                if params['-m']:
                    1==1
            except KeyError:
                await message.channel.send('error: no message. use -m="message here"')
                return
            if message.author!=client.user:
                await message.channel.send('{0}: {1} asked: {2} {3}'.format(params['cmd'],message.author.display_name,ping,params['-m']))
            await message.delete(delay=2)
        else:
            await message.channel.send("I'm not sure what ```{0}``` is supposed to be \U0001F610".format())
    elif message.author==message.channel.guild.me and message.content.startswith("post:"):
        for i in days:
            await message.add_reaction(indicators[i])
        await message.add_reaction('\U0000274C')
    elif message.author==message.channel.guild.me and message.content.startswith("poll: "):
        await message.add_reaction('\U00002705')
        await message.add_reaction('\U0000274C')

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
client.run(bot_token)
