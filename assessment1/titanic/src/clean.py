import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import mode


def bucket_ages(age):
    if 0 < age <= 18:
        return 1
    elif 18 < age <= 45:
        return 2
    elif 45 < age <= 65:
        return 3
    else:
        return 4


def bucket_fares(fare):
    if fare <= 9:
        return 3
    elif 10 <= fare <= 30:
        return 2
    else:
        return 1


def bucket_family_size(size):
    if size <= 3:
        return 1
    else:
        return 2


def clean_data(file_path):
    df = pd.read_csv(file_path)

    pclass_medians = df.pivot_table('Fare', cols = 'Pclass', aggfunc = 'median')
    embarked_mode  = mode(df.Embarked)[0][0]
    embarked       = {'S': 1, 'C': 2, 'Q': 3}
    titles         = {'Master': 1, 'Miss': 2, 'Mr': 3, 'Ms': 4, 'Sir': 5, 'Lady': 6}


    df.Fare          = df[['Fare', 'Pclass']].apply(lambda x: pclass_medians[int(x['Pclass'])] if pd.isnull(x['Fare']) else x['Fare'], axis = 1)
    df['FareRange']  = df.Fare.apply(lambda x: bucket_fares(x)).astype(float)

    df.Age           = df.Age.fillna(np.median(df.Age))
    df['AgeRange']   = df.Age.apply(lambda x: bucket_ages(x)).astype(float)

    df['Gender']     = df.Sex.apply(lambda x: 0 if x == 'male' else 1).astype(float)

    df['FamilySize'] = df[['SibSp', 'Parch']].apply(lambda x: int(x['SibSp']) + int(x['Parch']) + 1, axis = 1)
    df['FamilySize'] = df.FamilySize.apply(lambda x: bucket_family_size(x))

    df.Embarked      = df.Embarked.fillna(embarked_mode)
    df['Port']       = df.Embarked.apply(lambda x: embarked[x]).astype(float)

    df['Title']      = df.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())
    df.Title         = df.Title.apply(lambda x: 'Miss' if x in ['Mlle'] else x)
    df.Title         = df.Title.apply(lambda x: 'Ms'   if x in ['Mme', 'Mrs'] else x)
    df.Title         = df.Title.apply(lambda x: 'Sir'  if x in ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer'] else x)
    df.Title         = df.Title.apply(lambda x: 'Lady' if x in ['Dona', 'Lady', 'the Countess'] else x)
    df.Title         = df.Title.apply(lambda x: titles[x])

    return df.drop(['Name', 'Ticket', 'Cabin', 'Fare', 'Age', 'Sex', 'Embarked'], 1)


def main(argv):
    df = clean_data(argv[0])
    print df.describe()


if __name__ == '__main__':
    main(sys.argv[1:])
