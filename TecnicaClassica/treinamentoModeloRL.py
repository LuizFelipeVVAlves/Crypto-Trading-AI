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



def treinamentoModeloRL(X_final, y_final, novo):

    # Splitting data into training and testing sets - let's use the last 20% of data as test set
    split_index = int(len(novo) * 0.6)
    X_train, X_test = X_final[:split_index], X_final[split_index:]
    y_train, y_test = y_final[:split_index], y_final[split_index:]

    # Create and train the model
    modelLR = LinearRegression()
    modelLR.fit(X_train, y_train)
    # Make predictions
    predictions = modelLR.predict(X_test)

    calculoMetricas(y_test, predictions)


def calculoMetricas(y_test, predictions):
    
    # Evaluate the model
    mseLR = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mseLR)
    r2LR = r2_score(y_test, predictions)



    print(f"Modelo de Regressão Linear Treinado!")
    print(f"RMSE (Erro Quadrático Médio da Raiz): {rmse:.2f}")
    print("\nIsso significa que, em média, as previsões do modelo erram em torno de ${:.2f}.".format(rmse))
    print(f"R² (Coeficiente de Determinação): {r2LR:.2f}")

    # Para ver as últimas 5 predições vs. os valores reais
    comparison = pd.DataFrame({'Real': y_test.tail(), 'Predição': predictions[-5:]})
    print("\nComparação Final:")
    print(comparison)