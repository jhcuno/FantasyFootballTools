import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from ScoreSheet import ScoreSheet


scoreSheet = ScoreSheet()
listOfTeamNames = []



def box_score_scrap(url):
    """
    Scrapes the boxscores of the provided urls match-up.  This only scrapes one match-up.  Returning
    one of the teams scores and owners name.  Some of the functionaly should be edited out or added
    to.  Player1 info is currently gathered but not used/returned.
    """
    url = url
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "lxml")

    player0Table = soup.find(id = "playertable_0")
    player0Name = player0Table.find('tr', class_ = "playerTableBgRowHead tableHead playertableTableHeader").string
    player1Table = soup.find(id = "playertable_2")
    player1Name = player1Table.find('tr', class_ = "playerTableBgRowHead tableHead playertableTableHeader").string
    player0Name = player0Name[:-10]     #-10 removes "box score" from strings
    player1Name = player1Name[:-10]
    check_team_name_list(player0Name, listOfTeamNames)
    check_team_name_list(player1Name, listOfTeamNames)

    A = []      #List of active players on team A's roster
    B = []      #List of points scored by each active individual player

    #for loop populates lists A and B
    for row in player0Table.findAll('tr', class_ = 'pncPlayerRow'):
        cells = row.findAll('td')
        if len(cells) == 5:
            A.append(cells[1].find(text = True))
            if cells[4].string == "--":
                B.append(0.0)
            else:
                B.append(float(cells[4].find(text = True)))

    A1 = []     #List of active player on team B's roster
    B1 = []     #List of points scored by each active indidual player

    #for loop populates lists A1 and B1
    for row in player1Table.findAll('tr', class_ = 'pncPlayerRow'):
        cells = row.findAll('td')
        if len(cells) == 5:
            A1.append(cells[1].find(text = True))
            if cells[4].string == "--":
                B1.append(0.0)
            else:
                B1.append(float(cells[4].find(text = True)))

    player0df = pd.DataFrame({'player': A, 'points': B})
    player1df = pd.DataFrame({'player': A1, 'points': B1})
    player0points = round(player0df['points'].sum(), 2)
    player1points = round(player1df['points'].sum(), 2)

    weekly_points_leader(player0points, scoreSheet, player0Name)

    return_list = [player0Name, player0points]
    return return_list


def cycle_weekly_scores(leagueID, weekNum):
    """
    Cycles through all of that weeks games using boxScoreScrape().  Currently assumes a 14 team league.
    Added functionality of finding the leagues size should be found.  To allow for different sized leagues.
    """
    count = 1
    inner_team_names = []
    inner_team_scores = []
    while count < 16:
        if count == 13:
            count += 1
        link = str("http://games.espn.com/ffl/boxscorequick?leagueId="+str(leagueID)+"&teamId="+ str(count) +"&scoringPeriodId=" + str(weekNum) + "&seasonId=2016&view=scoringperiod&version=quick")
        box_score_scrap_list = box_score_scrap(link)
        inner_team_names.append(box_score_scrap_list[0])
        inner_team_scores.append(box_score_scrap_list[1])
        count += 1

    list_name_score = [inner_team_names, inner_team_scores]
    return list_name_score


def weekly_points_leader(points_to_compare, current_leader_score_sheet, points_to_compare_name):
    """
    Determines the highest scoring team for that week.
    """
    if points_to_compare > current_leader_score_sheet.highestWeeklyScore:
        current_leader_score_sheet.highestWeeklyScore = points_to_compare
        current_leader_score_sheet.highestWeeklyScoreHolder = points_to_compare_name


def check_team_name_list(teamName, list):
    """
    Checks to see if a teamName is already on the list
    """
    if teamName not in list:
        list.append(teamName)

