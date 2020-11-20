import discord
from discord.ext import commands

def makeIndicator(letter): ## Python magic
	'''Generates the correct regional indicator emoji for a letter'''
	lets="abcdefghijklmnopqrstuvwxyz"
	maked=eval('"\\U000'+hex(lets.index(letter)+127462)[2:]+'"')
	return maked
class ScheduleMan(commands.Cog):
	def __init__(self,bot,config,key):
		self.bot=bot
	@commands.command()
	async def poll(self,ctx,*,arg):
		"""Starts a yes/no poll"""
		allButAuthor=[]
		for i in ctx.guild.members:
			if i != ctx.author:
				allButAuthor.append(i)
		pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
		if "~" in arg:
			data = arg.split("~",1)
		else:
			data = [arg,"psst... you can set a custom message here by using ~ between the title and description!"]
		toEmbed=discord.Embed(title=data[0],description=data[1],colour=discord.Colour(0xFFFFFF))
		toEmbed.set_author(str(ctx.author),icon_url = ctx.author.avatar_url)
		if "@everyone" in arg:
			send="@everyone"
		else:
			send=None
		sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
		await sent_message.add_reaction('\U00002705')
		await sent_message.add_reaction('\U0000274C')
		if ctx.guild.me.permissions_in(ctx.channel).manage_messages:
			await ctx.message.delete()
	@commands.command()
	async def days(self,ctx,*,arg):
		"""Asks what days people can do something"""
		with ctx.channel.typing():
			allButAuthor=[]
			for i in ctx.guild.members:
				if i != ctx.author:
					allButAuthor.append(i)
			pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
			if "~" in arg:
				data = arg.split("~",1)
			else:
				data = [arg,"psst... you can set a custom message here by using ~ between the title and description!"]
			toEmbed=discord.Embed(title=data[0],description=data[1],colour=discord.Colour(0xFFFFFF))
			toEmbed.set_author(str(ctx.author),icon_url = ctx.author.avatar_url)
			if "@everyone" in arg:
				send="@everyone"
			else:
				send=None
			sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
			for i in "mtwhfs":
				await sent_message.add_reaction(makeIndicator(i))
			await sent_message.add_reaction('\U0000274C')
			await ctx.message.delete()

cogs=[ScheduleMan]
