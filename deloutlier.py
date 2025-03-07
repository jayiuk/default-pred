'''
이 함수는 데이터프레임에서 이상치를 제거해주는 함수다.
iqr을 이용해 일정 선 미만 혹은 초과인 값들을 제거해준다.
최소는 min_line이고 최대는 max_line이다.

'''

import pandas as pd
import numpy as np

def DelOutlier(df):
    i = 0
    cols = df.columns
    for i in cols:
        q1 = df[i].quantile(.25)
        q3 = df[i].quantile(.75)
        iqr = q3 - q1
        line = 1.5 * iqr
        min_line = q1 - iqr
        max_line = q3 + iqr
        min_index = df[df[i] < min_line].index
        max_index = df[df[i] > max_line].index
        df = df.drop(min_index, axis = 0)
        df = df.drop(max_index, axis = 0)
    df = df.dropna(axis = 0)
    return df