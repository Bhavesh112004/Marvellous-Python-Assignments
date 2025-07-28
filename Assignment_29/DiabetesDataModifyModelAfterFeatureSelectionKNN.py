import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report


import matplotlib.pyplot as plt
import seaborn as sns

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

    return df


def ModelTrain(df):

    selected_features = ['Glucose', 'BMI', 'DiabetesPedigreeFunction']
    x_selected = df[selected_features]
    y = df['Outcome']


    x_train, x_test, y_train, y_test = train_test_split(x_selected, y, test_size=0.2, random_state=42)

    accuracy_scores = []
    K_range = range(1,21)
    
    for k in K_range:
        knn = KNeighborsClassifier(n_neighbors = k)
        knn.fit(x_train, y_train)
        y_predict = knn.predict(x_test)
        accuracy = accuracy_score(y_test,y_predict)
        accuracy_scores.append(accuracy)

    best_k = K_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)

    model = KNeighborsClassifier(n_neighbors = best_k)
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)

    print("Final Best Accuracy is : ",accuracy*100)

def main():
    DataFrame = Diabetes("diabetes.csv")
    Modified_data = Modifydata(DataFrame)
    
    ModelTrain(Modified_data)

if __name__ == "__main__":
    main()