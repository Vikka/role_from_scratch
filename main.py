# bot.py
import os

from discord import Message, RawReactionActionEvent, Member
from discord.ext.commands import Bot
from discord.utils import get
from dotenv import load_dotenv


class CustomBot(Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)


COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')
bot: CustomBot = CustomBot(command_prefix=COMMAND_PREFIX,
                           case_insensitive=True)

ROLES = {
    729718957958889522: "Python"
}

@bot.event
async def on_ready():
    connected_guilds = [guild for guild in bot.guilds]
    chunks = [f'{bot.user} is connected to the following guild:']
    chunks.extend(list(f'{f"{guild.name}(id: {guild.id})"}'
                       for guild in connected_guilds))
    msg = '\n'.join(chunks)
    print(msg)


@bot.event
async def on_raw_reaction_add(payload: RawReactionActionEvent):
    message_id: int = payload.message_id
    emoji_id: int = payload.emoji.id
    member: Member = payload.member
    if message_id != int(FROM_SCRATCH_MSG_ID):
        return
    role = get(member.guild.roles, name=ROLES[emoji_id])
    print("DONE")
    await member.add_roles(role)


if __name__ == '__main__':
    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    FROM_SCRATCH_GUILD = os.getenv('FROM_SCRATCH_GUILD')
    FROM_SCRATCH_MSG_ID = os.getenv('FROM_SCRATCH_MSG_ID')

    bot.run(TOKEN)
