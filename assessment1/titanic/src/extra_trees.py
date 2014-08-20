import sys

from sklearn import ensemble
from clean import clean_data
from predict import make_prediction


def fit_extra_trees(X, y):
    clf = ensemble.ExtraTreesClassifier(criterion = 'entropy')
    clf.fit(X, y)

    return clf


def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test, fit_extra_trees, './output/prediction_xt.csv')


if __name__ == '__main__':
    main(sys.argv[1:])
