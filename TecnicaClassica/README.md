# Técnica Clássica 📈

## Visão Geral

Modelo de Regressão Logística implementado para prever se o preço do dia seguinte sobe ou desce com base em diferentes features.

## Objetivos do Projeto

Realizar o pré-processamento de dados históricos de preço do BTC.

Aplicar engenharia de features para criar indicadores técnicos robustos (RSI, ATR, etc.).

Garantir a integridade do modelo, prevenindo vazamento de dados (data leakage) em séries temporais.

Treinar e avaliar o modelo de Regressão Logística.

Analisar a performance do modelo através da Matriz de Confusão e outras métricas.

Interpretar os coeficientes do modelo para entender quais features são mais influentes.

## Tecnologias Utilizadas
Python 3.x

Pandas para manipulação de dados.

Pandas TA para cálculo de indicadores técnicos.

Scikit-learn para treinamento do modelo e avaliação.

Matplotlib / Seaborn para visualização de dados.

## Metodologia
O desenvolvimento do modelo seguiu um pipeline bem definido:

1. Coleta e Pré-processamento
Os dados históricos do Bitcoin (arquivo .csv) foram carregados, limpos e formatados. A coluna de data foi convertida para o tipo datetime e os dados foram ordenados cronologicamente.

2. Engenharia de Features
Para que o modelo pudesse "entender" o comportamento do mercado, algumas features foram desenvolvidas a partir de médias móveis de curto e médio prazo.

3. Definição do Alvo e Prevenção de Data Leakage
O problema foi estruturado como uma classificação binária:

Alvo (Target): 1 se o Preço(Amanhã) > Preço(Hoje), e 0 caso contrário.

4. Treinamento do Modelo
O conjunto de dados foi dividido cronologicamente em 80% para treino e 20% para teste. As features foram padronizadas com StandardScaler e, em seguida, um modelo de LogisticRegression foi treinado.

## Resultados e Análise

A primeira análise feita foi para a de finição do Dataset. Optamos por um conjunto de dados que englobasse os dados mais recentes possíveis, sendo estes retirados do site Kagle. Após isso, foi definido algumas features que poderiam ajudar ele a prever as movimentações do mercado, como as médias móveis. Abaixo segue a matriz de correlação com as colunas do dataset.

![Matriz de Correlação] (./images/matriz_correlação.png)

Como é possível observar, existem algumas features que estão fortemente relacionadas umas com as outras COM VALOR 1.0, então optamos por tira-las, deixando dentre essas apenas a média móvel dos últimos 15 dias (MMS_15)

O modelo treinado foi avaliado no conjunto de teste, que corresponde a dados que o modelo nunca viu durante o treinamento.

Matriz de Confusão
A Matriz de Confusão abaixo resume a performance do modelo, mostrando os acertos e os tipos de erros cometidos.

[Insira aqui a imagem da sua Matriz de Confusão, por exemplo: ![Matriz de Confusão](imagens/matriz_confusao.png)]

Verdadeiros Positivos (VP): [Seu número aqui]

Verdadeiros Negativos (VN): [Seu número aqui]

Falsos Positivos (FP): [Seu número aqui]

Falsos Negativos (FN): [Seu número aqui]

Métricas de Desempenho
Métrica

Valor (%)

Descrição

Acurácia

[Seu valor]%

Porcentagem geral de acertos.

Precisão

[Seu valor]%

Das vezes que o modelo previu "Sobe", ele acertou.

Recall

[Seu valor]%

De todas as altas reais, o modelo identificou esta porcentagem.

F1-Score

[Seu valor]

Média harmônica entre Precisão e Recall.


Exportar para as Planilhas
[Faça aqui uma breve análise dos seus resultados numéricos.]

## Conclusão
Este projeto estabeleceu com sucesso um pipeline para a criação de um modelo preditivo para o mercado de Bitcoin. O modelo de Regressão Logística serviu como um baseline robusto, demonstrando [resuma a performance, ex: "uma capacidade modesta, mas positiva, de identificar padrões direcionais"].

A análise dos coeficientes e das métricas, como a Precisão, fornece insights valiosos sobre o comportamento do modelo e as dinâmicas de mercado que ele foi capaz de capturar.

## Próximos Passos
[ ] Testar modelos mais complexos (Random Forest, Gradient Boosting).

[ ] Expandir o conjunto de features com mais indicadores técnicos e dados de volume.

[ ] Realizar um backtesting financeiro para simular o retorno de uma estratégia de negociação.

[ ] Otimizar os hiperparâmetros do modelo para melhorar o desempenho.

[ ] Incorporar dados externos, como análise de sentimento de notícias ou redes sociais.