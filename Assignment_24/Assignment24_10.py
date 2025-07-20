import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    df = pd.read_csv("students_result.csv")

    df.rename(columns={'Math': 'Mathematics'}, inplace=True)
    print(df)

    sns.boxplot(y=df['English'])
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.show()


if __name__ == "__main__":
    main()