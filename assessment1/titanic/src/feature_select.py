import sys
import csv

from sklearn import feature_selection, svm
from clean import clean_data


def select_features(X, y):
    selection = feature_selection.SelectKBest(score_func = feature_selection.chi2, k = 'all')
    selection = selection.fit(X, y)

    print
    print 'Chi-squared:'
    print
    for i in range(len(X.columns)):
        print '%10s: score = %8.2f, pvalue = %8.2f' % (X.columns[i], selection.scores_[i], selection.pvalues_[i])
    print

    selection = feature_selection.SelectKBest(score_func = feature_selection.f_regression, k = 'all')
    selection = selection.fit(X, y)

    print
    print 'Univariate Linear Regression:'
    print
    for i in range(len(X.columns)):
        print '%10s: score = %8.2f, pvalue = %8.2f' % (X.columns[i], selection.scores_[i], selection.pvalues_[i])
    print

    selection = feature_selection.RFE(svm.LinearSVC(C = 5))
    selection = selection.fit(X, y)

    print
    for i in range(len(X.columns)):
        print '%10s: support = %8.2f, ranking = %8.2f' % (X.columns[i], selection.support_[i], selection.ranking_[i])
    print

    return selection


def main(argv):
    df = clean_data(argv[0])

    X  = df.drop(['PassengerId', 'Survived'], 1)
    y  = df['Survived']

    select_features(X, y)



if __name__ == '__main__':
    main(sys.argv[1:])
