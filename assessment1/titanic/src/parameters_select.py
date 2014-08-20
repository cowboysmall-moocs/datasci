import sys

from sklearn import grid_search, svm
from clean import clean_data


def select_parameters(X, y):
    parameters_grid = [
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['linear']},
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['rbf'], 'gamma': [1, 0.5, 0.25, 0.1, 0.01, 0.001, 0.0001]},
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['poly'], 'gamma': [1, 0.5, 0.25, 0.1, 0.01, 0.001, 0.0001], 'degree': [1, 2, 3]},
        {'C': [1, 5, 10, 50, 100, 500, 1000], 'kernel': ['sigmoid'], 'gamma': [1, 0.5, 0.25, 0.1, 0.01, 0.001, 0.0001]},
    ]
    clf = svm.SVC()
    gs  = grid_search.GridSearchCV(svm.SVC(), parameters_grid)
    gs.fit(X, y)

    print
    print clf.get_params()
    print

    print
    print gs.get_params()
    print



def main(argv):
    df = clean_data(argv[0])

    X  = df.drop(['PassengerId', 'Survived'], 1)
    y  = df['Survived']

    select_parameters(X, y)



if __name__ == '__main__':
    main(sys.argv[1:])
