import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

def CancerDetection(Datapath):
    line = "-"*150
    df = pd.read_csv(Datapath)

    return df

def DataModify(df):

    df.drop(columns = "CodeNumber", inplace = True)
    #print(df.head())

    df.replace("?", np.nan, inplace = True)
    print(df.isnull().sum())

    df = df.apply(pd.to_numeric, errors='ignore')

    for col in df.select_dtypes(include = [np.number]).columns:
        df[col].fillna(df[col].median(), inplace = True)

    print(df.isnull().sum())
    
    scaler = StandardScaler()

    df = scaler.fit_transform(df)
    df = pd.DataFrame(df)

    return df
    
def main():
   Dataframe =  CancerDetection("breast-cancer-wisconsin.csv")
   Data = DataModify(Dataframe)


if __name__ == "__main__":
    main()