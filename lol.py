from riotwatcher import RiotWatcher
from time import sleep
import numpy as np
import pandas as pd

watcher = RiotWatcher("{APIkey}")

region = "jp1"
name = "{サモナーネーム}"

summoner = watcher.summoner.by_name(region, name)
ranked_state = watcher.league.positions_by_summoner(region, summoner["id"])
recentmatchlists = watcher.match.matchlist_by_account(region,summoner["accountId"])

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

df1 = pd.DataFrame(data_list, columns=decision_list)
df2 = pd.DataFrame(result_lsit)

df1.to_csv("dataset.csv",sep=",", mode='a',header=False)
df2.to_csv("rabel.csv",sep=",", mode='a',header=False)
#print(summoner)
#print("")
print(df1)
print("")
print(df2)
