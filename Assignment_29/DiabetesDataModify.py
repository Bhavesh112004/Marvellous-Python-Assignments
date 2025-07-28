import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

line = "-"*60
def Diabetes(Datapath):
    df = pd.read_csv(Datapath)

    print(line)
    print("The First few entries of data :")
    print(line)
    print(df.head())

    print(line)
    print("Dimesions of the dataset : ")
    print(line)
    print(df.shape)

    print(line)
    print("The Statistical Analysis of the Data :")
    print(line)
    print(df.describe())

    print(line)
    print("Checking the null values is data : ")
    print(line)
    print(df.isnull().sum())
    print(line)

    return df

def Modifydata(df):
    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols] = df[cols].replace(0, np.nan)

    df[cols]= df[cols].fillna(df[cols].median())

    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])

    print(df.describe())

    
    




def main():
    DataFrame = Diabetes("diabetes.csv")
    Modified_data = Modifydata(DataFrame)

if __name__ == "__main__":
    main()