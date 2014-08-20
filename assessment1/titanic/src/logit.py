import sys

from sklearn import linear_model
from clean import clean_data
from predict import make_prediction


def fit_linear_model(X, y):
    clf = linear_model.LogisticRegression(C = 50)
    clf.fit(X, y)

    return clf


def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test, fit_linear_model, './output/prediction_logit.csv')


if __name__ == '__main__':
    main(sys.argv[1:])
