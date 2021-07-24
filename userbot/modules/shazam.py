# Thanks Full To Team Ultroid
#
# Geez - Projects <https://github.com/Vckyou/Geez-UserBot/>
# Ported By Vcky @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
#

from pydub import AudioSegment
from json import dumps
from userbot.events import register
from userbot.modules.sql_helper.shazam_helper.communication import recognize_song_from_signature
from userbot.modules.sql_helper.shazam_helper.algorithm import SignatureGenerator
from requests import get
from os import remove
import urllib.parse
from userbot import CMD_HELP

@register(outgoing=True, pattern="^.shazam")
async def shazam(event):
    if not event.is_reply:
        return await event.edit('`Lütfen Bir Ses Dosyasına Yanıt Veriniz!`')
    else:
        await event.edit('`⬇️ Processing...`')
        reply_message = await event.get_reply_message()
        dosya = await reply_message.download_media()

        await event.edit('`🛠 File audio diterjemahkan ke dalam format...`')
        audio = AudioSegment.from_file(dosya)
        audio = audio.set_sample_width(2)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_channels(1)
            
        signature_generator = SignatureGenerator()
        signature_generator.feed_input(audio.get_array_of_samples())
            
        signature_generator.MAX_TIME_SECONDS = 12
        if audio.duration_seconds > 12 * 3:
            signature_generator.samples_processed += 16000 * (int(audio.duration_seconds / 2) - 6)
            
        results = '{"error": "Not found"}'
        sarki = None
        await event.edit('`🎧 🎤 Uploading...`')
        while True:
            signature = signature_generator.get_next_signature()
            if not signature:
                sarki = results
                break
            results = recognize_song_from_signature(signature)
            if results['matches']:
                sarki = results
                break
            else:
                await event.edit(f'`Pertama {(signature_generator.samples_process / 16000)} Tidak ada yang ditemukan dalam hitungan detik ... Silahkan mencoba lagi.`')
        
        if not 'track' in sarki:
            return await event.edit('`Maaf saya tidak mengerti apa yg anda berikan😔`')
        await event.edit('`✅ Musik Ditemukan!`')
        Caption = f'**Musik:** [{sarki["track"]["title"]}]({sarki["track"]["url"]})\n'
        if 'artists' in sarki['track']:
            Caption += f'**Artis(lar):** [{sarki["track"]["subtitle"]}](https://www.shazam.com/artist/{sarki["track"]["artists"][0]["id"]})\n'
        else:
            Caption += f'**Artis(lar):** `{sarki["track"]["subtitle"]}`\n'

        if 'genres'in sarki['track']:
            Caption += f'**Aliran:** `{sarki["track"]["genres"]["primary"]}`\n'

        if sarki["track"]["sections"][0]["type"] == "SONG":
            for metadata in sarki["track"]["sections"][0]["metadata"]:
                Caption += f'**{"İl" if metadata["title"] == "Sorti" else metadata["title"]}:** `{metadata["text"]}`\n'

        Caption += '\n**Musik Platform:** '
        for provider in sarki['track']['hub']['providers']:
            if provider['actions'][0]['uri'].startswith('spotify:track'):
                Url = provider['actions'][0]['uri'].replace(
                    'spotify:track:', 'http://open.spotify.com/track/'
                )
            elif provider['actions'][0]['uri'].startswith('intent:#Intent;action=android.media.action.MEDIA_PLAY_FROM_SEARCH'):
                Url = f'https://open.spotify.com/search/' + urllib.parse.quote(sarki["track"]["subtitle"] + ' - ' + sarki["track"]["title"])
            elif provider['actions'][0]['uri'].startswith('deezer'):
                Url = provider['actions'][0]['uri'].replace(
                    'deezer-query://', 'https://'
                )
            else:
                Url = provider['actions'][0]['uri']
            Caption += f'[{provider["type"].capitalize()}]({Url}) '
        for section in sarki['track']['sections']:
            if section['type'] == 'VIDEO':
                if 'youtubeurl' in section:
                    Youtube = get(section['youtubeurl']).json()
                else:
                    return

                Caption += f'\n**Video clip:** [Youtube]({Youtube["actions"][0]["uri"]})'

        if 'images' in sarki["track"] and len(sarki["track"]["images"]) >= 1:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                sarki["track"]["images"]["coverarthq"] if 'coverarthq' in sarki["track"]["images"] else sarki["track"]["images"]["background"],
                caption=Caption,
                reply_to=reply_message
                )
        else:
            await event.edit(Caption)  
        remove(dosya)


CMD_HELP.update({"shazam": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.shazam <text>`"
                 "\n↳ : '<respons>', 'Cari file audio yang Anda jawab Shazam."})
