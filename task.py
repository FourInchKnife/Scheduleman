from os import environ
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'),owner_id=600130839870963725,activity=discord.Game(name="!days and !poll"))

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))
@bot.command()
async def poll(ctx,*,arg):
    allButAuthor=[]
    for i in ctx.guild.members:
        if i != ctx.author:
            allButAuthor.append(i)
    pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
    toEmbed=discord.Embed(title=arg,description="React to this message to tell {0} what you think.".format(ctx.author.name),colour=discord.Colour(0xFFFFFF))
    if "@everyone" in arg:
        send="@everyone"
    else:
        send=None
    sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
    await sent_message.add_reaction('\U00002705')
    await sent_message.add_reaction('\U0000274C')
    await ctx.message.delete()
@bot.command()
async def days(ctx,*,arg):
    with ctx.channel.typing():
        allButAuthor=[]
        for i in ctx.guild.members:
            if i != ctx.author:
                allButAuthor.append(i)
        pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
        toEmbed=discord.Embed(title=arg,description="React to this message to tell {0} what works.".format(ctx.author.name),colour=discord.Colour(0xFFFFFF))
        if "@everyone" in arg:
            send="@everyone"
        else:
            send=None
        sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
        emojiGuild=bot.get_guild(712731280772694198)
        emojiIDs=[721544022534914130,721544022216278056,721544022534914120,721544022547759165,721544022237249538,721544022081929226,721544022384181339]
        for i in emojiIDs:
            nextEmoji= await emojiGuild.fetch_emoji(i)
            await sent_message.add_reaction(nextEmoji)
        await sent_message.add_reaction('\U0000274C')
        await ctx.message.delete()
@bot.event
async def on_message(message):
    await bot.process_commands(message)
@bot.event
async def on_command_error(context,exception):
    if type(exception)!=commands.errors.CommandNotFound:
        toEmbed=discord.Embed(title="That just raised an exception...",description="'{0}' when handling user input '{1}'".format(str(exception),context.message.content),colour=discord.Colour(0xFF0F0F))
        await context.send("",embed=toEmbed)

bot_token=environ.get('BOT_TOKEN')
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
bot.run(bot_token)
