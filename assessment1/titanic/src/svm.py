import sys
import csv

from sklearn import preprocessing, feature_selection, grid_search, cross_validation, metrics, svm
from clean import clean_data
from feature_select import select_features


def fit_model(data, target):
    # clf = svm.SVC(gamma = 0.25, C = 1)

    parameters_grid = [
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['linear']},
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['rbf'], 'gamma': [1, 0.5, 0.25, 0.1, 0.01, 0.001, 0.0001]},
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['poly'], 'gamma': [1, 0.5, 0.25, 0.1, 0.01, 0.001, 0.0001], 'degree': [1, 2, 3]},
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['sigmoid'], 'gamma': [1, 0.5, 0.25, 0.1, 0.01, 0.001, 0.0001]},
    ]
    clf = grid_search.GridSearchCV(svm.SVC(), parameters_grid)
    clf.fit(data, target)

    print clf.get_params()

    return clf


def main(argv):
    df        = clean_data(argv[0])
    X         = df.drop(['PassengerId', 'Survived'], 1)
    y         = df['Survived']
    # selection = select_features(X, y)
    # X         = selection.transform(X)
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


    df  = clean_data(argv[1])
    X   = df.drop(['PassengerId'], 1)
    # X   = selection.transform(X)
    X   = preprocessing.scale(X)
    ids = df['PassengerId'].values


    results = clf.predict(X)


    with open('./output/prediction_svm.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PassengerId', 'Survived'])
        for i in xrange(len(results)):
            writer.writerow([ids[i], results[i]])


if __name__ == '__main__':
    main(sys.argv[1:])



# clf = svm.NuSVC(gamma = 0.25, nu = 0.5)
# clf = svm.SVC(gamma = 0.25, C = 5., class_weight = 'auto')
# clf = svm.SVC(kernel = 'poly', gamma = 0.25, degree = 2, C = 5.)
# clf = svm.SVC(kernel = 'rbf', gamma = 0.25, C = 5.)
# clf = svm.SVC(kernel = 'rbf', gamma = 0.01, C = 100)
# clf = svm.SVC(kernel = 'sigmoid', gamma = 0.25, C = 5000.)
# clf = svm.LinearSVC(C = 5)
