import warnings

warnings.filterwarnings("ignore")
import pandas as pd
import yaml
import argparse


# reading the yaml data
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


# reading source data by using yaml coniguration
def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    return df


# creating config parmaters from file
def create_config(file):
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=file)
    parsed_args = args.parse_args()
    return parsed_args.config


if __name__ == "__main__":
    data = get_data(create_config("params.yaml"))
    print(data.head())
