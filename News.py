import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load fake and real news CSV files
def NewsPrediction(Datapath1, Datapath2):
    fake_df = pd.read_csv(Datapath1)
    true_df = pd.read_csv(Datapath2)

    # Add labels (0 = Fake, 1 = Real)
    fake_df["label"] = 0
    true_df["label"] = 1

    # Combine datasets
    df = pd.concat([fake_df, true_df], axis=0)

    # Keep only 'title' or 'text' column (choose one)
    df = df[["text", "label"]]

    # Drop missing values
    df.dropna(inplace=True)

    X = df["text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    log_reg = LogisticRegression(max_iter=1000)
    dt_clf = DecisionTreeClassifier(random_state=42)

    log_reg.fit(X_train_tfidf, y_train)
    dt_clf.fit(X_train_tfidf, y_train)

    # Predictions
    log_reg_pred = log_reg.predict(X_test_tfidf)
    dt_pred = dt_clf.predict(X_test_tfidf)

    print("Logistic Regression Accuracy:", accuracy_score(y_test, log_reg_pred))
    print("Decision Tree Accuracy:", accuracy_score(y_test, dt_pred))

    # Hard Voting (majority rule)
    voting_clf_hard = VotingClassifier(
        estimators=[('lr', log_reg), ('dt', dt_clf)],
        voting='hard'
    )
    voting_clf_hard.fit(X_train_tfidf, y_train)
    hard_pred = voting_clf_hard.predict(X_test_tfidf)

    # Soft Voting (average predicted probabilities)
    voting_clf_soft = VotingClassifier(
        estimators=[('lr', log_reg), ('dt', dt_clf)],
        voting='soft'
    )
    voting_clf_soft.fit(X_train_tfidf, y_train)
    soft_pred = voting_clf_soft.predict(X_test_tfidf)

   
    print("\nHard Voting Accuracy:", accuracy_score(y_test, hard_pred))
    print("Soft Voting Accuracy:", accuracy_score(y_test, soft_pred))

   
    def plot_confusion(y_true, y_pred, title):
        cm = confusion_matrix(y_true, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(title)
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

        plot_confusion(y_test, hard_pred, "Hard Voting Confusion Matrix")
        plot_confusion(y_test, soft_pred, "Soft Voting Confusion Matrix")

        print("\nHard Voting Classification Report:\n", classification_report(y_test, hard_pred))
        print("\nSoft Voting Classification Report:\n", classification_report(y_test, soft_pred))
def main():
    
    NewsPrediction("Fake.csv", "True.csv")

if __name__ == "__main__":
    main()