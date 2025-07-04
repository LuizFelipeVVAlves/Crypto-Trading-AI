from pandas import DataFrame


def calculoMediaMovel(df: DataFrame, janelas: list[int]) -> DataFrame:
    """
    Calcula a média móvel de uma série temporal.
    
    :param btc: DataFrame com os dados da série temporal.
    :param janela: Tamanho da janela para calcular a média móvel.
    :return: DataFrame com a coluna 'Média Móvel'.
    """

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

    df['desvio_longo_prazo'] = (df['Close'] - df['MMS_60']) / df['MMS_60']

    '''df['feat_pos_curto'] = (df['Close'] - df['MMS_7']) / df['MMS_7']

    # Feature 2: Posição de Médio Prazo
    df['feat_pos_medio'] = (df['Close'] - df['MMS_30']) / df['MMS_30']

    # Feature 3: Força do Momentum
    df['feat_spread_curto_longo'] = (df['MMS_7'] - df['MMS_50']) / df['MMS_50']

    # Feature 4: Volatilidade Relativa
    df['feat_volatilidade_relativa'] = (df['MMS_7'] - df['MMS_30']) / df['MMS_30']

    # Feature 5: Sinal de Cruzamento (Estado do Mercado)
    df['feat_sinal_cruzamento'] = (df['MMS_30'] > df['MMS_50']).astype(int)'''

    return df
