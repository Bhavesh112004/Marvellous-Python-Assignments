import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

    return df

def Prediction(df):

    x = df[['Temperature', 'Whether']]  
    y =df['Play']

    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)

    model = KNeighborsClassifier(n_neighbors = 7)
    model.fit(x_train,y_train)

    y_predict = model.predict(x_test)
    accuracy = accuracy_score(y_test,y_predict)

    print("Accuracy Score is : ",accuracy*100)



def main():

    DataFrame = PlayPredictor("PlayPredictor.csv")
    cleaned_data = Cleaning(DataFrame)
    Model = Prediction(cleaned_data)



if __name__ == "__main__":
    main()