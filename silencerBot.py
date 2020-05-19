import discord
from random import choice
def hasRole(name='@everyone',list=[]):
    list2=[]
    for i in range(len( list)):
        list2.append(list[i].name)
    if name in list2:
        return True
    else:
        return False
def makeDict(iterator):
    making=[]
    for i in iterator:
        making.append(i)
    made={}
    for i in making:
        made[i[0]]=i[1]
    return made
def isTrue(dict):
    trues=[]
    for i in dict:
        if dict[i]==True:
            trues.append(i)
    return trues
def findIDForRole(name,roleList):
    for i in roleList:
        if i.name==name:
            return i.id
indicators={'a': '\U0001f1e6', 'b': '\U0001f1e7', 'c': '\U0001f1e8', 'd': '\U0001f1e9', 'e': '\U0001f1ea', 'f': '\U0001f1eb', 'g': '\U0001f1ec', 'h': '\U0001f1ed', 'i': '\U0001f1ee', 'j': '\U0001f1ef', 'k': '\U0001f1f0', 'l': '\U0001f1f1', 'm': '\U0001f1f2', 'n': '\U0001f1f3', 'o': '\U0001f1f4', 'p': '\U0001f1f5', 'q': '\U0001f1f6', 'r': '\U0001f1f7', 's': '\U0001f1f8', 't': '\U0001f1f9', 'u': '\U0001f1fa', 'v': '\U0001f1fb', 'w': '\U0001f1fc', 'x': '\U0001f1fd', 'y': '\U0001f1fe', 'z': '\U0001f1ff'}
days='mtwhf'

client = discord.Client()

@client.event
async def on_guild_join(guild):
    await guild.create_role(name='Silenced',reason='Allows muting of rule breakers in the silent-conversation chat.')
    await guild.create_text_channel('silent-conversation',overwrites={guild.get_role(findIDForRole('Silenced',guild.roles)):discord.PermissionOverwrite(send_messages=False)})
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="be quiet."))
@client.event
async def on_message(message):
    if message.content.startswith('tsb!'):
        if message.content.startswith('tsb!perms'):
            await message.channel.send('I have the permissions: '+str(isTrue(makeDict(iter((message.channel.permissions_for(message.channel.guild.me)))))))
        else:
            await message.channel.send("That's not a thing.")
    elif not message.author.bot and not hasRole('The Silent Few',message.author.roles) and message.author!=client.user and not (message.content.startswith('*') and message.content[1]!='*' and not message.content[-2] in ['\\','*'] and message.content[-1]=='*') and message.channel.name=='silent-conversation':
        await message.channel.send(message.author.name+' was silenced.')
        for i in 'quiet':
            await message.add_reaction(indicators[i])
        await message.author.add_roles(message.channel.guild.get_role(findIDForRole('Silenced',message.channel.guild.roles)),reason='The User was too loud.')
client.run('')
