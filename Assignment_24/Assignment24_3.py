import pandas as pd
import matplotlib.pyplot as plt

def main():
    line = "-"*60

    Data = {'Name':['Amit','Sagar','Pooja'],
    'Gender':['Male', 'Male','Female'],
    'Science':[92, 88,80],
    'Math': [85,90,78],
    'English' : [75,85,82]
    }
    df = pd.DataFrame(Data)


    df['Math_normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    print(df)
    print(line)

    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    print(line)
    print("After Gender Encoding")
    print(line)
    print(df)
    print(line)

    print(line)
    average_by_gender = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print(line)
    print(average_by_gender)
    print(line)
    


if __name__ == "__main__":
    main()