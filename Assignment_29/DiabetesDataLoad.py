import pandas as pd

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

def main():
    Diabetes("diabetes.csv")

if __name__ == "__main__":
    main()