import os

API_ID = API_ID = 28308147

API_HASH = os.environ.get("API_HASH", "8240cdc945560ccd108b6ff2925ced5e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7296666221:AAE3euVcRc6Nau8jOpcfaj6bGNBu4vcqWMg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5618212564))

LOG = -1002172948859

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5618212564").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
