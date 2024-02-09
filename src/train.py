import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from get_data import read_params
import json

def evaluation(y_true,y_pred):
    res = dict()
    res["r2"] = r2_score(y_true=y_true,y_pred=y_pred)
    res["mse"] = mean_squared_error(y_true=y_true,y_pred=y_pred)
    res["mae"] = mean_absolute_error(y_true=y_true,y_pred=y_pred)
    return res
    
def train_evaluate():
    param = read_params("params.yaml")

    train_path = param["split_data"]["train_path"]
    test_path = param["split_data"]["test_path"]
    random_state = param["base"]["random_state"]
    alpha = param["estimators"]["ElasticNet"]["params"]["alpha"]
    l1 = param["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    target = param["base"]["target_col"]
    param_path = param["reports"]["params"]
    score_path = param["reports"]["scores"]
    columns_del = param["base"]["delete_col"]

    rem_train_cols = [target] + [columns_del]

    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    train_y = train[target]
    test_y = test[target]
    train_x = train.drop(columns=rem_train_cols,axis=1)
    test_x = test.drop(columns=rem_train_cols,axis=1)

    lr = ElasticNet(alpha=alpha,l1_ratio=l1,random_state=random_state)
    lr.fit(train_x,train_y)

    pred = lr.predict(test_x)
    eval = evaluation(test_y,pred)
    with open(score_path,"w") as f:
        json.dump(eval,f)
    with open(param_path,"w") as f:
        json.dump({"l1_ratio":l1,"alpha":alpha},f)


if __name__=="__main__":
    train_evaluate()