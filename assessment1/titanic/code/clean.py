import sys
import pandas
import numpy
import statsmodels.api as sm


from predict import predict
from patsy import dmatrices
from pandas import Series, DataFrame
from sklearn import svm




def main(argv):
    train = pandas.read_csv('./data/train.csv')
    test  = pandas.read_csv('./data/test.csv')

    # print train

    # train = train.drop(['Ticket', 'Cabin'], axis = 1)
    # train = train.dropna()

    # results = {}

    # formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp  + C(Embarked)'
    # y, X = dmatrices(formula, data = train, return_type = 'dataframe')
    # result = sm.Logit(y, X).fit()

    # results['Logit'] = [result, formula]

    # test['Survived'] = 0

    # compared_resuts  = Series(predict(test, results, 'Logit'))     
    # compared_resuts.to_csv('./output/logit.csv')
    # print compared_resuts



    # print train.head()
    # print test.head()


    # data1 = train.drop('Survived', 1)
    # data1 = data1.drop('Pclass', 1)
    # data1 = data1.drop('Name', 1)
    # data1 = data1.drop('Sex', 1)
    # data1 = data1.drop('Age', 1)
    # data1 = data1.drop('SibSp', 1)
    # data1 = data1.drop('Parch', 1)
    # data1 = data1.drop('Ticket', 1)
    # # data1 = data1.drop('Fare', 1)
    # data1 = data1.drop('Cabin', 1)
    # data1 = data1.drop('Embarked', 1)
    # data1 = data1.fillna(data1.mean())


    # print train['Survived']

    # clf = svm.SVC(gamma = 0.001, C = 100.)
    # clf.fit(data1, train['Survived'])


    # data2 = test.drop('Name', 1)
    # data2 = data2.drop('Pclass', 1)
    # data2 = data2.drop('Sex', 1)
    # data2 = data2.drop('Age', 1)
    # data2 = data2.drop('SibSp', 1)
    # data2 = data2.drop('Parch', 1)
    # data2 = data2.drop('Ticket', 1)
    # # data2 = data2.drop('Fare', 1)
    # data2 = data2.drop('Cabin', 1)
    # data2 = data2.drop('Embarked', 1)
    # data2 = data2.fillna(data2.mean())


    # count = 0
    # for index, row in data2.iterrows():
    #     if result.predict(row)[0] == 1:
    #         count += 1

    # print
    # print '   total -> %s' % (len(data2))
    # print 'survived -> %s' % (count)
    # print





if __name__ == '__main__':
    main(sys.argv[1:])