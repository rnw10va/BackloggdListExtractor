import re
# -*- coding: utf-8 -*-
backloggdWebPage="""

"""
gamesListWithExtraData=re.findall("\t<a href=\"/games/[a-z0-9\-]+/\">",backloggdWebPage)
listOfGames=[]
for gameWithExtraData in gamesListWithExtraData:
   listOfGames.append(gameWithExtraData.split("\t<a href=\"/games/")[1].split("/\">")[0].replace("-"," "))
print(*set(listOfGames),sep="\n")
