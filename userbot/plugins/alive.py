"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`YO BRO JABTAK YE KHEL KHATAM NHI HOTA APUN IDHARICH HAI ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @A_Dark_Princ3\n"
                     "`Bot created by:` [SnapDragon](tg://user?id=719877937)\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
          """Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""  
import asyncio  
from telethon import events  
from telethon.tl.types import ChannelParticipantsAdmins  
from platform import uname  
from userbot import ALIVE_NAME  
from userbot.utils import admin_cmd  
  
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"  
  
@command(outgoing=True, pattern="^.alive$")  
async def amireallyalive(alive):  
    """ For .alive command, check if the bot is running.  """  
    await alive.edit("**`YO BRO JABTAK YE KHEL KHATAM NHI HOTA APUN IDHARICH HAI ψ(｀∇´)ψ`**\n\n"  
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @cuuuuuu\n"  
                     "`Bot created by:` [𓆩 hassanmuaed 𓆪](tg://user?id=665877797)\n"  
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"  
                     f"`My peru owner`: {DEFAULTUSER}\n"  
                    "[لتنصيب البوت راسلني](t.me/hassanmuaed)")
