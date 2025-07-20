import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def main():
    
    data = {'Marks': [85,np.nan,90,np.nan,95]}
    df = pd.DataFrame(data)

    df['Marks'] = df['Marks'].interpolate()

    print(df)

if __name__ == "__main__":
    main()