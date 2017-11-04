Something maybe useful:
col = df_2016['finishedsquarefeet15']
big = col[np.abs(df_2016['finishedsquarefeet15']) > 200000]
small = col[np.abs(df_2016['finishedsquarefeet15']) < 200]
def replace(g):
   mask = (g > 200000) or (g < 200)
   g.loc[mask] = g[~mask].mean()
   return g
df_2016['finishedsquarefeet15'].transform(replace)# = df_2016['finishedsquarefeet15']\
.replace(np.abs(df_2016['finishedsquarefeet15'])>20000, df_2016['finishedsquarefeet15'].mean(), regex=True)
df_2016['finishedsquarefeet15'] = df_2016['finishedsquarefeet15'].fillna(df_2016['finishedsquarefeet15'].mean())
for d in data_2016['finishedsquarefeet15']:
    if (d > 200000) or (d < 200):
        d = data_2016['finishedsquarefeet15'].mean()
        d

col_name = df_2016.columns.tolist()  
col_name.insert(1,'year')  
df_2016.reindex(columns=col_name)
col_name = df_2017.columns.tolist()  
col_name.insert(1,'year')  
df_2017.reindex(columns=col_name)

outlier_15 = ts[ts.finishedsquarefeet15>4500].index.tolist()
outlier_15

missing_df = missing_df.ix[missing_df['missing_count']>0]
missing_df = missing_df.sort_values(by='missing_count')

x_cols = [col for col in ts.columns if col not in ['logerror'] if ts[col].dtype=='float64']

labels = []
values = []
for col in x_cols:
    labels.append(col)
    values.append(np.corrcoef(ts[col].values, ts.logerror.values)[0,1])
corr_df = pd.DataFrame({'col_labels':labels, 'corr_values':values})
corr_df = corr_df.sort_values(by='corr_values')
    
ind = np.arange(len(labels))
width = 0.9
fig, ax = plt.subplots(figsize=(12,40))
rects = ax.barh(ind, np.array(corr_df.corr_values.values), color='y')
ax.set_yticks(ind)
ax.set_yticklabels(corr_df.col_labels.values, rotation='horizontal')
ax.set_xlabel("Correlation coefficient")
ax.set_title("Correlation coefficient of the variables")
#autolabel(rects)
plt.show()
ts.head()

