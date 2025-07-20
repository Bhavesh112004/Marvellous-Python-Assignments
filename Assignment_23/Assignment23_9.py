import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    line = "-"*60

    Data = {'Name':['Amit','Sagar','Pooja'],
    'Science':[92, np.nan,80],
    'Math': [np.nan,90,78],
    }

    print(line)
    df = pd.DataFrame(Data)
    print("Original Dataframe with missing values")
    print(df)
    print(line)

    df.fillna(df.mean(numeric_only=True), inplace=True)
    print(df)
    print(line)

    
    

if __name__ == "__main__":
    main()