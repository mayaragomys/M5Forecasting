import pandas as pd
import numpy as np
import math
import json

def metricas(y_test, predict_test):
    ###########################################################################
    # METRICAS
    ###########################################################################

    score = s.Score(['mape', 'mae', 'mse', 'rmse', 'r2'])
    # metrics = score.get_scores(y_test, testPredict)
    metrics_norm = score.get_scores(y_test, predict_test)
    #print("Métricas: ", metrics)
    print("Métricas normalizadas: ", metrics_norm)

    # with open("results/maioba_consumo/" + '.json', 'w') as outfile:
    #     json.dump(metrics, outfile)

    with open('_norm.json', 'w') as outfile:
        json.dump(metrics_norm, outfile)