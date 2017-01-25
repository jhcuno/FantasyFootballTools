import matplotlib.pyplot as plt

from dataFrameBuilder import data_frame_builder
plt.style.use('ggplot')


'''
Plots all the teams weekly scores agains each other, line graph, not easy to look at. Too busy.
'''

colors = ['darkblue', 'cornsilk', 'crimson', 'forestgreen', 'gold', 'white', 'lime',
          'silver', 'saddlebrown', 'thistle', 'yellowgreen', 'papayawhip', 'orangered',
          'pink']


def plot_weekly_all_teams(leagueID, weekStart, weekEnd):
    df = data_frame_builder(leagueID, weekStart, weekEnd)
    score_array = df.as_matrix(columns = df.columns[3:])
    x = range(weekStart, weekEnd + 1)
    for i in range(0, score_array.shape[0]):
        # plt.plot(x, scoreArray[i], c = np.random.rand(3,1), label = str(i))
        plt.plot(x, score_array[i], linewidth = 2.0, c=colors[i], label=df.iloc[i,2])
    # plt.legend(bbox_to_anchor=(.5, 0), loc='lower center', ncol=2)
    # plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)
    plt.savefig('allteams.png')
    plt.close()
    # plt.show()


def plot_weekly_partial_teams(league_id, week_start, week_end):
    df = data_frame_builder(league_id, week_start, week_end)
    score_array = df.as_matrix(columns = df.columns[3:])
    x = range(week_start, week_end + 1)
    for i in range(0, 7):
        plt.plot(x, score_array[i], linewidth = 3.0, c=colors[i], label=str(i))
    # plt.legend(bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
    plt.savefig('partialTeams1.png')
    plt.close()
    # plt.show()
    for i in range(7, score_array.shape[0]):
        plt.plot(x, score_array[i], linewidth = 3.0, c=colors[i], label = str(i) )
    plt.savefig('partialTeams2.png')
    # plt.show()
    plt.close()
