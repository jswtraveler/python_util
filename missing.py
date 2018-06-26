def missing_ratio(df):
    total=df.isnull().sum()
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent],axis=1, keys=['Total', 'Percent']).sort_values(by='Percent', ascending=False)
    return missing_data
