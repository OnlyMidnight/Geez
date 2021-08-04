# SPECIALS THANKS TO TEAM ULTROID
#
# This file is a part of <https://github.com/vckyou/GeezProjects/>
# PLease read the GNU Affero General Public License in
# <https://github.com/vckyou/GeezProjects/blob/master/LICENSE>.
#
# Ported By VICKY <@VckyouuBitch>
# Geez Projects UserBot
# Copyright (C) 2021 GeezProjects
# JANGAN HAPUS CREDIT YA KALO MAU MENGHARGAI SESEORANG!!

import emoji
import re, os
import random
from telethon.utils import get_input_document

from userbot.events import register, bot
from userbot import CMD_HELP

chat = "text2gifBot"

def remove_emoji(string):
    return emoji.get_emoji_regexp().sub(u'', string)


@register(outgoing=True, pattern=r"^\.tgif(?: |$)(.*)")
async def t2g(e):
    eris = await e.edit("`Process...`")
    input_args = e.pattern_match.group(1) 
    if not input_args:
        input_args = "No Text was Given :(("
    args = remove_emoji(input_args)
    try:
        t2g = await e.client.inline_query(chat, args)
        doc = t2g[random.randrange(0, len(t2g) -1)]
        try:
            file = await doc.download_media()
            done = await e.client.send_file(
            e.chat_id,
            file = file,
            reply_to=e.reply_to_msg_id
            )
            os.remove(file)
        except AttributeError:
            # for files, without write Method
            done = await doc.click(
                e.chat_id,
                reply_to=e.reply_to_msg_id)
        await geez.delete()
    except Exception as fn:
        return await geez.delete(f"**ERROR** : `{fn}`")
    await cleargif(done)


async def cleargif(gif_):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=get_input_document(gif_),
                unsave=True,
            )
        )
    except Exception as E:
        LOGS.info(E)


CMD_HELP.update(
    {
        "text_gif": ">`.tgif <text>"
        "\nUsage: Untuk Memberikan Kata Kata Dalam GiF"
    }
)
