import sys
import csv

from sklearn import preprocessing, metrics, svm
from clean import clean_data


def fit_model(data, target):
    clf = svm.SVC(gamma = 0.1, C = 1.)
    # clf = svm.SVC(kernel = 'poly', gamma = 0.01, degree = 2, C = 50.)
    # clf = svm.SVC(kernel = 'rbf', gamma = 0.01, C = 5.)
    # clf = svm.SVC(kernel = 'sigmoid', gamma = 0.01, C = 5.)
    # clf = svm.LinearSVC(C = 5)
    clf.fit(data, target)

    return clf


def evaluate(clf, results, target, heading):
    positive = 0
    negative = 0

    for i in xrange(len(results)):
        if results[i] == target[i]:
            positive += 1
        else:
            negative += 1

    print
    print '%s: ' % (heading)
    print 'Positive: %s, Negative: %s, Perentage: %s' % (positive, negative, float(positive) / len(results))
    print
    print metrics.classification_report(target, results)
    print


def main(argv):
    df = clean_data(argv[0])

    target = df['Survived'].values
    data   = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Fare', 'Survived'], 1).values
    data   = preprocessing.scale(data)

    total       = len(data)
    train_count = int(total * 0.6)
    cv_count    = int(total * 0.8)



    clf = fit_model(data[:train_count], target[:train_count])

    results = clf.predict(data[train_count:cv_count])
    evaluate(clf, results, target[train_count:cv_count], 'Cross Validation')

    results = clf.predict(data[cv_count:])
    evaluate(clf, results, target[cv_count:], 'Test')



    clf = fit_model(data, target)

    df2  = clean_data(argv[1])
    ids  = df2['PassengerId'].values
    data = df2.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Fare'], 1).values
    data = preprocessing.scale(data)

    results = clf.predict(data)



    with open('./prediction_svm.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PassengerId', 'Survived'])
        for i in xrange(len(results)):
            writer.writerow([ids[i], results[i]])


if __name__ == '__main__':
    main(sys.argv[1:])
