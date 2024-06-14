#-----------------------------------------------------#
#                   Library imports                   #
import pandas as pd
#-----------------------------------------------------#

#-----------------------------------------------------#
#                      GPR Reader                     #
#-----------------------------------------------------#
def read_gpr(path, sample_id):
    df = pd.read_csv(path, compression={'method':'gzip'}, sep='\t', skiprows=33)
    df['id'] = df['ID'].replace(to_replace='.*~', value='', regex=True)
    #df = df.rename(columns={'ID': 'id'})
    df['position'] = df['Block'].astype(str).str.cat(df[['Column', 'Row']].astype(str), sep='-')
    df['name'] = df['Name'].replace(to_replace='~RFU.*', value='', regex=True)
    #df[['Block', 'Column','Row']].apply(lambda x: '-'.join(x), axis=1)
    #df = df.filter(['id','position','name','F635 Median','B635 Median','Intensity'])
    df[sample_id] = df['F635 Median'] - df['B635 Median'] #foreground minus background
    df = df.loc[:,['id','position','name',sample_id]]
    return df