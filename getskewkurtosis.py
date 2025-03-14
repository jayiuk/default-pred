'''
왜도와 첨도를 구하는 함수.
skew, kurtosis만 해주면 어떤 열이 어떤 왜도, 첨도를 갖는지 모름.
그래서 열 이름과 왜도, 첨도를 같이 나타내주는 함수를 만듬
'''

from scipy.stats import skew, kurtosis

def GetSkew(df):
    skews = []
    cols = df.columns
    for i in cols:
        skewi = skew(df[i])
        s = f'{df[i].name} = {skewi}'
        skews.append(s)
    return skews

def GetKurtosis(df):
    kurtosises = []
    cols = df.columns
    for i in cols:
        kurtosisi = kurtosis(df[i], fisher = True)
        k = f'{df[i].name} = {kurtosisi}'
        kurtosises.append(k)
    return kurtosises