
import numpy as np
import pandas as pd
import sys
import pipeline_Predicao
import pre_Process
import prediction_Process
import pos_Process

forcastName = 'INSTALACAO'

class PipelinePrediction(object):
	#region Override
	def __init__(self):
		self.hash = None	
					   
	def valid_of_class(self, df, data):
		if(df.shape[0] <= 1):
			return False		
		return True
	
	def pre_Process(self, df, data):
		# #ajusta a base de dados para adicionar os valores nulos nos meses referentes que estão faltando
		x, y = prediction_Process.division_x_y(df)		
				
		return x_treino, x_teste, y_treino, y_teste
		
	def predicao(self, x, y, data):
		x_treino, x_teste, y_treino, y_teste = predicao.division_train_test (x, y, por)
		y_test, predict_test = prediction_Process.SVR_Prediction(x_treino, x_teste, y_treino, y_teste)
		
		#return y_test, predict_test
		return data, data
					
	def pos_Process(self, y_test, predict_test, data):
			
		#posProcess.metricas(df, data)
		print()
					

	def finish(self, start_ref, end_ref):
		print()