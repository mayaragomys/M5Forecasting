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


def get_base(path):
	df = pd.read_csv(r''+path, sep=";")   #caminho
	return df

def run(df_city, pipe, end_ref):
	"""
		Descrição:
			Função que executa o módulo.
		Parâmetros:
			base - lista que contem o id de todos os produtos que serão processados.
		Retorno:
			Nenhum
		"""
	#percorre cada linha do data frame que é referente a um produto
	for i in df_city.index:
		df_produto = df_city.loc[i]
		data = {}	#inicialização do dicionário de parametros personalizados  		           
		print(df_produto)  
		if(pipe.valid_of_class(df_produto, data)):			
			df_treino, df_teste = pipe.preprocess(df, data)                    
			df_teste, df_predicao = pipe.treino_predicao(df_treino, df_teste, data)
			data = pipe.postprocess(df_teste, df_predicao, data)
					

if __name__== "__main__":

	end_ref, path = load_params()	#inicialização dos parâmetros
	
	base = get_base(path)		#Pega o base no caminho informado
	ini = time.time()	

	name_city = base['state_id'].unique()
	for cc in name_city:		
		run(base, pipe, end_ref)

	#pipe.finish(start_ref, end_ref)

	fim = time.time()
	timeStamp = fim-ini
	print("Tempo total: ", timeStamp) 