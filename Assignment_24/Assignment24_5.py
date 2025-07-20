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
    
    student = df[df['Name'] == 'Sagar']

    df.drop(columns = ['Gender'], inplace = True)

    scores = student.drop('Name', axis=1).squeeze()  # squeeze() turns it into a Series

    plt.figure(figsize=(6, 6))
    plt.pie(scores, labels=scores.index, autopct='%1.1f%%', startangle=140)
    plt.title('Marks Distribution of Alice')
    plt.show()

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    print(df)
    print(line)

    


if __name__ == "__main__":
    main()