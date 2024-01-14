#import libaray
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier


def predict_disease(sizes):
    df=pd.read_csv('data(1).csv')
    df.dropna(axis=1,inplace=True)


    labelEncoder=LabelEncoder()
    df.iloc[:,1]=labelEncoder.fit_transform(df.iloc[:,1].values)

    X=df.iloc[0:500,22:].values
    Y=df.iloc[0:500,1].values

    X_test=np.array(sizes)
    X_test=X_test.reshape(1,-1)

    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    classifier.fit(X, Y)
    return classifier.predict(X_test)

