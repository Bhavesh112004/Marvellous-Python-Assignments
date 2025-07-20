import pandas as pd

def main():
    line = "-"*60

    Data = {'Name':['Amit','Sagar','Pooja'],
    'Science':[92, 88,80],
    'Math': [85,90,78],
    'English' : [75,85,82]
    }

    
    df = pd.DataFrame(Data)
    print(line)

    
    print(df)

    print(line)
    print("The dimensions of the dataset :")
    print(line)
    print(df.shape)
   
    print(line)
    print(df.columns)
    print(line)

    print("Statistical Description of data :")
    print(line)
    print(df.describe())
    print(line)

if __name__ == "__main__":
    main()