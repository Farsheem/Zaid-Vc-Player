## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("BQAjvNwGPR0k2fZ6EAQ_fWQeZmfnfjHA32gFk84pZ54wXSG_WjIgrhhP4wVW6Ifzqn2ZtCuoY6x4cW1EL2AYYFrG6o1w4YycmasifC5gYFHollX02Lslrxnq2RTlWljvICPAz86Xs_bJ0EokF48TAb-FLwTg788ovCUgasJonu-sPY2-_o0FItPyvhiI-naPgCVODCiiHA6XcR_qT3ytKL1mcVR6YB-fyTT_NfQ1irmJ-LVKyyLLRPFTN8vAlZ1EF9zmaE7j43Oh7vPxdV6uTyJzf6TaBPwVkqyabXgKDYRZmbdXJkf18gGg-IRbAK5h9y_NTvPo-_exQsv5QE2wNlinf54azQA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5871363571:AAEaR6RdGKDj6P3T5i1fQ1d5zvwQpY2DzAE")
BOT_NAME = getenv("BOT_NAME", "Faizxmuzi_bot")

API_ID = int(getenv("API_ID", "24755516"))
API_HASH = getenv("API_HASH", "f06b275511fff3403ddd75e0534cd48c")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Farsheemfreeze:Faru3936@cluster0.hnr3fqs.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Faiz")
OWNER_USERNAME = getenv("Dark_fantasy_0", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Faiz")
BOT_USERNAME = getenv("BOT_USERNAME", "Faizxmuzi_bot")
OWNER_ID = getenv("OWNER_ID", "1083660482")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "tony_blaze0")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "the_squaaad")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "about_faiz")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1083660482").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
