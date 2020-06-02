# remover clientes com sequencia inteiramente 0
# remover clientes com 9 ou menos meses de leitura
# executar k-means
# dividir em clientes por perfil
import numpy as np
import pandas as pd
import os
import math

 #Variáveis para definir colunas de treino e teste
forcast_X = 'Qtd_dia'
forcast_Y = 'TARGET'

def division_x_y(df):
    # Nenhum historico eh utilizado, apenas o valor atual,
    # mas pode configurar essa variavel para adicionar outras N medicoes
    look_back = 1
   
    # Cria colunas novas para o tamanho de look_back
    for i in range(look_back):
        df[forcast_x + "_" + str(i+1)] = df[forcast_X].shift(-(i+1))

    # cria a coluna de target
    df[forcast_Y] = df[forcast_X].shift(-look_back-1)
    df.dropna(inplace=True)

    x = np.array(df)
    y = np.array(df[forcast_Y]).reshape(-1, 1)

    return x, y


def limpeza_dos_dados(df):

    #Retirando atributos dispensáveis
    df = df.drop(["weekday"], axis=1)

def add_atributos():
    print()

def look_back():
    print()

#def normalizacao():