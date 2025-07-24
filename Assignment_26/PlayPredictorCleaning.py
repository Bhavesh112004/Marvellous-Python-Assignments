import pandas as pd


line = "-"*60
def PlayPredictor(Datapath):
    df = pd.read_csv(Datapath)

    print(line)
    print("Dimensions of the data",df.shape)
    print(line)

    print("First five entries in the data : ")
    print(line)
    print(df.head())
    print(line)

    print(line)
    print("Description of the data : ")
    print(line)
    print(df.describe())
    print(line)

    print("The information about data : ")
    print(line)
    print(df.info())
    print(line)

    return df

def Cleaning(df):

    print("Checking the null values : ")
    print(df.isnull().sum())
    print(line)

    print("Dropping the unnessary column from data :")
    print(line)
    df.drop(columns = 'Unnamed: 0', inplace = True)
    print(df.head())
    print(line)

    # Ecoding the columns

    df['Whether'] = df['Whether'].map({'Sunny': 1, 'Overcast': 2, 'Rainy': 3})
    df['Temperature'] = df['Temperature'].map({'Hot': 4, 'Mild': 5, 'Cool' : 6})
    df['Play'] = df['Play'].map({'Yes': 1, 'No': 0})

    print(line)
    print(df.head())
    print(line)

def main():

    DataFrame = PlayPredictor("PlayPredictor.csv")
    cleaned_data = Cleaning(DataFrame)



if __name__ == "__main__":
    main()