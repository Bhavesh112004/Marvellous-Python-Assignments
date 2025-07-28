import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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

    sns.boxplot(data=df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']])
    plt.title("Boxplot of Scaled Features")
    plt.xticks(rotation=45)
    plt.show()

    cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols] = df[cols].replace(0, np.nan)

    df[cols]= df[cols].fillna(df[cols].median())

    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])

    return df

def Visual(df):
    sns.boxplot(data=df[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']])
    plt.title("Boxplot of Scaled Features")
    plt.xticks(rotation=45)
    plt.show()

def ModelTrain(df):

    x = df.drop(columns = ['Outcome'])
    y = df['Outcome']

    print(x.shape)
    print(y.shape)

    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)

    #logreg = LogisticRegression().fit(x_train, y_train)
    logreg = LogisticRegression().fit(x_train, y_train)

    print("Training Accuracy: ")
    print(logreg.score(x_train,y_train))

    print("Testing Accuracy: ")
    print(logreg.score(x_test,y_test))

    importance = pd.Series(abs(logreg.coef_[0]), index=x.columns)
    importance = importance.sort_values(ascending=False)

    
    importance.plot(kind='bar', figsize=(10,6), title="Feature Importance (Logistic Regression)")
    plt.ylabel("Absolute Coefficient Value")
    plt.tight_layout()
    plt.show()
        

    
def main():
    DataFrame = Diabetes("diabetes.csv")
    Modified_data = Modifydata(DataFrame)
    Data_Visualisation = Visual(Modified_data)
    ModelTrain(Modified_data)

if __name__ == "__main__":
    main()