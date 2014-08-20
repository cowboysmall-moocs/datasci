import sys

from sklearn import tree
from clean import clean_data
from predict import make_prediction


def fit_tree(X, y):
    clf = tree.DecisionTreeClassifier(criterion = 'entropy')
    clf.fit(X, y)

    return clf


def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test, fit_tree, './output/prediction_tree.csv')


if __name__ == '__main__':
    main(sys.argv[1:])
