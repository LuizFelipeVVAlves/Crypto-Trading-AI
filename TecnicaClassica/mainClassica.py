import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

import pandas as pd

def showGrafico(btc):
    # Create a scatter plot of the actual vs predicted values
    plt.figure(figsize=(10, 6))
    plt.plot(btc['End'],btc['Close'], color='blue', alpha=0.5)
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.title('Data x Preço')
    plt.grid()
    plt.show()




btc_data = pd.read_csv("C:/Users/Luiz Felipe/OneDrive/Documentos/CryptoTradingAI/bitcoin_2010-07-17_2024-06-28.csv")


btc_data['End'] = pd.to_datetime(btc_data['End'])


btc_data.sort_values('End', inplace=True)

btc_data.drop(columns=['Start'], inplace=True)

btc_data = btc_data[btc_data['End'].dt.year >= 2016]


# Prepare features and target variable
#features = btc_data[[f'Close_lag_{lag}' for lag in [1, 7, 30]]]
target = btc_data['Close']



# Splitting data into training and testing sets - let's use the last 20% of data as test set
split_index = int(len(btc_data) * 0.8)
#X_train, X_test = features[:split_index], features[split_index:]
y_train, y_test = target[:split_index], target[split_index:]

# Review the first few rows of the features in the training data
#print(X_train.head(), y_train.head())

showGrafico(btc_data)