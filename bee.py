import discord, asyncio, sys, traceback, checks, useful
from discord.ext import commands

class beeCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.justme()
    async def bee(self, ctx, user):
        userID = useful.getid(user)
        beeScript = useful.getscript()
        tosend = ""
        for counter in range (0, len(beeScript)-1):
            if counter % 2000 == 0 or counter == (len(beeScript)-1):
                if counter % 8000 == 0:
                    await asyncio.sleep(2)
                try:
                    await ctx.guild.get_member(userID).send(tosend)
                    tosend = ""
                except:
                    break
            else:
                tosend += beeScript[counter]


def setup(bot):
    bot.add_cog(beeCog(bot))
