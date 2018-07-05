import discord, asyncio, sys, traceback, checks, useful
from discord.ext import commands

class beeCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bee(self, ctx, user):
        userID = useful.getid(user)
        beeScript = useful.getscript()
        tosend = ""
        for counter in range (1, len(beeScript)):
            try:
                await ctx.guild.get_member(userID).send(tosend)
                tosend = ""
            except:
                break
            else:
                tosend += beeScript[counter]


def setup(bot):
    bot.add_cog(beeCog(bot))
