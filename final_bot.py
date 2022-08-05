import feedparser
import asyncio
import telegram

TELEGRAM_BOT_TOKEN = '5014571744:AAFBHU3UqfoUAFuv4ZXWv7j00r5mhLIdgDQ'
TELEGRAM_CHAT_ID = '-1001483409081'
PHOTO_PATH = 'https://drive.google.com/file/d/1LK7RJimIAbxZj01UWJzR8S1AkW4qgyeF/view?usp=sharing'
FEED_URL = 'https://www.livechart.me/feeds/episodes'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

NewsFeed = feedparser.parse(FEED_URL)
entry = NewsFeed.entries[0]
title = entry.title
info1 = title.split("#")
ti1 = info1[0][:-1]
ep1 = info1[1]
ep1 = '{:0>2}'.format(ep1)
x = 0

my_list = """BORUTO: NARUTO NEXT GENERATIONS
Dragon Quest: Dai no Daibouken (2020)
Meitantei Conan
One Piece
Kingdom 4th Season
Aoashi
Summer Time Render
Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 2nd Season
Engage Kiss
Hataraku Maou-sama!!
Isekai Ojisan
Lycoris Recoil
MADE IN ABYSS: Retsujitsu no Ougonkyo
Overlord IV
SHADOWS HOUSE 2nd Season
Soredemo Ayumu wa Yosetekuru
Yofukashi no Uta"""
list = my_list.split("\n")

my_list2 = """#Boruto
#DragonQuestDai
#DetectiveConan
#OnePiece
#Kingdom S4
#Aoashi
#SummertimeRender
#ClassroomOfTheElite S2
#EngageKiss
#HatarakuMaouSama!!
#IsekaiOjisan
#LycorisRecoil
#MadeInAbyss
#OverlordIV
#ShadowsHouse S2
#SoredemoAyumuWaYosetekuru
#YofukashiNoUta"""
list2 = my_list2.split("\n")

async def main():
    await asyncio.sleep(60)

while 1:
    NewsFeed = feedparser.parse(FEED_URL)
    entry = NewsFeed.entries[0]
    title = entry.title
    info2 = title.split("#")
    ti2 = info2[0][:-1]
    ep2 = info2[1]
    ep2 = '{:0>2}'.format(ep2)
    if ti1 != ti2 or x == 0:
        #print('if 1 is true')
        if ti2 in list:
            #print('if 2 is true')
            ind = list.index(ti2)
            #print(ind)
            ti22 = list2[ind]
            cap = f'═────⊹⋘•♢•⋙⊹────═\n『`%s`』┇EP%s\n═────⊹⋘•♢•⋙⊹────═'
            bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=PHOTO_PATH, caption=cap%(ti22, ep2), parse_mode="MARKDOWN")
            x = 1
    ti1 = ti2
    asyncio.run(main())
