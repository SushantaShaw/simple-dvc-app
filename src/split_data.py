import warnings
warnings.filterwarnings("ignore")
import pandas as pd 
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_load():
    param = read_params("params.yaml")

    train_path = param["split_data"]["train_path"]
    test_path = param["split_data"]["test_path"]
    split_ratio = param["split_data"]["test_size"]
    random_state = param["base"]["random_state"]

    raw_data_path = param["load_data"]["raw_dataset_csv"]
    raw_data = pd.read_csv(raw_data_path)
    raw_data = raw_data.dropna()
    train,test = train_test_split(raw_data,test_size=split_ratio,random_state=random_state)

    train.to_csv(train_path,index=False)
    test.to_csv(test_path,index=False)

if __name__=="__main__":
    split_and_load()