###########
##UDF CORR
##########

def corr_list(df):
    import numpy as np
    corr = df.corr().abs()
#np.triu returns only the upper triangle of an array. 
#Since a correlation matrix is duplicated, this means there will not be duplicated 
#values with the variable names switched order
#np.ones creates an array of shape n,n -->In this case, corr.shape is the shape so 54 by 54
    os = (corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool))
    .stack()
    .sort_values(ascending=False))

    corr_all=pd.DataFrame(os).reset_index().rename(columns={"index":"Col1",0:"Correlation"})
    return corr_all
