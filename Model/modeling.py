yesterday = date.today() - timedelta(1)
yesterday = yesterday.strftime("%Y%m%d%H%M%S")[0:8]
section = ['IT과학', '경제', '사회', '생활문화', '세계', '정치']

for i in range(len(section)):
    if i == 0:
        df = pd.read_csv(
            "/Users/jungyulyang/programming/Project_ThematicInvest/Data/today_news_data/{}_{}.csv".format(section[i],
                                                                                                          yesterday),
            header=None, names=['news'], engine='python')
    else:
        new_df = pd.read_csv(
            "/Users/jungyulyang/programming/Project_ThematicInvest/Data/today_news_data/{}_{}.csv".format(section[i],
                                                                                                          yesterday),
            header=None, names=['news'], engine='python')
        df = pd.concat([df, new_df])

df = df.reset_index(drop=True)

for i in range(len(df)):
    if len(df['news'][i]) <= 100:
        df = df.drop(index=i)

df = df.reset_index(drop=True)

df.to_csv(
    "/Users/jungyulyang/programming/Project_ThematicInvest/Data/data_for_use/{}_news_data.csv".format(yesterday))


