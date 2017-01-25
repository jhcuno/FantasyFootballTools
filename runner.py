from analyzingResults import plot_weekly_all_teams
from analyzingResults import plot_weekly_partial_teams


print("\n")
league_id = input("LeagueID: ")
week_to_start = input("Week to start building data frame: ")
week_to_start = int(week_to_start)
week_to_end = input("Week to end building data frame (leave blank for one week): ")
week_to_end = int(week_to_end)


plot_weekly_partial_teams(league_id, week_to_start, week_to_end)
plot_weekly_all_teams(league_id, 1, 13)
