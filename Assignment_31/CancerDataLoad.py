import pandas as pd
from sklearn.datasets import load_breast_cancer

def CancerDetection(Datapath):
    line = "-"*150
    df = pd.read_csv(Datapath)

    print(line)
    print("First five lines of data")
    print(line)
    print(df.head())
    print(line)

    print("Shape of data")
    print(df.shape)
    print(line)

    print("Statistical analysis of the data")
    print(line)
    print(df.describe())
    print(line)

    print("The count of null values")
    print(df.isnull().sum())
    print(line)


def main():
    CancerDetection("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()