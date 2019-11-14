# -*- coding: utf-8 -*-
from utilities import *
import xgboost as xgb
from xgboost import plot_importance
from sklearn.preprocessing import Imputer

# @File  : soccer_value_regression/process.py
# @Author: Qbliu
# @Date  : 11/14/2019
# @Desc  : Processing

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def load_data(fileName):
    return pd.read_csv(fileName, low_memory=False,
                                encoding='utf-8')
def featureSet()

if __name__ == '__main__':
    train_df = load_data("./data/train.csv")
    print(train_df.head(10))

