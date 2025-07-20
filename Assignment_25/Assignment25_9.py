import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def main():
    
    data = {'Marks': [45,67,88,32,76]}
    df = pd.DataFrame(data)

    df['Marks'] = df['Marks'].apply(lambda x: 'Fail' if x < 50 else x)

    print(df)

if __name__ == "__main__":
    main()