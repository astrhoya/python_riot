import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)
from urllib import parse

api_key = 'RGAPI-0bb111ae-6903-49b0-a90b-46ea6b9e6417'
request_header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,es;q=0.7",
                    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://developer.riotgames.com",
                    "X-Riot-Token": api_key
                }

def league_v4_god_league(queue, tier):
    if queue == "solo" :
        queue = "RANKED_SOLO_5x5"
    elif queue == "free" :
        queue = "RANKED_FLEX_SR"
    url = f"https://kr.api.riotgames.com/lol/league/v4/{tier.lower()}leagues/by-queue/{queue}"
    return requests.get(url, headers=request_header).json()


def league_v4_summoner_league(summoner_id):
    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
    return requests.get(url, headers=request_header).json()


def league_v4_league_id(league_id):
    url = f"https://kr.api.riotgames.com/lol/league/v4/leagues/{league_id}"
    return requests.get(url, headers=request_header).json()


#pp.pprint(league_v4_god_league("challenger", "solo")) #솔랭 챌린저 큐
#pp.pprint(league_v4_god_league("challenger", "free")) #자랭 챌린저 큐

#pp.pprint(league_v4_god_league("grandmaster", "solo")) #솔랭 그마 큐
#pp.pprint(league_v4_god_league("grandmaster", "free")) #자랭 그마 큐

#pp.pprint(league_v4_god_league("master", "solo")) #솔랭 마스터 큐
#pp.pprint(league_v4_god_league("master", "free")) #자랭 마스터 큐

#def league_v4_summoner_league(summoner_id):
#    url=f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}" #해당 소환사가 속해 있는 큐
#    return requests.get(url,headers=request_header).json()