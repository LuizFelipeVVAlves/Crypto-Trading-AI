import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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