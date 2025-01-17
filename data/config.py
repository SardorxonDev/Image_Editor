# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# API_TOKEN = env.str("API_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili


import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = list(os.environ.get("ADMINS"))
IP = str(os.environ.get("ip"))
API_TOKEN = str(os.environ.get("API_TOKEN"))
