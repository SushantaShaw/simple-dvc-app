import warnings
warnings.filterwarnings("ignore")
import pandas as pd 
import argparse
from get_data import read_params,get_data,create_config

def save_and_load():
    config_path = create_config("params.yaml")
    config = read_params(config_path) #reading params.yaml
    data = get_data(config_path) #reading data
    data.columns = [i.replace(" ","_") for i in data.columns] #removing space from exisiting column names

    raw_data_path = config["load_data"]["raw_dataset_csv"] #reading raw data
    data.to_csv(raw_data_path,index=False) #loading the data in the specified path
    print(data.head())

if __name__=="__main__":
   save_and_load()