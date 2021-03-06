import requests
import xlwt
APIKEY = '7FC42459CDFF49A2BC673FC8E72D5284'

listMatch = ['3168267304','3168326700','3173910801','3174044578','3174172918','3174252897','3175552353','3175652467','3176294300','3176445805','3176588039','3176700913'\
			,'3190155899','3190241106','3190695983','3190848836','3194342552','3194453869','3194597378','3195266432','3195383160','3195573037','3195686768','3195817999'\
			,'3226319720','3226426077','3226549989','3226894905','3227061790','3228512352','3228618966','3228786798','3230425517','3230524940','3235483600','3235705862'\
			,'3235896984','3238540842','3238795882','3241360537','3241475535','3241665434','3241825287','3327855394','3327943594','3328038592','3328081715','3330036964'\
			,'3330147109','3330224716','3330264429','3330335155','3351961375','3352061045','3352286942','3352327788','3352462460','3352505678','3353935410','3354000170'\
			,'3354210396','3354247448','3356044327','3356102779','3356251885','3356308437','3358011344','3358109772','3362113115','3362175204','3362247584','3364267872'\
			,'3364308762','3364351128','3367820228','3367897602','3368158118','3368249009','3368300783','3370307979','3370363807','3372269708','3372386596','3372455628'\
			,'3372622939','3372676225','3372726385']
radOrNot = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1\
			,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1\
			,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0\
			,0,1,1,0,1,0]

def getMatch(match_id, rad,result):
	match_url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id='+ match_id +'&key='+ APIKEY
	r = requests.get(match_url)
	print(r.status_code)
	data = r.json()
	resultjson = data["result"]
	#print(result)
	players = resultjson["players"]

	total_gold_spent_rad = 0
	total_level_rad = 0
	total_assist_rad = 0
	total_kill_rad = 0


	total_gold_spent_dire = 0
	total_level_dire = 0
	total_assist_dire = 0
	total_kill_dire = 0

	result_match = 0
	for i in range(0,len(players)):
		
		if (i<5):
			total_gold_spent_rad += players[i]["gold_spent"]
			total_level_rad += players[i]["level"]
			total_assist_rad += players[i]["assists"]
			total_kill_rad += players[i]["kills"]
		else: 
			total_gold_spent_dire += players[i]["gold_spent"]
			total_level_dire += players[i]["level"]
			total_assist_dire += players[i]["assists"]
			total_kill_dire += players[i]["kills"]
	
	if rad:
		gold_diff = total_gold_spent_rad - total_gold_spent_dire
		level_diff = (total_level_rad - total_level_dire)/5
		assists_diff = total_assist_rad - total_assist_dire
		kills_diff = total_kill_rad - total_kill_dire
		if (resultjson["radiant_win"]==True):
			result_match = 1
		else:
			result_match = 0
	else: 
		gold_diff = - total_gold_spent_rad + total_gold_spent_dire
		level_diff = (- total_level_rad + total_level_dire)/5
		assists_diff = -total_assist_rad + total_assist_dire
		kills_diff = -total_kill_rad + total_kill_dire
		if (resultjson["radiant_win"]==False):
			result_match = 1
		else:
			result_match = 0

	#wind_or_not = resultjson["radiant_win"]
	#print(result_match)
	data = [match_id,'x0',result_match,'x1', 'x2',level_diff,gold_diff, 'x5',assists_diff,kills_diff]
	result.append(data)

	# for player in players:
	# 	print(player["gold_spent"])
	# 	print(player)

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
	hero_url ='https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key='+APIKEY 
	r = requests.get(hero_url)
	print(r.status_code)
	print(r.json())

def writeResultToCSV(result):
	book = xlwt.Workbook(encoding="utf-8")
	sheet1 = book.add_sheet("Sheet 1")
	row = 0
	for l in result:
	    col = 0
	    for e in l:
	        if e:
	          sheet1.write(row, col, e)
	        col+=1
	    row+=1
	book.save("trial.xls")

def main():
	print("Main Function")
	result = []
	result.append(['Match ID','Versus Team','Result','Diff Of Highest MMR','Diff Of Average MMR','Diff Level','Diff Gold','Diff Ward','Diff Assists','Diff Kill'])
	#getLeague()
	#getMatchesFromLeague('5401')
	#getHeroes()
	for i in range(0,len(listMatch)):
		getMatch(listMatch[i],radOrNot[i],result)
	#getMatch('3372726385',1,result)
	#print(result)
	writeResultToCSV(result)
	#getMatchesFromTeam('105248644')

if __name__ == "__main__":
	main()