import requests
APIKEY = '7FC42459CDFF49A2BC673FC8E72D5284'
hero_url ='https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key='+APIKEY 

def getMatch(match_id):
	match_url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id='+ match_id +'&key='+ APIKEY
	r = requests.get(match_url)
	print(r.status_code)
	data = r.json()
	result = data["result"]
	#print(result)
	players = result["players"]
	for player in players:
		print(player["gold_spent"])
		print(player)

	#print(players)
def getMatchesFromLeague(league_id):
	league_url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?league_id='+ league_id +'&key='+ APIKEY
	r = requests.get(league_url)
	print(r.status_code)
	data = r.json()
	print(data)

def getMatchesFromTeam(player_id):
	league_url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?account_id='+ player_id+'&tournament_games_only=1&key='+ APIKEY
	r = requests.get(league_url)
	print(r.status_code)
	data = r.json()
	print(data)

def getLeague():
	league_url = 'https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/V001/?key='+APIKEY
	r = requests.get(league_url)
	data = r.json()
	result = data["result"]
	leagues = result["leagues"]
	#print(leagues)
	for l in leagues:
		print(l['name'] + ' : ' + str(l['leagueid']))


def getHeroes():
	r = requests.get(hero_url)
	print(r.status_code)
	print(r.json())

def main():
	print("Main Function")
	#getLeague()
	#getMatchesFromLeague('5401')
	#getHeroes()
	#getMatch('3372726385')
	getMatchesFromTeam('105248644')

if __name__ == "__main__":
	main()