import sys

from sklearn import preprocessing, grid_search, svm
from clean import clean_data


def select_parameters(df_train, df_test):
    X = preprocessing.scale(df_train.drop(['PassengerId', 'Survived'], 1))
    y = df_train['Survived']

    parameters_grid = [
        {
            'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            'kernel': ['rbf'], 
            'gamma': [0.01, 0.02, 0.03, 0.4, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
        },
    ]

    clf = svm.SVC()
    gs  = grid_search.GridSearchCV(clf, parameters_grid)
    gs.fit(X, y)

    X = preprocessing.scale(df_test.drop(['PassengerId'], 1))
    gs.predict(X)

    best  = 0.0
    score = None
    for grid_score in gs.grid_scores_:
        if best < grid_score[1]:
            best  = grid_score[1]
            score = grid_score[0]

    print
    print 'Best Grid Score:'
    print
    print '%s: C = %3s, gamma = %0.4f [mean = %0.8f]' % (score['kernel'], score['C'], score['gamma'], best)
    print
    print 'Best Estimator:'
    print
    print gs.best_estimator_
    print



def main(argv):
    df_train = clean_data(argv[0])
    df_test  = clean_data(argv[1])

    select_parameters(df_train, df_test)



if __name__ == '__main__':
    main(sys.argv[1:])
