## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCpqI7pyJBZV4n0yPrdWrGCnckyuhX104ZiGmR0DrQw_rxtFPbG2WewKCbhXg4pBuo7cwpD4DMPgAi50Wouhl7olSbIFV0Ic9FypCn8xX7wOehB-RAObQxs0ICfKd0Pu7e2d4Fyla0MJ5VcsXHeyJM646DgVs-c_FTZ1T-CiVqyZy-Ui0h3byXPYsiguG-DS5a8itvCze1bRKiiA5iyN3R9F9nDsbM-41BSwdxGD1wO44U8KebFAPfb_JN-C1qDY5TFtXbqZNLkLd0GhR-nBu93JOtfks-i_lf2mZpRAin8ctX4sV4VEMKP_vhg_1rWozZx1uuO8K5LrTbbTrqmQEBEAAAAAUdZJSYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5463206834:AAH_hPF0zrhsO86YGOGQaO7e3PTBqE0RZ_Q")
BOT_NAME = getenv("BOT_NAME", ".𝅯.𝅰.꯭𝅱.𝅲.𝅱.𝅮.꯭𝆫 ✹⃝‌꙰ 𝙎𝙆𝙔𝙇𝘼𝙍⸙𝄞ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ𝆫")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "قناص النجف")
OWNER_USERNAME = getenv("OWNER_USERNAME", "aa_ll_ddd_kk")
ALIVE_NAME = getenv("ALIVE_NAME", "قناص النجف")
BOT_USERNAME = getenv("BOT_USERNAME", "Qw_jlhg_BOT")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "aa_ll_ddd_kk")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "s_32_ss")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "s_32_ss")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5491991846").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
