import json
import GetHero
import urllib.request
from pprint import pprint

# API Variables
getMatchHistory = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?'
getMatchDetails = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?&match_id='

api_key = '&key=06F26E71DA72FD03C5A1304C565EAA9E'
my_id = 53793164
my_games = '&account_id=53793164'
_mr = '&matches_requested='


# Lobby Type
lobby_types = { 0: 'public', 1:'practice', 2:'tournament', 3:'tutorial', 4:'bot', 5:'team' }

# Game Type
game_types = { 1:'ap', 2:'cm', 3:'rd', 4:'sd', 5:'ar', 6:'?', 7:'diretide', 8:'rcm', 9:'greevling', 10:'tutorial', 11:'mid', 12:'lp', 13:'npp', 15:'yb', 18:'?' }

# Displays information about match, where match is a dictionary obtained from valve api
def ParseMatch (match) :
    mID = match['match_id']
    print("Match ID: " + str(mID))
    GetDetailsForMatch(mID)
    print("\n\n")

# Parses my last n Games 
def GetMyLast (n) :
    request = urllib.request.Request(getMatchHistory + api_key + my_games + _mr + str(n))
    f = urllib.request.urlopen(request)

    response = f.read().decode('utf8')
    jsonobj = json.loads(response)
    
    for match in jsonobj['result']['matches']:
        ParseMatch(match)
    f.close()


def GetDetailsForMatch(match_id):
    request = urllib.request.Request(getMatchDetails + str(match_id) + api_key)
    print("request")
    f = urllib.request.urlopen(request)

    response = f.read().decode('utf8')
    jsonobj = json.loads(response)

    gamemode = game_types[jsonobj['result']['game_mode']]
    pprint(gamemode)
    
GetMyLast(45)
