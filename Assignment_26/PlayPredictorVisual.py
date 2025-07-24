import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

def Cleaning(Cleaned_Data):

    print("Checking the null values : ")
    print(Cleaned_Data.isnull().sum())
    print(line)

    print("Dropping the unnessary column from data :")
    print(line)
    Cleaned_Data.drop(columns = 'Unnamed: 0', inplace = True)
    print(Cleaned_Data.head())
    print(line)

    # Ecoding the columns

    Cleaned_Data['Whether'] = Cleaned_Data['Whether'].map({'Sunny': 1, 'Overcast': 2, 'Rainy': 3})
    Cleaned_Data['Temperature'] = Cleaned_Data['Temperature'].map({'Hot': 4, 'Mild': 5, 'Cool' : 6})
    Cleaned_Data['Play'] = Cleaned_Data['Play'].map({'Yes': 1, 'No': 0})

    print(line)
    print(Cleaned_Data.head())
    print(line)

    return Cleaned_Data

def Visuals(df):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 8))

    sns.scatterplot(
        x=df['Temperature'],
        y=df['Whether'],
        hue=df['Play'],
        data=df,
        palette='Set1',
        s=100  # dot size
    )

    plt.title("Play Decision by Temperature and Weather")
    plt.xlabel("Temperature")
    plt.ylabel("Weather")
    plt.legend(title='Play')
    plt.grid(True)
    plt.show()


def main():

    DataFrame = PlayPredictor("PlayPredictor.csv")
    Visualize = Visuals(DataFrame)
    cleaned_data = Cleaning(DataFrame)
    

if __name__ == "__main__":
    main()