import sys
import csv

from sklearn import preprocessing, cross_validation, metrics, dummy
from clean import clean_data


def fit_dummy(X, y):
    clf = dummy.DummyClassifier()
    clf.fit(X, y)

    return clf


def cross_validation_score(clf, X, y, results, name):
    print
    print 'Cross Validation: ', name
    print
    print metrics.classification_report(y, results)
    print
    print 'Cross Validation: Score = ', cross_validation.cross_val_score(clf, X, y).mean()
    print


def make_prediction(df_train, df_test, fit_model = fit_dummy, output_file = './output/prediction_dummy.csv'):
    X = preprocessing.scale(df_train.drop(['PassengerId', 'Survived'], 1))
    y = df_train['Survived']

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, train_size = 0.5)

    clf     = fit_model(X_train, y_train)
    results = clf.predict(X_test)
    cross_validation_score(clf, X_test, y_test, results, 'Test Data')


    X_predict = preprocessing.scale(df_test.drop(['PassengerId'], 1))
    ids       = df_test['PassengerId']

    clf     = fit_model(X, y)
    results = clf.predict(X_predict)

    with open(output_file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PassengerId', 'Survived'])
        for i in xrange(len(results)):
            writer.writerow([ids[i], results[i]])


def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test)


if __name__ == '__main__':
    main(sys.argv[1:])

