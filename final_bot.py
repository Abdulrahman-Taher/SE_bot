import feedparser
import asyncio
import telegram

TELEGRAM_BOT_TOKEN = '5014571744:AAFBHU3UqfoUAFuv4ZXWv7j00r5mhLIdgDQ'
TELEGRAM_CHAT_ID = '-1001239587631'
PHOTO_PATH = 'https://drive.google.com/file/d/15lT0HEj8RX05Mrcx4lue9Nc5BVTdJWSE/view?usp=sharing'
FEED_URL = 'https://www.livechart.me/feeds/episodes'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

NewsFeed = feedparser.parse(FEED_URL)
entry = NewsFeed.entries[0]
title = entry.title
info1 = title.split("#")
ti1 = info1[0][:-1]
ep1 = info1[1]

list = ['Petit Seka', 'BanG Dream! Garupa☆Pico: Fever!', 'Saiyuki RELOAD -ZEROIN-', 'Gal-gaku. II ~Lucky Stars~', 'Arifureta Shokugyou de Sekai Saikyou 2nd Season']
async def main():
    await asyncio.sleep(60)

while 1:
    NewsFeed = feedparser.parse(FEED_URL)
    entry = NewsFeed.entries[0]
    title = entry.title
    info2 = title.split("#")
    ti2 = info2[0][:-1]
    ep2 = info2[1]
    if ti1 == ti2:
        print('if 1 is true')
        if ti2 in list:
            print('if 2 is true')
            cap = f'═────⊹⋘•♢•⋙⊹────═\n『' +ti2+ f'』┇Episode ' + ep2 + f'\n═────⊹⋘•♢•⋙⊹────═'
            bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=PHOTO_PATH, caption=cap)
    ti1 = ti2
    asyncio.run(main())
