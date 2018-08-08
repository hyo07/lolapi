from riotwatcher import RiotWatcher
from time import sleep
import numpy as np

watcher = RiotWatcher("RGAPI-4cc4a590-7420-45fa-8f9e-4e0a7e6da108")

region = "jp1"
name = "kinopy"

summoner = watcher.summoner.by_name(region, name)
sleep(5)
ranked_state = watcher.league.positions_by_summoner(region, summoner["id"])
sleep(5)
recentmatchlists = watcher.match.matchlist_by_account(region,summoner["accountId"])
sleep(10)

matches = recentmatchlists['matches']
match_detail = []
mode_lsit=[]
data_list =[]
result_lsit = []
decision_list = ["kills", "deaths", "assists", "largestKillingSpree", "largestMultiKill", "killingSprees", "longestTimeSpentLiving",
 "doubleKills", "tripleKills", "quadraKills", "pentaKills", "totalDamageDealt", "magicDamageDealt", "physicalDamageDealt", "trueDamageDealt",
  "largestCriticalStrike", "totalDamageDealtToChampions", "magicDamageDealtToChampions", "physicalDamageDealtToChampions",
   "trueDamageDealtToChampions", "totalHeal", "totalUnitsHealed", "damageSelfMitigated", "damageDealtToObjectives", "damageDealtToTurrets",
    "visionScore", "timeCCingOthers", "totalDamageTaken", "magicalDamageTaken", "physicalDamageTaken", "trueDamageTaken", "goldEarned",
     "goldSpent", "turretKills", "inhibitorKills", "totalMinionsKilled", "neutralMinionsKilled", "champLevel", "visionWardsBoughtInGame", "wardsPlaced",
      "wardsKilled", "firstBloodKill", "firstBloodAssist", "firstTowerKill", "firstTowerAssist", "firstInhibitorKill", "firstInhibitorAssist"]


for x in range(20):
    match_detail.append(watcher.match.by_id(region, matches[x]['gameId']))
    sleep(10)

    if match_detail[x]["gameMode"] == "CLASSIC":
        for data in  match_detail[x]["participantIdentities"]:

            if data["player"]["summonerName"] == name:
                player_num = data["participantId"] - 1

                for n in ["firstBloodKill", "firstBloodAssist", "firstTowerKill", "firstTowerAssist", "firstInhibitorKill", "firstInhibitorAssist"]:
                    if match_detail[x]["participants"][player_num]["stats"].get(n,0) == True:
                        match_detail[x]["participants"][player_num]["stats"][n] = 1
                    if match_detail[x]["participants"][player_num]["stats"].get(n,0) == False:
                        match_detail[x]["participants"][player_num]["stats"][n] = 0

                if match_detail[x]["participants"][player_num]["stats"]["win"] == True:
                    match_detail[x]["participants"][player_num]["stats"]["win"] = 1
                if match_detail[x]["participants"][player_num]["stats"]["win"] == False:
                    match_detail[x]["participants"][player_num]["stats"]["win"] = 0

                data_list.append([match_detail[x]["participants"][player_num]["stats"].get(i,0) for i in decision_list])
                result_lsit.append(match_detail[x]["participants"][player_num]["stats"]["win"])


data = np.array(data_list)
result = np.array(result_lsit)

print(summoner)
print("")
print(data)
print("")
print(result)
