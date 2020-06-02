# receber dataset
# aplicar k-means, onde k= 4 e int= 'k-means++'
# dividir os individuos dos clusters resultantes em arquivos csv

import numpy as np
import pandas as pd
#import autoSVR as svr
#import xmeansClass

def division_train_test (x, y, por):

    index = int(X.shape[0]*por)
    X_train = x[:index,:]
    X_test = x[index:,:]
    y_train = y[:index]
    y_test = y[index:]

    print("X_train", X_train.shape)
    print("X_test", X_test.shape)
    print("y_train", y_train.shape)
    print("y_test", y_test.shape)

    return X_train, X_test, y_train, y_test


def SVR_Prediction(x_treino, x_teste, y_treino, y_teste):
    ######################################################
    # TREINAMENTO DO MODELO
    ######################################################

    # model = svr.gridSVR()
    # model.fit(X_train, y_train.reshape(-1,), True)


    # print("OBTENDO PREDICTS...")
    # #OBTENDO PREDICTS
    # trainPredictNorm = model.predict(X_train)
    # testPredictNorm = model.predict(X_test)

    return 