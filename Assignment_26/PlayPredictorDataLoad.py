import pandas as pd

def PlayPredictor(Datapath):
    df = pd.read_csv(Datapath)

    print("Dimensions of the data",df.shape)

    print("First five entries in the data : ")
    print(df.head())

    print("Description of the data : ")
    print(df.describe())

    print("The information about data : ")
    print(df.info())

def main():

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()