import pandas as pd
from teamNameToOwnerNameScrap import cycleAllTeams
from boxScoreScrapFF2016 import cycle_weekly_scores


def data_frame_builder(leagueID, startWeekNum, end_week_num=None):
    """
    Builds the dataFrame of the team_names, owners, week_n scores
    league_id is the leagues ID numerical
    If you want to return a dataFrame for one week just enter league_id, weekNumber. Leave end_week_num blank
    Returns the dataFrame asked for
    """
    list_to_use = cycleAllTeams()

    name_dict = {'ESPN_Team_ID': list_to_use[0],
                 'Owner': list_to_use[1],
                 'Team_Name': list_to_use[2]}

    df = pd.DataFrame(name_dict)

    df2_list_to_use = cycle_weekly_scores(leagueID, startWeekNum)
    df2_dict = {'Team_Name': df2_list_to_use[0],
                'Week_Score_' + str(startWeekNum): df2_list_to_use[1]}
    df2 = pd.DataFrame(df2_dict)
    df_new = pd.merge(df, df2, on='Team_Name', how='outer')

    # if more than one week is being asked for runs for those weeks, end_week_num insclusive
    if (end_week_num != None):
        for i in range(startWeekNum + 1, end_week_num + 1):
            print(i)
            df_list_for_loop = cycle_weekly_scores(leagueID, i)
            df_dict_for_loop = {'Team_Name': df_list_for_loop[0],
                                'Week_Score_' + str(i): df_list_for_loop[1]}
            df_for_loop = pd.DataFrame(df_dict_for_loop)
            print(df_list_for_loop)
            df_new = pd.merge(df_new, df_for_loop, on='Team_Name')
    return df_new
