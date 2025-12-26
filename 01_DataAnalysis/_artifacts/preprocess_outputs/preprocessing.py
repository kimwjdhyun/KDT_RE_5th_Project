import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#행열 정리 코드
def clean_structure(df):
    df = df.iloc[:-3, :-3]      # 뒤쪽 행/열 제거만
    return df.reset_index(drop=True)

#강제로 행,열 정리하는 것이므로 전처리 과정에 크게 유용하지 못함.


#결측값 처리 (평균 값으로 대체)
def handle_rainfall_missing(df,col):
    if not pd.api.types.is_numeric_dtype(df[col]):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    pre = df[col].mean().round(1)
    df[col] = df[col].fillna(pre)

    return df

#결측값 처리 (평균 값으로 대체)= 범용성 있도록 개선한 함수는 이 쪽.
def handle_missing(df, col):
    if not pd.api.types.is_numeric_dtype(df[col]):
        df[col] = pd.to_numeric(df[col], errors="coerce")

    pre = df[col].mean().round(1)
    df[col] = df[col].fillna(pre)

    return df