import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from utils import calculaFeaturesMediaMovel
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay



def treinamentoModeloRL(features, target, novo):

    
    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    
    modelLR = LogisticRegression()
    modelLR.fit(X_train, y_train)
    
    predictions = modelLR.predict(X_test)

    calculoMetricas(y_test, predictions)


def calculoMetricas(y_test, predictions):
    
    ac_score = accuracy_score(y_test, predictions) #Acertos Totais / Total de Amostras
    pc_score = precision_score(y_test, predictions) #Acertos Positivos / (Acertos Positivos + Falsos Positivos) --- A capacidade do modelo de não prever como positivo um exemplo negativo
    rc_score = recall_score(y_test, predictions) # Acertos Positivos / (Acertos Positivos + Falsos Negativos) --- A capacidade do modelo de prever como positivo um exemplo positivo
    print(f"Accuracy: {ac_score:.2f}")
    print(f"Precision: {pc_score:.2f}")
    print(f"Recall: {rc_score:.2f}")

    
    cm = confusion_matrix(y_test, predictions)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Desce(0)', 'Sobe(1)'])
    disp.plot(cmap='Blues')
    plt.title('Matriz de Confusão')
    plt.show()