import sys

import pandas as pd
import numpy as np

from scipy.stats import mode


def clean_data(file_path):
    df = pd.read_csv(file_path)

    df.Fare = df.Fare.map(lambda x: np.nan if x == 0 else x)

    classmeans = df.pivot_table('Fare', index = 'Pclass', aggfunc = 'mean')
    df.Fare = df[['Fare', 'Pclass']].apply(lambda x: int(classmeans[x['Pclass']]) if pd.isnull(x['Fare']) else x['Fare'], axis = 1)
    # classmedians = df.pivot_table('Fare', index = 'Pclass', aggfunc = 'median')
    # df.Fare = df[['Fare', 'Pclass']].apply(lambda x: classmedians[int(x['Pclass'])] if pd.isnull(x['Fare']) else x['Fare'], axis = 1)

    df.Age = df.Age.fillna(np.mean(df.Age))
    # df.Age = df.Age.fillna(np.median(df.Age))

    df.Sex = df.Sex.apply(lambda x: 0 if x == 'male' else 1)

    modeEmbarked = mode(df.Embarked)[0][0]
    df.Embarked  = df.Embarked.fillna(modeEmbarked)
    embarked = {'S': 2, 'C': 1, 'Q': 0}
    df.Embarked = df.Embarked.apply(lambda x: embarked[x])

    df.Cabin = df.Cabin.fillna('Data Missing')

    return df


def main(argv):
    df = clean_data(argv[0])
    print df.describe()


if __name__ == '__main__':
    main(sys.argv[1:])
