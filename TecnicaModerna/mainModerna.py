import json
import pandas as pd
from transformers import pipeline
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, classification_report
import matplotlib.pyplot as plt



with open('./Data/bitcoin_practice.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print("Arquivo JSON carregado com sucesso.")

all_prices = []
all_news = []
for date_str, content in data.items():

    date = pd.to_datetime(date_str)
    all_prices.append({'Date': date, 'Price': content['prices']})

    for news_item in content['news_summary']:

        clean_headline = news_item.split('(sentiment:')[0].strip()
        all_news.append({'Date': date, 'Headline': clean_headline})


df_prices = pd.DataFrame(all_prices).sort_values('Date')
df_news = pd.DataFrame(all_news)

print("Passo 1: Dados carregados e estruturados.")


df_prices['Next_Day_Price'] = df_prices['Price'].shift(-1)

df_prices['Target_Real'] = (df_prices['Next_Day_Price'] > df_prices['Price']).astype(int)


df_prices.dropna(inplace=True)

print("Passo 2: Alvo real ('Target_Real') criado.")



print("Passo 3: Carregando o modelo de PLN... Isso pode levar um momento.")

sentiment_pipeline = pipeline("sentiment-analysis", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis")


def get_sentiment_score(headline):
    try:
        result = sentiment_pipeline(headline)[0]
        if result['label'] == 'positive':
            return result['score']
        elif result['label'] == 'negative':
            return -result['score']
        return 0.0 
    except Exception as e:
        print(f"Erro ao analisar a manchete: {headline} -> {e}")
        return 0.0


print("Analisando o sentimento de cada notícia... Seja paciente.")
df_news['sentiment_score'] = df_news['Headline'].apply(get_sentiment_score)
print("Análise de sentimento concluída.")


df_sentimento_diario = df_news.groupby('Date')['sentiment_score'].mean().to_frame()

df_sentimento_diario['Previsao_LLM'] = (df_sentimento_diario['sentiment_score'] > 0).astype(int)

print("Passo 4: Previsões da LLM geradas com base no sentimento diário.")

df_final = df_prices.join(df_sentimento_diario, on='Date')
df_final.dropna(inplace=True)


y_real = df_final['Target_Real']
y_previsto_pela_llm = df_final['Previsao_LLM']

print("\n--- AVALIAÇÃO FINAL DO MODELO DE PLN ---")

acuracia = accuracy_score(y_real, y_previsto_pela_llm)
print(f"Acurácia Final: {acuracia:.2%}")
print("\nRelatório de Classificação:")
print(classification_report(y_real, y_previsto_pela_llm, target_names=['Desce/Mantém', 'Sobe']))


cm = confusion_matrix(y_real, y_previsto_pela_llm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Desce/Mantém', 'Sobe'])
disp.plot(cmap='Blues')
plt.title('Matriz de Confusão (Previsão via Sentimento de Notícias)')
plt.show()

