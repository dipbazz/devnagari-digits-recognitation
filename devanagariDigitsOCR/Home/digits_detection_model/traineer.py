
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib


# def getAccuracy():
#     pred = clf.predict(features_test)
#     from sklearn.metrics import accuracy_score
#     print("Accuracy score in KNN: ", accuracy_score(pred, labels_test))


def main():
    print("************************** LOADING DATASET **************************")
    digit_dataset = pd.read_csv("digit_data.csv").values

    print("************************** SPLITING DATASET FEATURES AND LABELS **************************")
    digit_features, digit_labels = digit_dataset[:, :-3].astype(int), digit_dataset[:, -1:].astype(int)

    print("************************** SPLITING TRAINING AND TESTING DATA **************************")
    features_train, features_test, labels_train, labels_test = \
        train_test_split(digit_features, digit_labels, test_size=0.2)

    print("************************** USING KNN ALGORITHM **************************")
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(n_neighbors=1)

    print("************************** FITING DATASET IN A MODEL **************************")
    clf.fit(features_train, labels_train)

    joblib.dump(clf, "model_cache/cache.pkl")


if __name__ == "__main__":
    main()
