from os import environ
from discord.ext import commands
from discord import AllowedMentions,Game
import datetime

bot = commands.Bot(command_prefix='!',owner_id=600130839870963725,activity=Game(name="!days and !poll",start=datetime.datetime.now()))

emoji_list=[]
emojiIDs=[721544022534914130,721544022216278056,721544022534914120,721544022547759165,721544022237249538,721544022081929226,721544022384181339]
for i in emojiIDs:
    emoji_list.append(bot.get_emoji(i))

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
@bot.command()
async def poll(ctx,*,arg):
    allButAuthor=[]
    for i in ctx.guild.members:
        if i != ctx.author:
            allButAuthor.append(i)
    pingable=AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
    sent_message=ctx.send("{0} asked: {1}".format(ctx.author.mention,arg),allowed_mentions=pingable)
    await sent_message.add_reaction('\U00002705')
    await sent_message.add_reaction('\U0000274C')
@bot.command()
async def days(ctx,*,arg):
    allButAuthor=[]
    for i in ctx.guild.members:
        if i != ctx.author:
            allButAuthor.append(i)
    pingable=AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
    sent_message=ctx.send("{0} asked: {1}".format(ctx.author.mention,arg),allowed_mentions=pingable)
    for i in emoji_list:
        await sent_message.add_reaction(i)
@bot.event #super simple error handling that sends the exception in a discord message
async def on_command_error(context,exception):
    await context.send("Error: ```{}```".format(str(exception)))

bot_token=environ.get('BOT_TOKEN',None)
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
bot.run(bot_token)
