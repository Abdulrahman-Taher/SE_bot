import feedparser
import asyncio
import telegram

TELEGRAM_BOT_TOKEN = '5014571744:AAFBHU3UqfoUAFuv4ZXWv7j00r5mhLIdgDQ'
TELEGRAM_CHAT_ID = '-1001483409081'
PHOTO_PATH = 'https://drive.google.com/file/d/1_oZ7wyPXflD6h-xL-BEPKsTnaYHLeihK/view?usp=sharing'
FEED_URL = 'https://www.livechart.me/feeds/episodes'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

NewsFeed = feedparser.parse(FEED_URL)
entry = NewsFeed.entries[0]
title = entry.title
info1 = title.split("#")
ti1 = info1[0][:-1]
ep1 = info1[1]
x = 0

my_list = """Leadale no Daichi nite
ORIENT
Tokyo 24-ku
Slow Loop
Shikkakumon no Saikyou Kenja
SABIKUI BISCO
Fantasy Bishoujo Juniku Ojisan to
Koroshi Ai
Kimetsu no Yaiba: Yuukaku-hen
Shingeki no Kyojin: The Final Season Part 2
Karakai Jouzu no Takagi-san 3
Tensai Ouji no Akaji Kokka Saisei Jutsu
Vanitas no Carte 2nd Cour
One Piece
BORUTO: NARUTO NEXT GENERATIONS
SHAMAN KING (2021)
Meitantei Conan
Dragon Quest: Dai no Daibouken (2020)
Ousama Ranking"""
list = my_list.split("\n")

my_list2 = """#LeadaleNoDaichiNite
#Orient
#Tokyo24ku
#SlowLoop
#ShikkakumonNoSaikyouKenja
#SabikuiBisco
#FantasyBishoujoJunikuOjisanTo
#KoroshiAi
#KimetsuNoYaiba Yuukaku-hen
#AttackOnTitan Final Season P2
#KarakaiJouzuNoTakagiSan S3
#TensaiOujiNoAkaji
#VanitasNoCarte 2nd Cour
#OnePiece
#Boruto
#ShamanKing
#DetectiveConan
#DragonQuestDai
#OusamaRanking"""
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
