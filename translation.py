class Translation(object):
    START_TEXT = """Здравствуйте {},
При помощи этого бота вы сможете скачать с Instagram, YouTube, TikTok и т.д."""
    FORMAT_SELECTION = "Выберите нужный формат: <a href='{}'>размер файла может быть приблизительным"
    SET_CUSTOM_USERNAME_PASSWORD = """Если вы хотите скачать видео премиум-класса, предоставьте его в следующем формате:
URL | имя файла | имя пользователя | пароль"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Скачано в {} секунд.\nDetected File Size: {}\nИзвините. Но я не могу загружать файлы размером более 2 ГБ из-за ограничений API Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using me \n\n<b>Join @isIam007 For More UsefUl Bots Like Me </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@isIam07"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Something About Me :
    
   ☞My Name  : All Url Uploader Bot

   ☞Updates  : @isIam07    

   ☞Language : Python3

   ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """Please Follow These steps!
    
1. Send url (example.domain/File.mp4 | New Filename.mp4).
2. Send Image As Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File (video) as file with Screenshots
   Video  - Give File as video without Screenshots
   File   - Give File without Screenshots
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
