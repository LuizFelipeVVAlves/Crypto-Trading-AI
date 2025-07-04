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
import pandas_ta as ta

def TratamentoDeDados() -> pd.DataFrame:
    """
    Função para tratar os dados do DataFrame de Bitcoin.
    """
    btc_data = pd.read_csv("C:/Users/Luiz Felipe/OneDrive/Documentos/CryptoTradingAI/btc2018-2025.csv")

    btc_data.drop(columns=['Open', 'High', 'Low', 'Volume', 'Quote asset volume', 'Number of trades', 'Close time', 'Taker buy base asset volume',
                           'Taker buy quote asset volume', 'Ignore'], inplace=True)

    btc_data.rename(columns={'Open time': 'Date'}, inplace=True)

    btc_data['Date'] = pd.to_datetime(btc_data['Date'])

    btc_data = btc_data[btc_data['Date'].dt.time == pd.to_datetime('18:00:00').time()]

    btc_data['Date'] = btc_data['Date'].dt.date

    btc_data.sort_values('Date', inplace=True)

    janelas = [60, 90, 120]

    btc_data = calculaFeaturesMediaMovel(btc_data, janelas)

    btc_data.dropna(inplace=True)

    btc_data['Target'] = btc_data['Close'].shift(-1)


    btc_data.dropna(inplace=True)


    # Prepare features and target variable
    features = btc_data[[ 'MMS_90', 'MMS_120', 'MMS_60', 'desvio_longo_prazo']]
    target = btc_data['Target']


    final_df = pd.concat([features, target], axis=1)
    final_df.dropna(inplace=True)

    X_final = final_df.drop('Target', axis=1)
    y_final = final_df['Target']
    
    return X_final, y_final, btc_data
