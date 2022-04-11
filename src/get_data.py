# read the features
# process the features
# return the dataframe

import os
import yaml
import pandas as pd
import argparse #For Argument parsing from the command line

def read_params(config_path): #create this 1st, It will return the yaml file
   with open(config_path) as yaml_file:
    config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path): 
    config = read_params(config_path) #read the parameters from the configuration path
    #print(config)
    data_path = config['data source']['s3_source']
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    #print(df.head())
    return df

if __name__ == '__main__': #entry point for the project
    args = argparse.ArgumentParser() # to pass the configuration file
    args.add_argument("--config", default='params.yaml') #default is params.yaml
    parsed_args = args.parse_args() #After this create get data function
    data = get_data(config_path= parsed_args.config)


