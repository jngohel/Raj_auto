class script(object):

  START_TEXT = """<b>ᴛʜɪꜱ ɪꜱ ꜰɪʟᴇ,ᴠɪᴅᴇᴏꜱ,ɪᴍᴀɢᴇꜱ,ᴀᴜᴅɪᴏ ꜱᴀᴠᴇʀ ʙᴏᴛ. ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ, ᴠɪᴅᴇᴏꜱ, ɪᴍᴀɢᴇꜱ, ᴀᴜᴅɪᴏ ᴏʀ ᴀ ᴘᴏꜱᴛ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀ ꜱʜᴀʀᴀʙʟᴇ ʟɪɴᴋ. ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ᴍᴏɴᴇʏ ʙʏ ꜱʜᴀʀɪɴɢ ᴛʜᴀᴛ ʟɪɴᴋ.

🚫 ɴᴏᴛᴇ -  ᴀᴅᴜʟᴛ ʀᴇꜱᴛʀɪᴄᴛᴇᴅ, ɪꜰ ʏᴏᴜ ʙʀᴇᴀᴋɪɴɢ ʀᴜʟᴇꜱ ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ</b>"""

  FEATURES_TEXT = """<b>ꜰᴇᴀᴛᴜʀᴇꜱ - 

- ɢᴇɴᴇʀᴀᴛᴇ ɪɴꜱᴛᴇɴᴛ ᴇɴᴄʀʏᴘᴛᴇᴅ ꜱʜᴀʀɪɴɢ ʟɪɴᴋ.
- ꜰɪʟᴇ & ᴠɪᴅᴇᴏ ᴏɴʟʏ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.
- ᴇᴀʀɴ ʙʏ ꜱʜᴀʀɪɴɢ ʟɪɴᴋꜱ.
- ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ.
- ᴠᴇʀʏ ᴜꜱᴇʀꜰʀɪᴇɴᴅʟʏ.
- ʀᴇɢᴜʟᴀʀ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇꜱ ᴜᴘᴅᴀᴛᴇꜱ.
- ʟɪɴᴋꜱ ᴀʀᴇ ᴘᴀʀᴍᴀɴᴇɴᴛ ᴜɴᴛɪʟ ᴅᴇʟᴇᴛᴇᴅ ʙʏ ᴀᴅᴍɪɴ.
- 100% ꜱᴀꜰᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ.

/set_shortner - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜱʜᴏʀᴛɴᴇʀ.
/remove_shortner - ʀᴇᴍᴏᴠᴇ ʏᴏᴜʀ ꜱʜᴏʀᴛɴᴇʀ ᴀɴᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅᴇᴅ ᴅᴇꜰᴀᴜʟᴛ.
/set_caption - ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ꜰᴏʀ ʀᴇꜱᴜʟᴛ.
/remove_caption - ʀᴇᴍᴏᴠᴇ ʏᴏᴜʀ ᴀᴅᴅᴇᴅ ᴄᴀᴘᴛɪᴏɴ.
/set_channel - ᴛᴏ ꜱᴇᴛ ᴍᴜʟᴛɪᴘʟᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ꜰᴏʀᴡᴀʀᴅ ᴍᴇꜱꜱᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ.
/remove_channel - ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ.
/set_batch_channel - ᴛᴏ ꜱᴇᴛ ʙᴀᴛᴄʜ ᴄʜᴀɴɴᴇʟ ɪᴅ [<code>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ꜱᴛᴏʀᴇ ʙᴀᴛᴄʜ ꜰɪʟᴇꜱ</code>].
/remove_batch_channel - ᴛᴏ ʀᴇᴍᴏᴠᴇ ʙᴀᴛᴄʜ ᴄʜᴀɴɴᴇʟ.
/batch - ᴛᴏ ꜱᴛᴏʀᴇ ʙᴀᴛᴄʜ ꜰɪʟᴇꜱ.
/info - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴅᴇᴛᴀɪʟꜱ.</b>"""

  NEW_USER_TEXT = """#New_Users

Name - {}
Id - <code>{}</code>
Bot - @{}"""
