# read the data from data source file
# save it in data/raw for further processing

import os
from get_data import read_params, get_data
# read_params will return the config file, get_data will return you the dataframe
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(' ', '_') for col in df.columns]
    raw_data_path = config["load data"]["raw_dataset_csv"]

    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)

if __name__ == '__main__':
    args = argparse.ArgumentParser() # to pass the configuration file
    args.add_argument("--config", default='params.yaml') #default is params.yaml
    parsed_args = args.parse_args()
    load_and_save(config_path= parsed_args.config)