import os
import pandas as pd
import numpy as np

def get_base(path):
	df = pd.read_csv(r''+ path, sep=";")   #caminho
	return df

def juntar_calendario_preco(df_cal, df_preco):

	#result = pd.merge(df_cal, df_preco, on='wm_yr_wk')
	result = df_cal.join(df_preco.set_index('wm_yr_wk'), on='wm_yr_wk')
	
	#result.to_csv("bases/base_cal_preco.csv", index= False)   # exportar para csv
	return result

def div_produtos(df_produtos, df_cal_preco, path_out):
	#percorre cada linha do data frame que é referente a um produto	
	dfCopy = df_produtos.copy()
	produtos_ID = df_produtos["id"]
	
	dfCopy = dfCopy.drop(["state_id"], axis=1)
	dfCopy = dfCopy.drop(["store_id"], axis=1)
	dfCopy = dfCopy.drop(["cat_id"], axis=1)
	dfCopy = dfCopy.drop(["dept_id"], axis=1)
	dfCopy = dfCopy.drop(["item_id"], axis=1)

	time_series = dfCopy.values[:,1:].astype(np.float)

	for i, x in enumerate(time_series):
		nameDoc = produtos_ID[i]	
		item_id = df_produtos.iloc[i]['item_id']	
		new_df = pd.DataFrame(x, columns=["Qtd_dia"])
		#new_df["item_id"] = item_id
		#aux = dfCopy.columns[1:]
		new_df["d"] = dfCopy.columns[1:]
				
		df_Cal_prod = df_cal_preco.loc[(df_cal_preco["item_id"] == item_id)]
		
		#df_final = pd.merge(new_df, df_Cal_prod, on='d')
		df_final = new_df.join(df_Cal_prod.set_index('d'), on='d')

		#path_out = "bases/base_dividida"
		if not os.path.exists(path_out):
			os.makedirs(path_out)
		
		df_final.to_csv(path_out + "/"+ nameDoc + ".csv", index= False)   # exportar para csv
		
		print(nameDoc)
									

def juntar(path_calendario, path_preco, path_produtos, path_out):

	# path_calendario = "bases/calendar.csv"	#inicialização dos parâmetros
	# path_preco = "bases/sell_prices.csv"	#inicialização dos parâmetros
	# path_produtos = "bases/sales_train_validation.csv"	#inicialização dos parâmetros

	df_cal = get_base(path_calendario)		#Pega o base no caminho informado	
	df_preco = get_base(path_preco)
	df_produtos = get_base(path_produtos)

	#Juntar dataset de calendário com o dataset dos preços 
	df = juntar_calendario_preco(df_cal, df_preco)

	#path = "bases/base_cal_preco.csv"
	#df = pd.read_csv(r''+path, sep=",")   #caminho

	#Juntar dataset de calendário com o dataset dos preços 
	div_produtos(df_produtos, df, path_out)
	
	print("End")
	