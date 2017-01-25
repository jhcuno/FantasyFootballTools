from bs4 import BeautifulSoup
import urllib.request
import re

'''
Scraps the league and returns a list with the owner's name to team name
'''
def teamNameToOwnerScrap(url):
    url = url
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')

    realName = soup.find(class_ = "per-info").string
    teamName = str(soup.find(class_ = "team-name"))
    teamName = re.findall(r'>(.+?) <', teamName)
    bothNames = [realName, teamName[0]]
    return bothNames


'''
cycles through the leagues list members.
returning a list of two list.  Team owners and team names.
'''
def cycleAllTeams():
    count = 1

    listRealNames = []
    listTeamNames = []
    listTeamIDNum = []
    listOflists = [listTeamIDNum,listRealNames, listTeamNames]

    #while loop necessary because there is no team#13
    while(count < 16):
        if count == 13:
            count = count + 1
        link = str("http://games.espn.com/ffl/clubhouse?leagueId=424375&teamId="+str(count)+"&seasonId=2016")
        newName = teamNameToOwnerScrap(link)
        listRealNames.append(newName[0])
        listTeamNames.append(newName[1])
        listTeamIDNum.append(count)
        count = count + 1
    return listOflists