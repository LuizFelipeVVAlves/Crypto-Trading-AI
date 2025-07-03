import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from TecnicaClassica.utils import calculoMediaMovel

import pandas as pd

def showGrafico(btc_x, btc_y, btc_y2) -> None:
    
    plt.figure(figsize=(10, 6))
    plt.plot(btc_x,btc_y, color='blue', alpha=0.5, label='Média Móvel')
    plt.plot(btc_x,btc_y2, color='orange', alpha=0.5, label='Preço de Fechamento')
    plt.xlabel(f'{btc_x.name}')
    plt.ylabel(f'{btc_y.name}')
    plt.title(f'{btc_y.name} x {btc_x.name}')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout() 
    plt.show()


def showGraficoComparacaoMediasMoveis(MMS7, MMS30, MMS50, Datas):
    plt.figure(figsize=(10, 6))
    plt.plot(Datas, MMS7, color='blue', alpha=0.5, label='MMS 7')
    plt.plot(Datas, MMS30, color='orange', alpha=0.5, label='MMS 30')
    plt.plot(Datas, MMS50, color='green', alpha=0.5, label='MMS 50')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.title('Comparação de Médias Móveis')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout() 
    plt.show()



btc_data = pd.read_csv("C:/Users/Luiz Felipe/OneDrive/Documentos/CryptoTradingAI/btc2018-2025.csv")

btc_data.rename(columns={'Open time': 'Date'}, inplace=True)

btc_data['Date'] = pd.to_datetime(btc_data['Date'])

btc_data = btc_data[btc_data['Date'].dt.time == pd.to_datetime('18:00:00').time()]

btc_data['Date'] = btc_data['Date'].dt.date

btc_data.sort_values('Date', inplace=True)


# Prepare features and target variable
#features = btc_data[[f'Close_lag_{lag}' for lag in [1, 7, 30]]]
target = btc_data['Close']



# Splitting data into training and testing sets - let's use the last 20% of data as test set
split_index = int(len(btc_data) * 0.8)
#X_train, X_test = features[:split_index], features[split_index:]
y_train, y_test = target[:split_index], target[split_index:]

janelas = [7, 30, 50]

novo = calculoMediaMovel(btc_data, janelas)

novo = novo.tail(30)

showGraficoComparacaoMediasMoveis( novo['MMS_7'], novo['MMS_30'], novo['MMS_50'], novo['Date'])