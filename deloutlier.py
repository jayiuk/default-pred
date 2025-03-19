'''
이 함수는 데이터프레임에서 이상치를 제거해주는 함수다.
iqr을 이용해 일정 선 미만 혹은 초과인 값들을 제거해준다.
최소는 min_line이고 최대는 max_line이다.
이 값을 기준으로 이상치를 제거
'''
'''
zscore를 기준으로 이상치를 제거하는 함수도 추가했다.
이 함수는 반복문을 이용해 각 열별로 해당 값의 zscore를 구한다.
그 후 그 zscore가 일정 값을 넘어가면 nan으로 바꾼다.
마지막 데이터프레임에서 dropna를 해줌.
'''

import pandas as pd
import numpy as np

def DelOutlier(df):
    cols = df.columns
    for i in cols:
        q1 = df[i].quantile(.25)
        q3 = df[i].quantile(.75)
        iqr = q3 - q1
        line = 1.5 * iqr
        min_line = q1 - line
        max_line = q3 + line
        df[i] = np.where((df[i] < min_line) | (df[i] > max_line), np.nan, df[i])
    df = df.dropna(axis = 0)
    return df

def DelOutlierZscore(df):
    th = 3
    cols = df.columns
    for i in cols:
        z = np.abs(df[i] - np.mean(df[i])) / np.std(df[i])
        df[i] = np.where(z > th, np.nan, df[i])
    df = df.dropna(axis = 0)
    return df