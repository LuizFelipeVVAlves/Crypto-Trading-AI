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


def main():

    X_final, y_final, novo = td.TratamentoDeDados()

    trl.treinamentoModeloRL(X_final, y_final, novo)




main()
