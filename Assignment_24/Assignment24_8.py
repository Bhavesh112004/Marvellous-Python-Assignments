import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    df = pd.read_csv("students_result.csv")

    print(df)

    x = df['Math']  

    sns.histplot(x, bins=5, kde=False, color='skyblue', edgecolor='black')
    plt.title('Distribution of Math Marks')
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()