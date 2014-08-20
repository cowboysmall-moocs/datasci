import sys

import pandas as pd
import numpy as np

from scipy.stats import mode


def clean_data(file_path):
    df = pd.read_csv(file_path)

    pclass_medians = df.pivot_table('Fare', cols = 'Pclass', aggfunc = 'median')
    embarked_mode  = mode(df.Embarked)[0][0]
    embarked       = {'S': 1, 'C': 2, 'Q': 3}
    titles         = {'Master': 1, 'Miss': 2, 'Mr': 3, 'Ms': 4, 'Sir': 5, 'Lady': 6}



    df.Fare     = df[['Fare', 'Pclass']].apply(lambda x: pclass_medians[int(x['Pclass'])] if pd.isnull(x['Fare']) else x['Fare'], axis = 1)

    df.Age      = df.Age.fillna(np.median(df.Age))

    df.Sex      = df.Sex.apply(lambda x: 0 if x == 'male' else 1)

    df.Embarked = df.Embarked.fillna(embarked_mode)
    df.Embarked = df.Embarked.apply(lambda x: embarked[x])

    df['Title'] = df.Name.apply(lambda x: x.split(',')[1].split('.')[0].strip())
    df.Title    = df.Title.apply(lambda x: 'Miss' if x in ['Mlle'] else x)
    df.Title    = df.Title.apply(lambda x: 'Ms'   if x in ['Mme', 'Mrs'] else x)
    df.Title    = df.Title.apply(lambda x: 'Sir'  if x in ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir'] else x)
    df.Title    = df.Title.apply(lambda x: 'Lady' if x in ['Dona', 'Lady', 'the Countess', 'Jonkheer'] else x)
    df.Title    = df.Title.apply(lambda x: titles[x])


    return df.drop(['Name', 'Ticket', 'Cabin'], 1)


def main(argv):
    df = clean_data(argv[0])
    print df.describe()


if __name__ == '__main__':
    main(sys.argv[1:])
