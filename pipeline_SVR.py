
import numpy as np
import pandas as pd
import sys
import pipeline_predicao
import preprocess
import prediction_process
import posProcess

forcastName = 'INSTALACAO'

class PipelinePrediction(object):
	#region Override
	def __init__(self):
		self.hash = None	
					   
	def valid_of_class(self, df, data):
		if(df.shape[0] <= 1):
			return False		
		return True
	
	def preprocess(self, df, data):
		# #ajusta a base de dados para adicionar os valores nulos nos meses referentes que estão faltando
		# df = preprocess.ajuste_base(df)			
		# #Normaliza o data frame por produto		
		# df = preprocess.normalize_dataFrame(df, 'timeSeries', data)		
		# print(df)
		# #Retorna um data frame para o treino e outro para o teste		
		# df_treino, df_teste = preprocess.division_train_test(df)
		df_treino = data
		df_teste = data
		return df_treino, df_teste
		
	def treino_predicao(self, df_treino, df_teste, data):
		# df_teste, df_predicao = prediction_process.prediction(df, data)	
		df_teste = data 
		df_predicao = data

		return df_teste, df_predicao
					
	def postprocess(self, df_teste, df_predicao, data):
		
		
		# posProcess.metrica(df, data)
			
		return data

	def finish(self, start_ref, end_ref):
		print()