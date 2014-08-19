import sys

import pandas as pd
import numpy as np

from scipy.stats import mode


def clean_data(file_path):
    df = pd.read_csv(file_path)

    classMedians = df.pivot_table('Fare', cols = 'Pclass', aggfunc = 'median')
    modeEmbarked = mode(df.Embarked)[0][0]
    embarked     = {'S': 0, 'C': 1, 'Q': 2}

    df.Fare     = df[['Fare', 'Pclass']].apply(lambda x: classMedians[int(x['Pclass'])] if pd.isnull(x['Fare']) else x['Fare'], axis = 1)
    df.Age      = df.Age.fillna(np.median(df.Age))
    df.Sex      = df.Sex.apply(lambda x: 0 if x == 'male' else 1)
    df.Embarked = df.Embarked.fillna(modeEmbarked)
    df.Embarked = df.Embarked.apply(lambda x: embarked[x])

    return df.drop(['Name', 'Ticket', 'Cabin'], 1)


def main(argv):
    df = clean_data(argv[0])
    print df.describe()


if __name__ == '__main__':
    main(sys.argv[1:])
