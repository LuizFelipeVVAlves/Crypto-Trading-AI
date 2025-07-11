# Técnica Moderna 📈

## Visão Geral

Foi desenvolvido um modelo de Inteligência Artificial utilizando uma LLM (modelo de linguagem) especializada em notícias financeiras para prever se o preço do Bitcoin no dia seguinte irá subir ou descer com base no sentimento das manchetes de notícias do dia atual.

## Objetivos do Projeto 🎯

Realizar o pré-processamento dos dados históricos de preço do BTC e suas respectivas manchetes diárias.

Aplicar um modelo de PLN para inferir o sentimento de cada notícia.

Calcular um escore médio de sentimento por dia e usá-lo para prever a movimentação de preço do dia seguinte.

Avaliar a performance da técnica moderna com métricas de classificação.

## Tecnologias Utilizadas

Python 3.x

Pandas para manipulação de dados

Transformers (HuggingFace) para análise de sentimento

Scikit-learn para métricas de avaliação

Matplotlib para visualização da matriz de confusão

## Metodologia ⚙️

1. Coleta e Pré-processamento
Os dados foram lidos de um arquivo .json contendo o preço do Bitcoin e o resumo das notícias de cada dia. As manchetes foram limpas e as datas organizadas em ordem cronológica. O alvo (target) foi definido como 1 se o preço do dia seguinte for maior que o do dia atual, e 0 caso contrário.

2. Análise de Sentimento via LLM
Utilizou-se o modelo mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis, treinado especialmente em notícias financeiras. Para cada manchete, o modelo retornou um sentimento (positivo ou negativo) com uma pontuação de confiança. Essa pontuação foi convertida em um score numérico (positivo ou negativo).

3. Agregação Diária e Previsão
Os scores de sentimento foram agrupados por dia. Se a média diária fosse maior que zero, o modelo previa que o preço subiria no dia seguinte. Caso contrário, previa queda ou estabilidade.

4. Avaliação do Modelo
As previsões foram comparadas com os dados reais utilizando métricas como acurácia, precisão, recall e matriz de confusão.

## Resultados e Análise 📊

O modelo alcançou uma performance razoável ao prever o comportamento do preço do Bitcoin apenas com base no sentimento das manchetes do dia.

**Acurácia**
61% → O modelo acertou 61% das previsões gerais.

**Precisão**
61% → Das vezes em que o modelo previu "Sobe", ele acertou 61%.

**Recall**
61% → De todos os dias em que o preço realmente subiu, o modelo identificou corretamente 61%.

# Conclusão 🏁

A técnica moderna baseada em modelos de linguagem demonstrou um bom desempenho mesmo sem usar dados numéricos de mercado. Isso mostra que o sentimento presente nas manchetes pode ser um sinal relevante para prever o comportamento do preço. Apesar disso, o modelo pode ser aprimorado ao combinar essa abordagem textual com indicadores técnicos e históricos quantitativos, formando uma solução híbrida mais precisa e robusta para a previsão em mercados financeiros voláteis como o de criptomoedas.