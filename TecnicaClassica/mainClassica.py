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
import tratamentoDados as td
import treinamentoModeloRL as trl

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

def showGraficoComparacaoRealxPrevisao(previsao, real, Datas):
    plt.figure(figsize=(10, 6))
    plt.plot(Datas, previsao, color='blue', alpha=0.5, label='Previsão')
    plt.plot(Datas, real, color='orange', alpha=0.5, label='Real')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.title('Comparação de Previsão x Real')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout() 
    plt.show()


def main():

    X_final, y_final, novo = td.TratamentoDeDados()

    trl.treinamentoModeloRL(X_final, y_final, novo)




main()






'''
# Create and train the Random Forest model
modelRF = RandomForestRegressor(n_estimators=100, random_state=42)
modelRF.fit(X_train, y_train)
# Make predictions with Random Forest
predictions_rf = modelRF.predict(X_test)
# Evaluate the Random Forest model
mseRF = mean_squared_error(y_test, predictions_rf)
rmse_rf = np.sqrt(mseRF)
r2RF = r2_score(y_test, predictions_rf)

print(f"Modelo de Regressão RF Treinado!")
print(f"RMSE (Erro Quadrático Médio da Raiz): {rmse_rf:.2f}")
print("\nIsso significa que, em média, as previsões do modelo erram em torno de ${:.2f}.".format(rmse_rf))
print(f"R² (Coeficiente de Determinação): {r2RF:.2f}")

comparison_rf = pd.DataFrame({'Real': y_test.tail(), 'Predição': predictions_rf[-5:]})
print("\nComparação Final:")
print(comparison_rf)

#results_df = pd.DataFrame({
#   'Preço Real': y_test,
#    'Previsão do Modelo': predictions,
#    'Data': datas_test
#})
#showGraficoComparacaoRealxPrevisao(results_df['Previsão do Modelo'].tail(50), results_df['Preço Real'].tail(50), results_df['Data'].tail(50))


#showGraficoComparacaoMediasMoveis( novo['MMS_7'], novo['MMS_30'], novo['MMS_50'], novo['Date'])

# 1. Extrair a importância das features
importances_rf = modelRF.feature_importances_

# 2. Criar um DataFrame para melhor visualização
features_rf_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': importances_rf
}).sort_values(by='Importance', ascending=False)

print("--- Importância das Features (Random Forest) ---")
print(features_rf_df)

# 3. Criar um gráfico de barras para visualizar
plt.figure(figsize=(12, 8))
sns.barplot(x='Importance', y='Feature', data=features_rf_df, palette='viridis')

plt.title('Importância de Cada Feature no Modelo Random Forest', fontsize=16)
plt.xlabel('Importância Relativa', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.show()






# 1. Padronizar as features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # Usa o mesmo scaler do treino

# 2. Treinar um NOVO modelo de Regressão Linear com os dados escalados
modelLR_scaled = LinearRegression()
modelLR_scaled.fit(X_train_scaled, y_train)

# 3. Extrair os coeficientes
coefficients_lr = modelLR_scaled.coef_

# 4. Criar um DataFrame para visualização
features_lr_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Coefficient': coefficients_lr
}).sort_values(by='Coefficient', ascending=False)

print("\n--- Influência das Features (Regressão Linear) ---")
print(features_lr_df)


# 5. Visualizar os coeficientes
plt.figure(figsize=(12, 8))
sns.barplot(x='Coefficient', y='Feature', data=features_lr_df, palette='coolwarm')
plt.title('Influência de Cada Feature no Modelo de Regressão Linear', fontsize=16)
plt.xlabel('Valor do Coeficiente', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.axvline(x=0, color='black', linewidth=0.8) # Linha no zero para referência
plt.show()
'''