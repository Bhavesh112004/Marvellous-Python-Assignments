import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix
import matplotlib.pyplot as plt

def WinePredictor(Datapath):
    df = pd.read_csv(Datapath)

    df.dropna(inplace = True)

    x = df.drop(columns = ['Class'])
    y = df['Class']
    
    scalar = StandardScaler()
    x_scale = scalar.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale,y, test_size = 0.2, random_state = 42)

    accuracy_scores = []
    K_range = range(1,21)
    
    for k in K_range:
        model = KNeighborsClassifier(n_neighbors = k)
        model.fit(x_train, y_train)
        y_predict = model.predict(x_test)
        accuracy = accuracy_score(y_test,y_predict)
        accuracy_scores.append(accuracy)

    plt.figure(figsize = (8,5))
    plt.plot(K_range,accuracy_scores, marker = 'o', linestyle = '--')
    plt.title("Accuracy vs K value")
    plt.xlabel("Value of K")
    plt.ylabel("Acuracy of model")
    plt.grid(True)
    plt.xticks(K_range)
    plt.show()

    best_k = K_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k is : ",best_k)

    model = KNeighborsClassifier(n_neighbors = best_k)
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)

    print("Final Best Accuracy is : ",accuracy*100)
    cm = confusion_matrix(y_test,y_predict)
    print(cm)
        
def main():

    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()