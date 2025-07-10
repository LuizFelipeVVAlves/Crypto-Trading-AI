import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from utils import calculaFeaturesMediaMovel
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import StandardScaler


def TratamentoDeDados() -> pd.DataFrame:

    # Carrega os dados do arquivo CSV
    btc_data = pd.read_csv("C:/Users/Luiz Felipe/OneDrive/Documentos/CryptoTradingAI/btc2018-2025.csv")

    #Removo colunas desnecessárias
    btc_data.drop(columns=['Volume', 'Quote asset volume', 'Number of trades', 'Close time', 'Taker buy base asset volume',
                           'Taker buy quote asset volume', 'Ignore'], inplace=True)

    # Renomeia a coluna 'Open time' para 'Date' para fins de visualização
    btc_data.rename(columns={'Open time': 'Date'}, inplace=True)

    # Converte a coluna 'Date' para o tipo datetime
    btc_data['Date'] = pd.to_datetime(btc_data['Date'])

    # Considero apenas os dados do horário de fechamento diário (18:00)
    btc_data = btc_data[btc_data['Date'].dt.time == pd.to_datetime('18:00:00').time()]

    # Converte a coluna 'Date' para o tipo date (sem hora)
    btc_data['Date'] = btc_data['Date'].dt.date

    # Ordena os dados pela coluna 'Date'
    btc_data.sort_values('Date', inplace=True)

    # Define as janelas de média móvel
    janelas = [3,7,15]

    # Calcula features
    btc_data = calculaFeaturesMediaMovel(btc_data, janelas)


    btc_data['open-close']  = btc_data['Open'] - btc_data['Close']
    btc_data['low-high']  = btc_data['Low'] - btc_data['High']

    btc_data.dropna(inplace=True)

    btc_data['Target'] = np.where(btc_data['Close'].shift(-1) > btc_data['Close'], 1, 0)

    btc_data['Close'] = btc_data['Close'].shift(-1)

    btc_data.drop(columns=['Date'], inplace=True)

    btc_data.dropna(inplace=True)

    corr_matrix = btc_data.corr()
 
    plt.figure(figsize=(12, 10)) # Define um bom tamanho para a figura

    sns.heatmap(
        corr_matrix, 
        annot=True,      # Escreve os valores numéricos em cada célula
        cmap='coolwarm', # Esquema de cores: vermelho para positivo, azul para negativo
        fmt=".2f"        # Formata os números para terem 2 casas decimais
    )

    plt.title('Matriz de Correlação das Features e do Alvo', fontsize=16)
    plt.show()

    # Separa as features e o alvo removendo features redundantes 
    features = btc_data.drop(columns=['Target', 'Date', 'MMS_7', 'MMS_3', 'Close', 'Open', 'High', 'Low'])
    target = btc_data['Target']
    
    return features, target, btc_data
