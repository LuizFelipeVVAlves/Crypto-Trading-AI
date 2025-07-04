Crypto Trading AI



Análises

- Utilizar a Média Móvel dos ultimos 7 dias faz a previsão ser extremamente parecido. Suspeita de Data Leakage, modelo provavelmente está considerando os valores mais recentes, sem uma visão de longo prazo.

Modelo de Regressão Linear Treinado!
RMSE (Erro Quadrático Médio da Raiz): 1743.14

Isso significa que, em média, as previsões do modelo erram em torno de $1743.14.
R² (Coeficiente de Determinação): 0.99
Comparação Final:
             Real       Predição
262004  106802.54  105014.984929
262100  107416.91  105672.646425
262196  107445.40  106719.055233
262292  107366.75  107282.979764
262388  106140.15  107061.967175

- Nesse proximo caso, utilizei médias móveis mais longas, de 60, 90 e 120 dias

Modelo de Regressão Linear Treinado!
RMSE (Erro Quadrático Médio da Raiz): 6475.52

Isso significa que, em média, as previsões do modelo erram em torno de $6475.52.
R² (Coeficiente de Determinação): 0.95

Comparação Final:
             Real       Predição
261908  106802.54  110673.558175
262004  107416.91  110657.534993
262100  107445.40  110601.823868
262196  107366.75  110597.255301
262292  106140.15  110454.307062

 - Adicionei uma feature que calcula o quao "esticado" a predição está em relação ao preço verdadeiro

 Modelo de Regressão Linear Treinado!
RMSE (Erro Quadrático Médio da Raiz): 4709.42

Isso significa que, em média, as previsões do modelo erram em torno de $4709.42.
R² (Coeficiente de Determinação): 0.97

Comparação Final:
             Real       Predição
261908  106802.54  107937.826009
262004  107416.91  107861.048263
262100  107445.40  107991.918777
262196  107366.75  108054.996627
262292  106140.15  108011.617259


