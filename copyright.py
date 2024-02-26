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

BOT_USERNAME = os.environ.get("BOT_USERNAME","ModularCopyRightSaverbot")

OWNER_ID = "6379841493"
# -------------------------------------------------------------------------------------

API_ID = "6435225" # 
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖  𝗠𝗢𝗗𝗨𝗟𝗔𝗥 𝗖𝗢𝗣𝗬𝗥𝗜𝗚𝗛𝗧 𝗦𝗔𝗩𝗘𝗥 🛡️ </b>

🛡️➛ 𝖧𝖾𝗅𝗅𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾! 𝖨 𝖺𝗆 𝗍𝗁𝖾 𝖢𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝖱𝖾𝗆𝗈𝗏𝖾𝗋 𝖡𝗈𝗍, 𝗁𝖾𝗋𝖾 𝗍𝗈 𝗁𝖾𝗅𝗉 𝗒𝗈𝗎 𝖾𝗇𝗌𝗎𝗋𝖾 𝗍𝗁𝖺𝗍 𝗒𝗈𝗎𝗋 𝖼𝗈𝗇𝗍𝖾𝗇𝗍 𝗂𝗌 𝖿𝗋𝖾𝖾 𝖿𝗋𝗈𝗆 𝖺𝗇𝗒 𝗉𝗈𝗍𝖾𝗇𝗍𝗂𝖺𝗅 𝖼𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝗏𝗂𝗈𝗅𝖺𝗍𝗂𝗈𝗇𝗌. 𝖶𝗁𝖾𝗍𝗁𝖾𝗋 𝗒𝗈𝗎 𝗇𝖾𝖾𝖽 𝗍𝗈 𝗋𝖾𝗆𝗈𝗏𝖾 𝖼𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍𝖾𝖽 𝗂𝗆𝖺𝗀𝖾𝗌, 𝗍𝖾𝗑𝗍, 𝗈𝗋 𝖺𝗇𝗒 𝗈𝗍𝗁𝖾𝗋 𝗆𝖺𝗍𝖾𝗋𝗂𝖺𝗅, 𝖨 𝖺𝗆 𝗁𝖾𝗋𝖾 𝗍𝗈 𝖺𝗌𝗌𝗂𝗌𝗍 𝗒𝗈𝗎 𝗂𝗇 𝖼𝗋𝖾𝖺𝗍𝗂𝗇𝗀 𝗈𝗋𝗂𝗀𝗂𝗇𝖺𝗅 𝖺𝗇𝖽 𝗅𝖾𝗀𝖺𝗅𝗅𝗒 𝖼𝗈𝗆𝗉𝗅𝗂𝖺𝗇𝗍 𝖼𝗈𝗇𝗍𝖾𝗇𝗍. 𝖫𝖾𝗍'𝗌 𝗐𝗈𝗋𝗄 𝗍𝗈𝗀𝖾𝗍𝗁𝖾𝗋 𝗍𝗈 𝗉𝗋𝗈𝗍𝖾𝖼𝗍 𝗒𝗈𝗎𝗋 𝗂𝗇𝗍𝖾𝗅𝗅𝖾𝖼𝗍𝗎𝖺𝗅 𝗉𝗋𝗈𝗉𝖾𝗋𝗍𝗒 𝖺𝗇𝖽 𝗌𝗁𝖺𝗋𝖾 𝗒𝗈𝗎𝗋 𝗐𝗈𝗋𝗄 𝗐𝗂𝗍𝗁 𝗉𝖾𝖺𝖼𝖾 𝗈𝖿 𝗆𝗂𝗇𝖽📎.

๏ 𝖧𝖮𝖶 𝖳𝖮 𝖴𝖲𝖤 ➛ 𝖩𝖴𝖲𝖳 𝖠𝖣𝖣 𝖬𝖤 𝖨𝖭 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯 𝖠𝖭𝖣 𝖯𝖱𝖮𝖬𝖮𝖳𝖤 𝖬𝖤 𝖶𝖨𝖳𝖧 𝖲𝖮𝖬𝖤 𝖱𝖨𝖦𝖧𝖳𝖲 ⚠️ """

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝖲𝖴𝖬𝖬𝖮𝖭 𝖬𝖤", url=f"https://t.me/ModularCopyRightSaverbot?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝖴𝖯𝖣𝖠𝖳𝖤", url=f"https://t.me/ModularCopyrights")
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
            InlineKeyboardButton("𝖴𝖯𝖣𝖠𝖳𝖤𝖲", url="https://t.me/ModularCopyrights"),    
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



FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

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
        warning_message = f"@{message.from_user.username} ᴍᴀᴀ ᴍᴀᴛ ᴄʜᴜᴅᴀ ᴘᴅғ ʙʜᴇᴊ ᴋᴇ,\n ʙʜᴏsᴀᴅɪᴋᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀɢʏᴇɢᴀ \n\n ᴅᴇʟᴇᴛᴇ ᴋᴀʀ ᴅɪʏᴀ ᴍᴀᴅᴀʀᴄʜᴏᴅ.\n\n ᴀʙ @iam_daxx ʙʜᴀɪ ᴋᴇ ᴅᴍ ᴍᴇ ᴀᴘɴɪ ᴍᴜᴍᴍʏ ᴋᴏ ʙʜᴇᴊ ᴅᴇ 🍌🍌🍌."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪║┏━━━━━━➣║┣⪼ ᴏᴡɴᴇʀ :- @DaxxSir3 ║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ALLTYPECC║┗━━━━━━➣║╔═════ஜ۩۞۩ஜ════╗║अनंत अखंड अमर अविनाशी║कष्ट हरण है║शंभु कैलाशी║╚═════ஜ۩۞۩ஜ════╝╚═════════════════❍⊱❁ """)
app.run()
