import sys

from sklearn import ensemble
from clean import clean_data
from predict import make_prediction


def fit_random_forest(data, target):
    clf = ensemble.RandomForestClassifier()
    clf.fit(data, target)

    return clf


def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test, fit_random_forest, './output/prediction_rf.csv')


if __name__ == '__main__':
    main(sys.argv[1:])
