import sys

from sklearn import svm
from clean import clean_data
from predict import make_prediction


def fit_svm(X, y):
    clf = svm.SVC(gamma = 0.05, C = 5)
    clf.fit(X, y)

    return clf


def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test, fit_svm, './output/prediction_svm.csv')


if __name__ == '__main__':
    main(sys.argv[1:])
