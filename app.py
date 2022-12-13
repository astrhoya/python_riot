import flask
import requests
from urllib import parse
import pprint
pp = pprint.PrettyPrinter(indent=4)

api_key = 'RGAPI-0bb111ae-6903-49b0-a90b-46ea6b9e6417'
request_header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
                    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,es;q=0.7",
                    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://developer.riotgames.com",
                    "X-Riot-Token": api_key
                }

def summoner_v4_by_summoner_name(summonerName):
    encodingSummonerName = parse.quote(summonerName)
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{encodingSummonerName}"
    return requests.get(url, headers=request_header).json()
#소환사의 이름으로 정보 출력
#pp.pprint(summoner_v4_by_summoner_name("그 져 빛 챤"))

def summoner_v4_by_accountId(accountId):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-account/{accountId}"
    return requests.get(url, headers=request_header).json()
#소환사의 계정아이디로 정보 출력
#pp.pprint(summoner_v4_by_accountId("1hIWmsO6a4XtGCCykgvQ-yqNfsZGY5Gfinfh_GrLUXZEHLg"))


def summoner_v4_by_puuid(puuid):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    return requests.get(url, headers=request_header).json()
#소환사의 puuid로 정보 출력
#pp.pprint(summoner_v4_by_puuid("sASNI2LyWbvcnhXVhjCC2odVcUliuetQgc-U6RWLe4I_hC9brZ0AfiWjUh3KR3SrEo0WP9DrJvWc8Q"))


def summoner_v4_summoner_name(id):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/{id}"
    return requests.get(url, headers=request_header).json()
#소환사의 아이디로 정보 출력
#pp.pprint(summoner_v4_summoner_name("sKJKrZUSmvxWxJxJcwNauyy_DK6lEEl8O2_WMuSC-fVq3jo"))