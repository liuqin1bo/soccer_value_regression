# -*- coding: utf-8 -*-
from utilities import *
import os
import shutil
from pandas_profiling import ProfileReport
import xgboost as xgb
from xgboost import plot_importance
from sklearn.preprocessing import Imputer

# @File  : soccer_value_regression/process.py
# @Author: Qbliu
# @Date  : 11/14/2019
# @Desc  : Processing
precode = True  ## 代码试验工作, 非运行代码
submit_file_has_generated = False
stats_file_has_generated = True

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def load_data(fileName):
    return pd.read_csv(fileName, low_memory=False,
                       encoding='utf-8')
def train_df_stats(train_df):
    stats_dir = "./stats"
    if  not stats_file_has_generated:
        try:
            # create the output Directory
            if  os.path.exists(stats_dir):
                shutil.rmtree(stats_dir)
                print("Directory ", stats_dir, " Removed.")
                os.mkdir(stats_dir)
                print("Directory ", stats_dir, " Created.")
            else:
                os.mkdir(stats_dir)
                print("Directory ", stats_dir, " Created.")
        except FileExistsError:
            print("Creation of the directory %s failed" % stats_dir)
        data_stats_profile = train_df.profile_report(title='Soccer Player Dataset',style={'full_width': True})
        data_stats_profile.to_file(stats_dir + '/data_stats_profile.html')


    
    
def get_train_feature_list(feature):
    train_feature = [x for x in feature if
                         x not in ['id', 'birth_date', 'height_cm', 'weight_kg',
                                   'nationality', 'pac', 'sho', 'pas', 'dri', 'def',
                                   'phy', 'skill_moves', 'weak_foot',
                                   'work_rate_att', 'work_rate_def', 'preferred_foot', 'crossing',
                                   'finishing', 'heading_accuracy', 'short_passing', 'volleys',
                                   'dribbling', 'curve', 'free_kick_accuracy', 'long_passing',
                                   'acceleration', 'sprint_speed', 'agility',
                                   'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
                                   'strength', 'long_shots', 'aggression', 'interceptions',
                                   'positioning', 'vision', 'penalties', 'marking', 'standing_tackle',
                                   'sliding_tackle', 'gk_diving', 'gk_handling', 'gk_kicking',
                                   'gk_positioning', 'gk_reflexes', 'rw', 'rb', 'st', 'lw', 'cf',
                                   'cam', 'cm', 'cdm', 'cb', 'lb', 'gk', 'y']]
    return train_feature

def get_test_data_for_train(fileName, train_feature):
    df = pd.read_csv(fileName, low_memory=False,
                       encoding='utf-8')
    today = date(2018, 1, 1)
    df['birth_date'] = pd.to_datetime(df['birth_date']).dt.date
    df['age'] = (today - df['birth_date']).apply(lambda x: x.days) / 365.0
    print(df[train_feature].head(5))  # 只是验证一下训练和测试的特征排序是否一致
    return df[train_feature].values

# 训练与测试函数
def train_and_test(X_train, Y_train, X_test):
    # XGBoost 训练
    model = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, silent=False,
                             objective='reg:gamma')
    model.fit(X_train, Y_train)
    ans = model.predict(X_test).round().astype(np.int)
    id_list = np.arange(10441, 17441)
    print(type(ans))
    predict_df = pd.DataFrame({'id': id_list, 'y': ans})
    
    output_dir = "./output"
    if  not submit_file_has_generated:
        try:
            # create the output Directory
            if  os.path.exists(output_dir):
                shutil.rmtree(output_dir)
                print("Directory ", output_dir, " Removed.")
                os.mkdir(output_dir)
                print("Directory ", output_dir, " Created.")
            else:
                os.mkdir(output_dir)
                print("Directory ", output_dir, " Created.")
        except FileExistsError:
            print("Creation of the directory %s failed" % output_dir)
        predict_df.to_csv("./output/submit.csv", index=None)
    plot_importance(model)
    plt.show()
    
if __name__ == '__main__':
    train_df = load_data("./data/train.csv")
    # 获得球员年龄
    today = date(2018, 1, 1)
    train_df['birth_date'] = pd.to_datetime(train_df['birth_date']).dt.date
    train_df['age'] = (today - train_df['birth_date']).apply(lambda x: x.days) / 365.0
    print(train_df.head(10))
    print(train_df.info())
    train_df_stats(train_df)  # 输出训练数据统计结果
    

    if precode:
        feature = train_df.columns.values.tolist()
        print("feature is:\n", feature)
        train_feature = get_train_feature_list(feature)
        # train_feature = ['club', 'league', 'potential', 'international_reputation']
        print("train_feature is:\n", train_feature)
        X = train_df[train_feature].values
        Y = train_df['y'].values
        X_train = X  # 后面我们可以修改
        Y_train = Y  # 后面我们可以修改
        X_test = get_test_data_for_train("./data/test.csv", train_feature)
        train_and_test(X_train, Y_train, X_test)