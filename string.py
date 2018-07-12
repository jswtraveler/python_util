def string_90(df):
    ninety_unique=pd.DataFrame(columns=["Col_Name", "Ninety", "Total"])
#    for col in df.select_dtypes(include='object').columns.values:
    for col in df.select_dtypes(include=[object]).columns.values:
        freq = df[col].value_counts().cumsum()/df[col].value_counts().sum()
        ninety=freq[freq<=.9].count()
        total=df[col].value_counts().sum()
        ninety_unique = ninety_unique.append(pd.DataFrame({'Col_Name': col, 'Ninety': ninety, 'Total':total },index=[0]))

    return ninety_unique.reset_index(drop=True)
