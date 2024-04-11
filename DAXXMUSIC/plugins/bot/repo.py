from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝘿𝙭 𝘾𝙤𝙙𝙚𝙧 𝙍𝙚𝙥𝙤 ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗔𝗕𝗢𝗨𝗧", url="https://t.me/TheAryan_Abouts "),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Dx_Coder"),
          ],
               [
                InlineKeyboardButton("𝗡𝗘𝗢 𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/NeoUpdatess"),

],
[
              InlineKeyboardButton("𝗣𝗥𝗜𝗡𝗖𝗬 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/princymusicbot"),
              InlineKeyboardButton("︎𝗞𝗜𝗗 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/KidMusicBot"),
              ],
              [
              InlineKeyboardButton("𝗕𝗔𝗕𝗬 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/Baby_Music_Robot"),
InlineKeyboardButton("𝗡𝗘𝗢 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/Neo_MusicBot"),
],
[
InlineKeyboardButton("𝗦𝗣𝗜𝗖𝗬 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/F2F_Music_Bot"),
InlineKeyboardButton("𝗝𝗘𝗡𝗡𝗜𝗘 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/JennieMusicBot"),
],
[
              InlineKeyboardButton("𝟵𝘅𝗺 𝗠𝘂𝘀𝗶𝗰", url=f"https://t.me/UniiMusicBot"),
              InlineKeyboardButton("𝗡𝗔𝗠𝗢𝗛 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/Namoh_MusicBot"),
              ],
              [
              InlineKeyboardButton("𝗞𝗬𝗟𝗜𝗘 𝗠𝗨𝗦𝗜𝗖 ", url=f"https://t.me/Kylie_MusicBot"),
InlineKeyboardButton("𝗡𝗔𝗩𝗨 𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/NavuXMusicBot"),
],
[
InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧", url=f"https://t.me/Kid_Management_Bot"),
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗕𝗢𝗧", url=f"https://t.me/The_StringRobot"),
],
[
InlineKeyboardButton("𝗔𝗦𝗞 𝗠𝗘 𝗗𝗠", url=f"https://t.me/Itz_prince_king"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/1828f73a119a92336a0da.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/DAXXTEAM/DAXXMUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[REPO LINK](https://t.me/The_F2F_Shayri) | [GROUP](https://t.me/The_F2F_Dpz)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
