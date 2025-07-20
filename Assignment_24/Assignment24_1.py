import pandas as pd
import matplotlib.pyplot as plt

def main():
    line = "-"*60

    Data = {'Name':['Amit','Sagar','Pooja'],
    'Science':[92, 88,80],
    'Math': [85,90,78],
    'English' : [75,85,82]
    }
    df = pd.DataFrame(Data)

    df['Math_normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    print(df)


if __name__ == "__main__":
    main()