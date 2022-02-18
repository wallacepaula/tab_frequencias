# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:45:06 2021

@author: walla
"""

import pandas as pd

# Importa dados da tabela CSV com delimitador ";"
dados = pd.read_csv("C:/Users/walla/Desktop/mba/fundamentos-estatistica/ex-1-tabela-frequencias.csv", sep=";")

def tab_frequencias(data, col_agg, col_count, n_decimals):
    """
    Gera tabela com Frequência Absoluta, Relativa, Absoluta Acumulada e Relativa Acumulada

    Parameters
    ----------
    data : DataFrame
        dados
    col_agg : str
        Nome da coluna que quer agrupar
    col_count : str
        Nome da coluna em que será realizada a contagem de observações
    n_decimals: int
        Número de casas decimais

    Returns
    -------
    DataFrame

    """

    # Agrupa observações pelo país de origem usando groupby e conta 
    # usando método count()
    #pais_origem = dados.groupby(by="País de Origem").count()
    data = data.groupby(by=col_agg).count()
    
    # Cria a tabela de frequência
    tab_frequencias = pd.DataFrame()
    
    # Cria a tabela de frequência absoluta
    tab_frequencias.loc[:,'Frequência Absoluta'] = data[col_count]
    
    # Cria a tabela de frequência relativa
    tab_frequencias.loc[:, 'Frequência Relativa (%)'] = (tab_frequencias['Frequência Absoluta']
                                                     /sum(tab_frequencias['Frequência Absoluta'])).round(n_decimals)*100
    
    # Cria a tabela de frequência absoluta acumulada
    tab_frequencias.loc[:, 'Frequência Absoluta Acumulada'] = tab_frequencias['Frequência Absoluta'].cumsum()
    
    # Cria a tabela de frequência relativa acumulada
    tab_frequencias.loc[:, 'Frequência Relativa Acumulada (%)'] = tab_frequencias['Frequência Relativa (%)'].cumsum()
    
    # Retona tabela
    return tab_frequencias

tab_frequencias = tab_frequencias(dados, "País de Origem", 'Indivíduo', 3)

tab_frequencias.to_excel('Tabela de Frequências.xlsx')

