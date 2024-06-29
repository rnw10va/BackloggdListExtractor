import re
# -*- coding: utf-8 -*-
backloggdWebPage="""

"""
gamesListWithExtraData=re.findall("\t<a href=\"/games/[a-z0-9\-]+/\">",backloggdWebPage)
for gameWithExtraData in gamesListWithExtraData:
   print(gameWithExtraData.split("\t<a href=\"/games/")[1].split("/\">")[0].replace("-"," "))
