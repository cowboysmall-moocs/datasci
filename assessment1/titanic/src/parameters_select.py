import sys

from sklearn import grid_search, svm
from clean import clean_data


def select_parameters(X, y):
    parameters_grid = [
        {'C': [1, 3, 5, 10, 25, 50, 100, 250, 500], 'kernel': ['rbf'], 'gamma': [0.5, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025, 0.001, 0.0001]},
        {'C': [1, 3, 5, 10, 25, 50, 100, 250, 500], 'kernel': ['sigmoid'], 'gamma': [0.5, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025, 0.001, 0.0001]},
    ]
    clf = svm.SVC()
    gs  = grid_search.GridSearchCV(clf, parameters_grid)
    gs.fit(X, y)

    best  = 0.0
    score = None
    for grid_score in gs.grid_scores_:
        if best < grid_score[1]:
            best  = grid_score[1]
            score = grid_score[0]

    print
    print 'Best Grid Score:'
    print
    print '%s: C = %5s, gamma = %2.4f [mean = %2.6f]' % (score['kernel'], score['C'], score['gamma'], best)
    print
    print 'Best Estimator:'
    print
    print gs.best_estimator_
    print



def main(argv):
    df = clean_data(argv[0])

    X  = df.drop(['PassengerId', 'Survived'], 1)
    y  = df['Survived']

    select_parameters(X, y)



if __name__ == '__main__':
    main(sys.argv[1:])
