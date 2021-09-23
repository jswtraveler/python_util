def top90cat(fit_df,transform_df,cat_var_list):
    categories = cat_var_list
    for cat in categories:
        if fit_df[cat].nunique()<=10:
            transform_df[cat+'_90'] = transform_df[cat]
        else:
            cat_cnt = pd.DataFrame(train_set[cat].value_counts()).reset_index()
            cat_cnt.columns=[cat,'cnt']
            cat_cnt = cat_cnt.sort_values('cnt',ascending=False)
            cat_cnt['cumul_rt'] = cat_cnt['cnt'].cumsum()/cat_cnt['cnt'].sum()
            transform_df[cat+'_90'] = np.where(transform_df[cat].isin(cat_cnt[cat_cnt['cumul_rt']<=.9][cat].to_list()),transform_df[cat],'other')
    return
