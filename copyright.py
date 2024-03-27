from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
import logging

import pyrogram
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

# -------------------------------------------------------------------------------------

BOT_USERNAME = os.environ.get("BOT_USERNAME","ModularCopyrightSaverxDBot")

OWNER_ID = "6329058409"
# -------------------------------------------------------------------------------------

API_ID = "21989020" # 
API_HASH = "3959305ae244126404702aa5068ba15c"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> ⚜ CᴏᴘʏRɪɢʜᴛ Sᴀᴠᴇʀ Bᴏᴛ ⚜
ʜᴇʏ! ɪ ᴀᴍ ᴀ ᴄᴏᴘʏʀɪɢʜᴛ sᴀᴠᴇʀ ʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴛʜɴ. ᴍᴜsᴛ ᴊᴏɪɴ @XovaUpdates ғᴏʀ ᴜᴘᴅᴀᴛᴇs...

๏ 𝙼𝚈 𝚄𝚂𝙴 ? ✨💐
ɪ'ʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴇɴsᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄᴏɴᴛᴇɴᴛ ɪs ғʀᴇᴇ ғʀᴏᴍ ᴀɴʏ ᴘᴏᴛᴇɴᴛɪᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ᴠɪᴏʟᴀᴛɪᴏɴs.

๏ 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴 ? 🍃🥀
ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴡɪᴛʜ sᴏᴍᴇ ʀɪɢʜᴛs ; ʟɪᴋᴇ ᴅᴇʟᴇᴛᴇ & ʙᴀɴ.

🍁 ▸ ʟᴇᴛ's ᴡᴏʀᴋ ᴛᴏɢᴇᴛʜᴇʀ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ ᴀɴᴅ sʜᴀʀᴇ ʏᴏᴜʀ ᴡᴏʀᴋ ᴡɪᴛʜ ᴘᴇᴀᴄᴇ ᴏғ ᴍɪɴᴅ !!

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝖲𝖴𝖬𝖬𝖮𝖭 𝖬𝖤", url=f"https://t.me/THNCopyrightSaverBot?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝖴𝖯𝖣𝖠𝖳𝖤", url=f"https://t.me/TheHKNetwork")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/538a4cab76bdf088cde4f.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("𝖣𝖤𝖵", user_id=OWNER_ID),
            InlineKeyboardButton("𝖴𝖯𝖣𝖠𝖳𝖤𝖲", url="https://t.me/TheHKNetwork"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt", "pom"]

@app.on_message()
async def handle_message(client, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
      #  user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
       # user_mention = from_user.mention
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
        
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
def delete_long_messages(_, m):
    return len(m.text.split()) > 10

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"Hey {user_mention}, please keep your messages short!")
    

# -----------------------------------------------------------------------------------


    
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def keep_reaction_message(client, message: Message):
    pass 
# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪║┏━━━━━━➣║┣⪼ ᴏᴡɴᴇʀ :- @llxHKxll ║┣⪼ ᴘᴀʀᴛ ᴏғ :- @TheHKNetwork║┗━━━━━━➣║╔═════ஜ۩۞۩ஜ════╗║Tʜᴇ Hᴋᴢ Nᴇᴛᴡᴏʀᴋ║ ஜ۩۞۩ஜ════╝╚═════════════════❍⊱❁ """)
app.run()
