
# -*- coding: utf-8 -*-

""" 
Implementação da classe abstrata para uso no módulo de predição do projeto de Ciência de Dados
    
Esta classe tras as assinaturas de funções necessárias para a execução do pipeline de predição.
Para o funcionamento correto, as assinaturas das funções nao devem ser alteradas. Caso seu código precise 
passar algum dado para as etapas futuras, utilize o  dicionário *param* para armazenar os dados e passar 
adiante. 

Versão do Python em que foi testada: 3.7
Sistema operacional: Windows de 64 bits

Instruções de uso:
Crie um arquivo para a nova classe.
Utilize:

    class Nome_da_Classe(Pipeline):

para realizar a herança.   
Redefina os métodos. 
"""
from abc import ABCMeta, abstractmethod

__author__ = "Mayara Gomes"
__copyright__ = ""
__credits__ = "Equipe Anderson, Mayara, Nelia"
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Mayara Gomes"
__email__ = "mayaragomys@gmail.com"
__status__ = "Em desenvolvimento, etapa de testes"

class PipelinePrediction(object):
    __metaclass__ = ABCMeta
    """Classe base para pipeline do núcleo de predição"""
    
    @abstractmethod
    def valid_of_class(self, df, data):
        """
        Descrição:
            Essa função deve implementar o método que indica se um dataframe de uma classe pode ser processado.
        Parâmetros:
            df - dataframe contendo os dados da loja.
            data - dicionário que contém parametros personalizados, deve ser utilizado para fornecer dados para 
                as etapas posteriores ou receber dados das etapas anteriores. Esse atributo deve ser controlado 
                pelo programador das classes filhas dessa classe.
        Retorno:
            O retorno deve ser do tipo boolean, indicando a possibilidade ou não de processamento.
        """
        pass

    @abstractmethod
    def preprocess(self, df, data):
        """
        Descrição:
            Essa função deve implementar o método que realiza o preprocessamento da base.
        Parâmetros:
            df - dataframe contendo os dados da base.
            data - dicionário que contém parametros personalizados, deve ser utilizado para fornecer dados 
                para as etapas posteriores ou receber dados das etapas anteriores. Esse atributo deve ser 
                controlado pelo programador das classes filhas dessa classe.
        Retorno:
            O retorno deve ser dois dataframes: um contendo os dados para o treinamento, um contendo os dados
            para o teste.
        """
        pass

    @abstractmethod
    def treino_predicao(self, df_treino, df_teste, data):
        """
        Descrição:
            Essa função deve implementar o método responsável por treinar e prever os dados com a técnica 
            escolhida.
        Parâmetros:
            df_treino - dataframe contendo os dados da loja para o treinamento.
            df_teste - dataframe contendo os dados da loja para a predição.
            data - dicionário que contém parametros personalizados, deve ser utilizado para fornecer dados 
                para as etapas posteriores ou receber dados das etapas anteriores. Esse atributo deve ser 
                controlado pelo programador das classes filhas dessa classe.
        Retorno:
            Esse método deve retornar os dados da predição e do teste."""
        pass

    
    @abstractmethod
    def postprocess(self, df_teste, df_predicao, data):
        """
        Descrição:
            Essa função deve implementar o método responsável por realizar o pós processamento dos dados, 
            quando necessário, como por exemplo, desnormalizar os dados que foram normalizados no 
            preprocessamento e também calcular as métricas.
        Parâmetros:
            df_teste - dataframe contendo os dados da classe.
            df_predicao - dataframe contendo os dados de clientes com séries zeradas.
            data - dicionário que contém parametros personalizados, deve ser utilizado para fornecer dados para as etapas posteriores ou receber dados das etapas anteriores. Esse atributo deve ser controlado pelo programador das classes filhas dessa classe.
        Retorno:
            
            """     
        pass

   
    @abstractmethod
    def finish(self):
        """
        Descrição:
            Essa função deve implementar o método responsável executar as rotinas necessárias após executar toda a base.
        Parâmetros:
            mounth_ref - o mês referencia processado.
        Retorno:
            Esse método não deve retornar nada."""
        pass