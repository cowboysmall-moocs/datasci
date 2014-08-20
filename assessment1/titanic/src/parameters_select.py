import sys

from sklearn import preprocessing, grid_search, svm
from clean import clean_data


def select_parameters(df_train, df_test):
    X = preprocessing.scale(df_train.drop(['PassengerId', 'Survived'], 1))
    y = df_train['Survived']

    parameters_grid = [
        {'C': [1, 3, 5, 10, 25, 50, 100, 250, 500], 'kernel': ['rbf'], 'gamma': [0.5, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025, 0.001, 0.0001]},
        {'C': [1, 3, 5, 10, 25, 50, 100, 250, 500], 'kernel': ['sigmoid'], 'gamma': [0.5, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025, 0.001, 0.0001]},
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
