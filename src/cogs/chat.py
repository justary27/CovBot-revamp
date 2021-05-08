import discord
from discord.ext.commands import Cog
from discord.ext.commands.core import command
from wit import Wit

responses = ['Hello {}, How may I help?','Good morning {}, May I help you ?']
initiaters=["hi","hello","howdy","how are ya","how are you"]
class Task(Cog):
    def __init__(self, client):
        self.client = client


    @Cog.listener()
    async def on_message(self,msg):
        for x in initiaters:
            if x in str(msg.content):
                pass

    @command(aliases=['hi', 'hii', 'hello'],help='General Interaction')
    async def _hey(self, ctx):
        resp = str(f'Hello ! {ctx.author.mention} How may I help you ? ')
        await ctx.reply(resp)
        await ctx.message.add_reaction("🙋‍♀️")

def setup(client):
    client.add_cog(Task(client))
