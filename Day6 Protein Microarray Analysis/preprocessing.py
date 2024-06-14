#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
import pandas as pd
from scipy import stats # only required for Z-Score normalization

#-----------------------------------------------------#
#                   Panel Filtering                   #
#-----------------------------------------------------#
def panel_filtering(dt, panel_path):
    df = pd.read_csv(panel_path, sep='\t')
    df = df.dropna()
    newdf = pd.merge(dt, df, how='outer',on='id')
    newdf = newdf.drop(columns=['uniprotIDs','ncbiIDs'])
    newdf = newdf.dropna()
    #print(newdf.head().to_string())
    return newdf

#-----------------------------------------------------#
#              Control Spot Normalization             #
#-----------------------------------------------------#
def control_spot_norm(dt):
    # newdf = dt.drop(columns=['id', 'position','description'])
    newdf = dt.drop(columns=['id', 'position'])
    newdf = newdf.groupby(['name', 'description']).mean()
    newdf = newdf.reset_index()

    # newdf = pd.merge(dt.loc[:, ['name', 'description']], newdf, how='outer', on='name')
    # return newdf.drop_duplicates(subset='name', keep="last") #.sort_values(by=['name'])
    return newdf
#-----------------------------------------------------#
#         Split Samples into healthy & cancer         #
#-----------------------------------------------------#
def split_samples(dt, path_samples):
    samples = pd.read_csv(path_samples, sep='\t').filter(['Sample_type','Sample_id'])
    #print(dt.head().to_string())
    #print(samples['Sample_type'])
    healthy_list = (samples[samples['Sample_type'].str.contains("Normal")])['Sample_id'].tolist()
    cancer_list =  (samples[samples['Sample_type'].str.contains("Breast Cancer")])['Sample_id'].tolist()
    dt_healthy = dt.drop(columns=cancer_list)
    dt_cancer = dt.drop(columns=healthy_list)
    #dt_healthy = pd.merge(samples, dt_healthy, how='outer', left_on='Sample_id', right_on='customer_id')
    #print(dt_healthy)
    return dt_healthy, dt_cancer

#-----------------------------------------------------#
#       BONUS - Sample Normalization by Z-Score       #
#-----------------------------------------------------#
def sample_norm(dt):
    df = dt.drop(columns=['name','description'])
    #print(df.head().to_string())
    df = df.apply(stats.zscore, axis=0)
    #df = df.apply(lambda x:stats.zscore(df),axis=1) #stats.zscore(df)
    #for (columnName, columnData) in df.iteritems():
     #   df[columnName] = stats.zscore(columnData)
    #for ind, column in enumerate(df.columns):
     #   print(ind, column)
      #  df.iloc[ind] = stats.zscore(column)
        #df[col] = stats.zscore(col.Values)
    #print(df.head().to_string())
    return pd.concat([dt.loc[:, ['name', 'description']],df], axis=1)
