# Modelo Preditivo para a Direção do Preço do Bitcoin 📈

## Visão Geral
O mercado de criptomoedas é notório por sua volatilidade, o que apresenta tanto riscos quanto oportunidades. Este projeto explora o uso de Machine Learning para tentar encontrar padrões em meio a esse caos aparente.

O objetivo desse trabalho foi desenvolver duas técnicas diferentes para trabalhar com predição da direção de preço. A primeira foi uma técnica clássica utilizando o modelo de Regressão Logística para a tarefa de classificação binária: prever se o preço de fechamento do dia seguinte será de Alta ou Baixa em relação ao dia atual. A segunda técnica foi um modelo moderno baseado em PLN (...)

## Objetivos do Projeto
Objetivo Principal: Desenvolver um modelo de classificação para prever a direção do movimento diário do preço do Bitcoin.

Objetivos Secundários:

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
Para que o modelo pudesse "entender" o comportamento do mercado, as seguintes features foram criadas usando a biblioteca pandas_ta:

feat_reversao_media: Mede o desvio percentual do preço em relação à sua Média Móvel de 50 dias (MMS_50).

RSI_14: O Índice de Força Relativa, um oscilador de momentum que indica condições de sobrecompra ou sobrevenda.

ATRr_14: O Average True Range, um indicador de volatilidade do mercado.

3. Definição do Alvo e Prevenção de Data Leakage
O problema foi estruturado como uma classificação binária:

Alvo (Target_Direcao): 1 se o Preço(Amanhã) > Preço(Hoje), e 0 caso contrário.

Nota Crítica: Para evitar o vazamento de dados, onde o modelo "trapaceia" usando informações do futuro, a matriz de features X foi deslocada em um período (.shift(1)). Isso garante que a previsão para o dia D utilize apenas dados conhecidos até o final do dia D-1.

4. Treinamento do Modelo
O conjunto de dados foi dividido cronologicamente em 80% para treino e 20% para teste. As features foram padronizadas com StandardScaler e, em seguida, um modelo de LogisticRegression foi treinado.

## Resultados e Análise
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