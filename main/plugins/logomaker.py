from pyrogram import filters 
from main import pyrobot, support 
from pyrogram.types import *
from main.makelogo import generate_logo

No_text = """ **ʜᴏᴡ ᴄᴀɴ ɪ ᴄʀᴇᴀᴛᴇ ᴀ ʟᴏɢᴏ 
ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ǫᴜᴇʀʏ ᴘʟs  ғᴏʟʟᴏᴡ ᴏᴜʀ ᴛʏᴘᴇ:**

~ `{} yourname`

**if comes error pls contact @{}**
"""

#livegram

logo1 = "/logo"
logo2 = "/slogo"

@pyrobot.on_message(filters.command("logo"))
async def logo(_, message):
      if len(message.command) <2:
         await message.reply_text(No_text.format(logo1,support))
         return 
      text = message.text.split(None, 1)[1]
      x = await message.reply_text("`🔍 Generating Logo For You...`")  
      logo = await generate_logo(text)
      if "telegra.ph" not in logo:
         return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support")
      
      if "error" in logo:
         return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support \n\n`{logo}`")
      
      await x.edit("`🔄 Done Generated... Now Sending You`")
      logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
      await message.reply_photo(logo,caption="**🖼 Logo Generated By @Nandhabots**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
    
@pyrobot.on_message(filters.command("slogo"))
async def squarelogo(_, message):
      if len(message.command) <2:
         await message.reply_text(No_text.format(logo2,support))
         return 
      text = message.text.split(None, 1)[1]
      x = await message.reply_text("`🔍 Generating Logo For You...`")  
      logo = await generate_logo(text, True)
      if "telegra.ph" not in logo:
         return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support")
      
      if "error" in logo:
         return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @TechZBots_Support \n\n`{logo}`")
      
      await x.edit("`🔄 Done Generated... Now Sending You`")
      logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
      await message.reply_photo(logo,caption="**🖼 Logo Generated By @Nandhabots**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
      

@pyrobot.on_callback_query(filters.regex("flogo"))
async def flogo(_, query):
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By @NandhaBots**")
    await x.delete()
      
      
      
      
