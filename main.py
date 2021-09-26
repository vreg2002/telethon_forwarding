from telethon import TelegramClient, sync, events

INPUT_CHANNEL = 'input_channel_username'
OUTPUT_CHANNEL = 'output_channel_username'
TAGS = ['#TAG1', '#TAG2']
import telebot
bot = telebot.TeleBot("2031762379:AAF6vEaCKc_yUOVMuJ3OQRRM2I5hIryzEps")
# 1. Заходим на сайт https://my.telegram.org/apps
# 2. Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.


api_id = 8757085
api_hash = '86e5df9bdb341074646a4b9946a67512'


client = TelegramClient('session_name', api_id, api_hash)




@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):
    for tag in TAGS:

        if tag in str(event.message):

            await client.send_message(OUTPUT_CHANNEL, event.message)

client.start()
client.run_until_disconnected()
