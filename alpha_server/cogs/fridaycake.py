import discord

from discord.ext import commands

class Admin(commands.Cog, name="admin", command_attrs=dict(hidden=True)):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='fridaycake', aliases=['fc'])
	async def reload_all_cogs(self, ctx):
		await ctx.send(':cake::fish_cake::moon_cake::cupcake::pancakes:')

def setup(bot):
	bot.add_cog(Admin(bot))