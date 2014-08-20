import sys
import csv

from sklearn import preprocessing, cross_validation, metrics, dummy
from clean import clean_data



def fit_dummy(X, y):
    clf = dummy.DummyClassifier()
    clf.fit(X, y)

    return clf



def make_prediction(df_train, df_test, fit_model, output_file):
    X         = df_train.drop(['PassengerId', 'Survived'], 1)
    y         = df_train['Survived']
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
    print metrics.classification_report(y.values, results)
    print
    print 'Cross Validation: Score = ', cross_validation.cross_val_score(clf, X, y).mean()
    print


    X   = df_test.drop(['PassengerId'], 1)
    X   = preprocessing.scale(X)
    ids = df_test['PassengerId'].values


    results = clf.predict(X)


    with open(output_file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PassengerId', 'Survived'])
        for i in xrange(len(results)):
            writer.writerow([ids[i], results[i]])



def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    make_prediction(df_train, df_test, fit_dummy, './output/prediction_dummy.csv')



if __name__ == '__main__':
    main(sys.argv[1:])

