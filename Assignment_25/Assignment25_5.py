import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    

    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
    df = pd.DataFrame(data)

    
    X = df[['Age']]         
    Y = df['Purchased']     

    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train:\n", X_train)
    print("\nX_test:\n", X_test)
    print("\nY_train:\n", Y_train)
    print("\nY_test:\n", Y_test)

if __name__ == "__main__":
    main()