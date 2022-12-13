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

def league_v4_queue_tier_division(queue, tier, division, page_number):
    if division == 1 :
        division = 'I'
    elif division == 2 :
        division = 'II'
    elif division == 3 :
        division = 'III'
    elif division == 4:
        division = 'IV'
    if queue == "solo" :
        queue = "RANKED_SOLO_5x5"
    elif queue == "free" :
        queue = "RANKED_FLEX_SR"
    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}?page={page_number}"
    return requests.get(url, headers=request_header).json()

pp.pprint(league_v4_queue_tier_division("solo", "PLATINUM", 3, 3))
#솔랭 플레티넘 3 3페이지