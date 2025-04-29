#-------------------------------------- https://github.com/dakshkohli23/Rename-Pro-Bot --------------------------------------#

import os

class Config(object):    
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7696984863:AAEiUA76NTYiQ2dYlCzxEAaymT_FMnnkKpM")

    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "12655645"))

    API_HASH = os.environ.get("API_HASH", "05c4cafe00b81ed83207bb4365e0053b")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1025922801").split())
    
    # Banned Users...
    #BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # Channels to forward the formatted video (Optional, Prefix: "-100", Bot should be an admin of the channels)
    CHANNEL1_ID = os.environ.get("CHANNEL1_ID", "1714238387")

    CHANNEL1_NAME = os.environ.get("CHANNEL1_NAME", "Mohanrajanrc")

    CHANNEL2_ID = os.environ.get("CHANNEL2_ID")

    #CHANNEL2_NAME = os.environ.get("CHANNEL2_NAME")

    
