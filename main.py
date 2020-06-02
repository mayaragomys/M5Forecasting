# -*- coding: utf-8 -*-
""" 
Implementação do módulo de predição do projeto de Ciência de Dados.
Este módulo executará as etapas necessárias para a predição de preços dos produtos de uma 
empresa em várias cidades. A implementação deve ser dada pela sobre carga da classe pipeline.
Versão do Python em que foi testada: 3.7
Sistema operacional: Windows de 64 bits
Para executar esse módulo, o arquivo params.sco deve ser configurado com as opções de execução.
"""

import os
import pandas as pd
import numpy as np
import pipeline_SVR as method	
import time
import glob
import juntar_bases
from os.path import basename
pipe = method.PipelinePrediction()

def load_params():
	"""
		Descrição:
			Função que carrega os parametos de execução.
		Parâmetros:
			Nenhum
		Retorno:
			Retorna os paramentros
		"""
	param_file = open('params.sco', 'r')
	lines = param_file.readlines()
	for l in lines:
		s = l.split(':', 1)		
		if(s[0] == 'end_ref'):
			end_ref = int(s[1])
		elif(s[0] == 'path'):
			path = s[1].replace('\n', '').replace(' ', '') 
			
	return end_ref, path

def run(df_produto, pipe, end_ref):
	"""
		Descrição:
			Função que executa o módulo.
		Parâmetros:
			df_produto - dados do produto a ser processado.
		Retorno:
			Nenhum
		"""
	data = {}	#inicialização do dicionário de parametros personalizados  	 
	if(pipe.valid_of_class(df_produto, data)):			
		df_treino, df_teste = pipe.pre_Process(df, data)                    
		y_test, predict_test = pipe.predicao(df_treino, df_teste, data)
		pipe.pos_Process(y_test, predict_test, data)
		
					

if __name__== "__main__":
	
	#end_ref, path_out = load_params()	#inicialização dos parâmetros
	path_calendario = "dataset/calendar.csv"	#Caminho da base de calendário
	path_preco = "dataset/sell_prices.csv"	#Caminho da base dos preços
	path_produtos = "dataset/sales_train_validation.csv"	#Caminho da base dos produtos com a quantidade de venda por dia
	path_out = "dataset/base_dividida"	#Caminho para salvar a base dividida

	# Junta as três bases e separa as informações de cada produto em um csv
	#juntar_bases.juntar(path_calendario, path_preco, path_produtos, path_out)	
	
	#Processa cada produto individualmente
	for path_base in glob.glob(path_out+"/*"):
		df= pd.read_csv(r''+ path_base, engine='python') # lendo csv
		#print(df)
		run(df, pipe, "")
					
	print("End! ") 