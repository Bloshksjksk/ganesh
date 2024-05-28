import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token,likeurl
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("**ℍɪɪ** ┈━═𝙈𝙮 𝙁𝙧𝙚𝙞𝙣𝙙═━┈😎\𝙣\𝙣 𝙄 𝘼𝙢 𝘼 𝘽𝙤𝙩 𝙁𝙤𝙧 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙇𝙞𝙣𝙠𝙨 𝙁𝙧𝙤𝙢 𝙔𝙤𝙪𝙧 **.𝙏𝙓𝙏** 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙏𝙝𝙚𝙣 𝙐𝙥𝙡𝙤𝙖𝙙 𝙏𝙝𝙖𝙩 𝙁𝙞𝙡𝙚 𝙊𝙢 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙎𝙤 𝘽𝙖𝙨𝙞𝙘𝙖𝙡𝙡𝙮 𝙄𝙛 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚 𝙁𝙞𝙧𝙨𝙩 𝙎𝙚𝙣𝙙 𝙈𝙚 /upload 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝘼𝙣𝙙 𝙏𝙝𝙚𝙣 𝙁𝙤𝙡𝙡𝙤𝙬 𝙁𝙚𝙬 𝙎𝙩𝙚𝙥𝙨..\n\n #𝙣𝙤𝙩𝙚: 𝙄 𝙖𝙢 𝙊𝙣𝙡𝙮 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 2𝙂𝘽",reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("𝙏𝙍𝙐𝙈𝘽𝙊𝙏𝙎", url="https://t.me/movie_time_botonly"),
                InlineKeyboardButton("𝘾𝙍𝙀𝘼𝙏𝙊𝙍", url="https://t.me/fligher")
                
            ]
        ]
        
    )
)
@bot.on_message(filters.command(["about"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_photo(photo="https://th.bing.com/th/id/OIG4.iV2l1_HaysKkHZXO8DlJ?pid=ImgGn",caption="𝙄 𝘼𝙢 𝘼 𝘽𝙤𝙩 𝙁𝙤𝙧 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙇𝙞𝙣𝙠𝙨 𝙁𝙧𝙤𝙢 𝙔𝙤𝙪𝙧 **.𝙏𝙓𝙏** 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙏𝙝𝙚𝙣 𝙐𝙥𝙡𝙤𝙖𝙙 𝙏𝙝𝙖𝙩 𝙁𝙞𝙡𝙚 𝙊𝙢 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙎𝙤 𝘽𝙖𝙨𝙞𝙘𝙖𝙡𝙡𝙮 𝙄𝙛 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚 𝙁𝙞𝙧𝙨𝙩 𝙎𝙚𝙣𝙙 𝙈𝙚 /upload 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 𝘼𝙣𝙙 𝙏𝙝𝙚𝙣 𝙁𝙤𝙡𝙡𝙤𝙬 𝙁𝙚𝙬 𝙎𝙩𝙚𝙥𝙨..\n\n #𝙣𝙤𝙩𝙚: 𝙄 𝙖𝙢 𝙊𝙣𝙡𝙮 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 2𝙂𝘽",reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("𝙏𝙍𝙐𝙈𝘽𝙊𝙏𝙎", url="https://t.me/movie_time_botonly"),
                InlineKeyboardButton("𝘾𝙍𝙀𝘼𝙏𝙊𝙍", url="https://t.me/fligher")
                
            ]
        ]
        
    )
)


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦\n\n <blockquote>start new one click => /upload </blockquote>", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["upload"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(' 𝙎𝙚𝙣𝙙 𝘼 𝙏𝙚𝙭𝙩 𝙁𝙞𝙡𝙚 𝙏𝙝𝙖𝙩 𝘾𝙤𝙣𝙩𝙖𝙞𝙣𝙨 𝙇𝙞𝙣𝙠 𝙊𝙣𝙚 𝘽𝙮 𝙊𝙣𝙚..🔗 \n\n <b><strong>If You Want to Cancel the task Click</strong></b> => /stop')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**𝕋ᴏᴛᴀʟ ʟɪɴᴋ𝕤 ғᴏᴜɴᴅ ᴀʀᴇ🔗🔗** **{len(links)}**\n\n** Tell No of Links You Wants ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪ𝕤 ** **1**\n\n If It One Means it Will Download 1-link or first link \n\n <b><strong>If You Want to Cancel the task Click</strong></b> => /stop")
    
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your name or refrence**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**𝔼ɴᴛᴇʀ ʀᴇ𝕤ᴏʟᴜᴛɪᴏɴ📸**",reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝟭𝟰𝟰𝗽", callback_data="144"),
                InlineKeyboardButton("𝟮𝟰𝟬𝗽", callback_data="240"),
                InlineKeyboardButton("𝟯𝟲𝟬𝗽", callback_data="360")
            ],
            [
                InlineKeyboardButton("𝟰𝟴𝟬𝗽", callback_data="480"),
                InlineKeyboardButton("𝟳𝟮𝟬𝗽", callback_data="720"),
                InlineKeyboardButton("𝟭𝟬𝟴𝟬𝗽", callback_data="1080")
            ],
            [
                InlineKeyboardButton("cancel/stop", callback_data="stop")
            ]
        ]
    )
)
    input2: CallbackQuery = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
   # await input2.delete(True)
    try:
        if raw_text2 == "144" or input2:
            res = "256x144"
            await m.reply_text(f"Selected resolution: {res}")
            await m.reply_text(f"144")
        elif raw_text2 == "240" or input2:
            res = "426x240"
            await m.reply_text(f"Selected resolution: {res}")
            await m.reply_text(f"240")
        elif raw_text2 == "360" or input2:
            res = "640x360"
            await m.reply_text(f"Selected resolution: {res}")
            await m.reply_text(f"360")
        elif raw_text2 == "480" or input2:
            res = "854x480"
            await m.reply_text(f"Selected resolution: {res}")
        elif raw_text2 == "720" or input2:
            res = "1280x720"
            await m.reply_text(f"Selected resolution: {res}")
        elif raw_text2 == "1080"or input2:
            res = "1920x1080" 
            await m.reply_text(f"Selected resolution: {res}")
        else: 
            res = "UN"
            await m.reply_text("Invalid selection❌")
    except Exception:
            res = "UN"
    
    

    await editable.edit("Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg » https://telegra.ph/file/1bf523c4b51530e57e84d.jpg \n\n Or if don't want thumbnail send = no/n \n\n n=> it will send a Documnet📂\n\n no=> it will send a Video 🎥")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no" or thumb == "n"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {MR} {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[📽️] 𝗩𝗜𝗗_𝗜𝗗:** {str(count).zfill(3)}.\n\n**𝙐𝙋𝙇𝙊𝘼𝘿 𝘽𝙔 ➤**『𝙏𝙍𝙐𝙈𝘽𝙊𝙏𝙎』\n\n**𝙍𝙀𝙌𝙐𝙀𝙎𝙏 𝘽𝙔** » **{raw_text0}**\n\n**𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘➤** {MR}'
                cc1 = f'**[📁] 𝗣𝗗𝗙_𝗜𝗗:** {str(count).zfill(3)}.\n\n**𝙐𝙋𝙇𝙊𝘼𝘿 𝘽𝙔 ➤**『𝙏𝙍𝙐𝙈𝘽𝙊𝙏𝙎』\n\n**𝙍𝙀𝙌𝙐𝙀𝙎𝙏 𝘽𝙔** » **{raw_text0}**\n\n**𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ➤** {MR}'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n\n**📝Name »** `{name}\n\n\n❄Quality » {raw_text2}`\n\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n\n\n{str(e)}\n\n\n**Name** » {name}\n\n\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝗗𝗢𝗡𝗘 𝗕𝗢𝗦𝗦🩷✔️**",reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("GIve 💖 Heart",url=likeurl)
            ]
        ]
    ))


bot.run()
