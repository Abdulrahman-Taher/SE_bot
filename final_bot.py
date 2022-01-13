import feedparser
import asyncio
import telegram

TELEGRAM_BOT_TOKEN = '5014571744:AAFBHU3UqfoUAFuv4ZXWv7j00r5mhLIdgDQ'
TELEGRAM_CHAT_ID = '-1001483409081'
PHOTO_PATH = 'https://drive.google.com/file/d/13HOHISS1x6I9Kl6XnAAWXgFlYemH8TVQ/view?usp=sharing'
FEED_URL = 'https://www.livechart.me/feeds/episodes'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

NewsFeed = feedparser.parse(FEED_URL)
entry = NewsFeed.entries[0]
title = entry.title
info1 = title.split("#")
ti1 = info1[0][:-1]
ep1 = info1[1]

my_list = """Kimetsu no Yaiba: Yuukaku-hen
Shingeki no Kyojin: The Final Season Part 2
Sono Bisque Doll wa Koi wo Suru
BORUTO: NARUTO NEXT GENERATIONS
Ousama Ranking
SHAMAN KING (2021)
Vanitas no Carte 2nd Cour
Karakai Jouzu no Takagi-san 3
Princess Connect! Re:Dive Season 2
Akebi-chan no Sailor-fuku
Slow Loop
Dragon Quest: Dai no Daibouken (2020)
One Piece
Hakozume: Koban Joshi no Gyakushuu
Meitantei Conan"""

list = my_list.split("\n")

async def main():
    await asyncio.sleep(60)

while 1:
    NewsFeed = feedparser.parse(FEED_URL)
    entry = NewsFeed.entries[0]
    title = entry.title
    info2 = title.split("#")
    ti2 = info2[0][:-1]
    ep2 = info2[1]
    if ti1 != ti2:
        print('if 1 is true')
        if ti2 in list:
            print('if 2 is true')
            cap = f'═────⊹⋘•♢•⋙⊹────═\n『' +ti2+ f'』┇Episode ' + ep2 + f'\n═────⊹⋘•♢•⋙⊹────═'
            bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=PHOTO_PATH, caption=cap)
    ti1 = ti2
    asyncio.run(main())
