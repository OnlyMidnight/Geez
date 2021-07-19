""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.geezhelp$")
async def usit(e):
    await e.edit(
        f"Here's something for {DEFAULTUSER} to use it for help_on_update on **Geez-UserBot**:\n"
        "\n[Windows Method](https://telegra.ph/How-to-keep-repo-updated-while-keeping-your-changes-through-windows-cmd-method-04-01)"
        "\n[Kali Linux Method](https://telegra.ph/How-to-keep-OpenUserBot-repo-updated-while-keeping-your-changes-through-Termux-method-04-01)"
        "\n[Ubuntu Linux Method](https://telegra.ph/How-to-keep-OUB-repo-updated-while-keeping-your-changes-through-Ubuntu-Terminal-method-04-01-2)"
        "\n[Gdrive Tutorial](https://telegra.ph/How-To-Setup-Google-Drive-04-03)"
        "\n[video-tutorial](https://youtu.be/us1O-AnWmHA)")


@register(outgoing=True, pattern="^.geezvar$")
async def var(m):
    await m.edit(
        f"Here's a list of VARS for {DEFAULTUSER} on **Geez - UserBot**:\n"
        "\n[HEROKU VARS](https://raw.githubusercontent.com/vckyou/Geez-UserBot/varshelper.txt)")


CMD_HELP.update({
    "geezhelper":
    "`.geezhelp`\
\nUsage: Provide links to update repo guides while you keep your changes on the floor.\
\n`.geezvar`\
\nUsage: Provide vars to cross check for you."
})
