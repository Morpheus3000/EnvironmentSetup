__author__ = "Partha Das"
__copyright__ = "Partha Das"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Partha Das"
__status__ = "Production"

'''
Vim setup module. Downloads Vundle and sets up the dot files from the
github repo.
'''
import os
import fire
from rich import print


def main(
    universal_dict={
        "DotFileLoc": "dot_files",
        "DownloadLoc": "~/Configs/",
        "SymLink": True,
    },
    config_dict={
        'PluginManager': 'Vundle',
        'VimDotName': '_vimrc'
    }
):
    config_dict = {k:x.lower() for k, x in config_dict.items()}
    universal_dict = {k:x.lower() for k, x in universal_dict.items()}
    print('[magenta]Getting Vundle...')
    cmd = ['git', 'clone']

    if config_dict['PluginManager'] == 'vundle':
        cmd.append('Vundle link')
        # Clone the repo to the location

    #  the dot file to the location
    if universal_dict['SymLink']:
        pass
    else:
        pass
    print(config_dict)
    print(cmd)

if __name__ == '__main__':
    fire.Fire(main)
