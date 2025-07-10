from pandas import DataFrame


def calculoMediaMovel(df: DataFrame, janelas: list[int]) -> DataFrame:
   

    for janela in janelas:
        # Verifica se a janela é válida
        if janela <= 0:
            raise ValueError("O tamanho da janela deve ser um número positivo.")
        
        # Calcula a média móvel e adiciona ao DataFrame
        df[f'MMS_{janela}'] = df['Close'].rolling(window=janela).mean()
    
    
    
    return df


def calculaFeaturesMediaMovel(df: DataFrame, janelas: list[int]) -> DataFrame:

    df = calculoMediaMovel(df, janelas)
    # Feature 1: Posição de Curto Prazo

    for j in janelas:
        df[f'desvio_{j}'] = (df['Close'] - df[f'MMS_{j}']) / df[f'MMS_{j}']


    return df
