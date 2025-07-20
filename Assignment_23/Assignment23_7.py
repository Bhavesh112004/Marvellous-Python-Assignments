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

    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    print(df)
    print(line)
    
    print(line)
    print("Students who scored above 90 marks in science : ")
    print(line)
    score = df[df['Science'] > 85]
    print(score)
    print(line)

    print("Replacing name Pooja with Puja")
    print(line)
    df['Name'] = df['Name'].replace('Pooja','Puja')
    print(df)
    print(line)

    print(line)
    print("Sorted in decending order of marks")
    df_sorted = df.sort_values(by= 'Total', ascending = False)
    print(df_sorted)
    print(line)

    plt.figure(figsize = (8,5))
    plt.bar(df['Name'],df['Total'], color = 'skyblue')
    plt.xlabel('Student Name')
    plt.ylabel('Total Marks')
    plt.title("Total marks of students")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()