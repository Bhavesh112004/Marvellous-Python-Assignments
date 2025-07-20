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
    print(line)
    print("The Data :")
    print(line)
    print(df)
    print(line)

    df.drop(columns = ['English'], inplace = True)
    print(line)
    print("Data after dropping the English column")
    print(line)
    print(df)
    
if __name__ == "__main__":
    main()