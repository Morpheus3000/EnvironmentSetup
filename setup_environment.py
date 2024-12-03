__author__ = "Partha Das"
__copyright__ = "Partha Das"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Partha Das"
__status__ = "Production"

'''
Script managing the setup of new development environments. Configuration is
through a json file which defines which components to setup. Each components
have their own setup scripts for modality. The config file loads them and any
associated arguments with them.
'''
import os
import subprocess
import fire
import json
from rich import print


def get_config(config_file_path):
    with open(config_file_path) as fp:
        config_dict = json.load(fp)

    print(config_dict)
    for k, v in config_dict:
        print('%s -> ' % k, v)
    return config_dict


def SetupVim():
    cmd = ['cd', 'Components']
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)


def main(config_file_path='Configs/environment_setup.json'):
    # config_dict = get_config(config_file_path)

    # Vim Setup
    SetupVim()




if __name__ == '__main__':
    fire.Fire(main)
