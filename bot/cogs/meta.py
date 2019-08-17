import datetime

import discord
from discord.ext import commands


class Meta(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def uptime(self, ctx: commands.Context):
        """Tells you how long the bot has been up for."""

        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        fmt = "{h}h {m}m {s}s"
        if days:
            fmt = "{d}d " + fmt

        await ctx.send(
            content="Uptime: {}".format(
                fmt.format(d=days, h=hours, m=minutes, s=seconds)
            )
        )

    @commands.command()
    async def invite(self, ctx: commands.Context):
        """Points the user to the #informational channel,
        which contains invite links.
        """
        await ctx.send(f"Invite link: <https://discord.gg/VGqtadw>")

    @commands.command()
    async def cleanup(self, ctx: commands.Context, limit=None):
        """Deletes the bot's messages for cleanup.
        You can specify how many messages to look for.
        """

        limit = limit or 100

        def is_me(m):
            return m.author.id == self.bot.user.id

        deleted = await ctx.channel.purge(limit=limit, check=is_me)
        await ctx.send(f"Deleted {len(deleted)} message(s)", delete_after=5)
        await ctx.message.add_reaction(self.bot.emoji_rustok)

    @commands.command()
    async def source(self, ctx: commands.Context):
        """Links to the bot GitHub repo."""

        await ctx.send("<https://github.com/cwfitzgerald/RustbotPython> a fork of <https://github.com/ivandardi/RustbotPython>")

    async def cog_command_error(self, ctx: commands.Context, error):
        await ctx.message.clear_reactions()
        await ctx.message.add_reaction("❌")


def setup(bot):
    bot.add_cog(Meta(bot))
