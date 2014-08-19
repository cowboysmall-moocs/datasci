import sys
import csv

from sklearn import preprocessing, cross_validation, metrics, ensemble
from clean import clean_data
from feature_select import select_features


def fit_model(data, target):
    clf = ensemble.AdaBoostClassifier(n_estimators = 100)
    clf.fit(data, target)

    return clf


def main(argv):
    df        = clean_data(argv[0])
    X         = df.drop(['PassengerId', 'Survived'], 1)
    y         = df['Survived']
    selection = select_features(X, y)
    X         = selection.transform(X)
    X         = preprocessing.scale(X)


    data_train, data_test, target_train, target_test = cross_validation.train_test_split(X, y, train_size = 0.8)


    clf     = fit_model(data_train, target_train)
    results = clf.predict(data_test)


    print
    print 'Cross Validation: Test Data'
    print
    print metrics.classification_report(target_test, results)
    print
    print 'Cross Validation: Score = ', cross_validation.cross_val_score(clf, data_test, target_test).mean()
    print


    clf     = fit_model(X, y)
    results = clf.predict(X)


    print
    print 'Cross Validation: Training Data'
    print
    print metrics.classification_report(y, results)
    print
    print 'Cross Validation: Score = ', cross_validation.cross_val_score(clf, X, y).mean()
    print


    df  = clean_data(argv[1])
    X   = df.drop(['PassengerId'], 1)
    X   = selection.transform(X)
    X   = preprocessing.scale(X)
    ids = df['PassengerId'].values


    results = clf.predict(X)


    with open('./prediction_ab.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PassengerId', 'Survived'])
        for i in xrange(len(results)):
            writer.writerow([ids[i], results[i]])


if __name__ == '__main__':
    main(sys.argv[1:])
