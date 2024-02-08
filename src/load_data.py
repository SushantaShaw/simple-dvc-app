import warnings
warnings.filterwarnings("ignore")
import pandas as pd 
import argparse
from get_data import read_params,get_data,create_config

def save_and_load():
    config_path = create_config("params.yaml")
    config = read_params(config_path)
    data = get_data(config_path)
    data.columns = [i.replace(" ","_") for i in data.columns]

    raw_data_path = config["load_data"]["raw_dataset_csv"]
    data.to_csv(raw_data_path,index=False)
    print(data.head())

if __name__=="__main__":
   save_and_load()