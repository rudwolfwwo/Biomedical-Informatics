#-----------------------------------------------------#
#                   Library imports                   #
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
#-----------------------------------------------------#

#-----------------------------------------------------#
#              Data Processing Functions              #
#-----------------------------------------------------#
# Read data set in csv function
def read_dataset(path):
    #with open(path,"r") as file:
     #   for f in file.readlines():
      #      print(f.rstrip().split(","))
    df = pd.read_csv(path)
    #print(df.to_string())
    return df

# Data exploration
def exploration(data_set):
    print("head of the data set:")
    print(data_set.iloc[0:5].to_string()) #5 rows
    #patient_with_asd = data_set["ASD"].value_counts()
    patient_with_asd = (data_set["ASD"] == "NO").sum()
    patient_without_asd = (data_set["ASD"] == "YES").sum()
    print("\nthere are %i patients, %i with ASD %i without" %
          (len(data_set),patient_with_asd ,patient_without_asd))
    print("\nthere are " + str(data_set["Entry_Person"].nunique()) + " different categories in 'Entry Person':")
    print(data_set["Entry_Person"].value_counts())
    print("\nthere are following age ranges: \n" + str(data_set["Age_Range"].value_counts()))
    print("\nthe person with highest age is " + str(data_set["Age"].max()) + " years old") #abnormal high age
    print("\nincomplete datacells/patients:\n" + str(data_set.isnull().sum(axis=1).value_counts()))




# Preprocess data
def preprocessing(data_set, categorical_variables, binary_variables,
                  numeric_variables):
    data_set_complete = data_set.dropna() #incomplete data
    print(len(data_set_complete))

    new_df = pd.get_dummies(data_set_complete, columns=categorical_variables,dtype='int')
    for col in binary_variables:
        if col == 'ASD':
            new_df[col] = new_df['ASD'].replace({'YES': 1, 'NO': 0})
        elif col == 'Gender':
            new_df[col] = new_df['Gender'].replace({'m':1,'f':0})
        else:
            new_df[col] = new_df[col].replace({'yes':1,'no':0})
        #new_df[col] = new_df[col].astype(int)
    #new_df = pd.get_dummies(new_df, columns=binary_variables,dtype='int')
    #new_df = pd.get_dummies(new_df, columns=numeric_variables, dtype='int')
    scaler = MinMaxScaler()
    new_df[numeric_variables] = scaler.fit_transform(new_df[numeric_variables])
    return new_df
    #print(new_df.head().to_string())
    #print(new_df.replace({True: 1, False: 0}).head())
    #new_df['Gender_f'] = new_df['Gender_f'].astype(int)

# Split data set
def split_dataset(data_set, y_var, test_size=0.2):
    len_test = int(len(data_set) * test_size) #20%
    len_train = len(data_set) - len_test #80%
    asd = data_set[y_var] #first column
    #train_y = asd.drop(labels=range(0,len_train),axis=0)
    #print(train_y)
    data_wo_asd = data_set.drop(labels=y_var,axis=1)
    test_x = data_wo_asd.drop([data_wo_asd.index[i] for i in range(len_train,len(data_set))])
    train_x = data_wo_asd.drop([data_wo_asd.index[i] for i in range(0,len_train)])
    test_y = asd.drop([asd.index[i] for i in range(len_train,len(data_set))])
    train_y = asd.drop([asd.index[i] for i in range(0,len_train)])
    #print(test_y)
    #print(train_y)
    return train_x, test_x, train_y, test_y
