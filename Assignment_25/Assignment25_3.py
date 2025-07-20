import pandas as pd

def main():
    data = {'City' : ['Pune','Mumbai','Delhi','Pune','Delhi']}

    df = pd.DataFrame(data)
    print(df)

    df['City_encoded'] = df['City'].map({'Pune': 0, 'Mumbai': 1, 'Delhi': 2})
    print(df)

if __name__ == "__main__":
    main()