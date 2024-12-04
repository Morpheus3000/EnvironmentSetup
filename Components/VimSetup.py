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
import subprocess
# import Path
from rich import print
# from ..Utils import prog_runner


def prog_runner(cmd_str, raise_error=True, capture_output=True, text=True):
    if type(cmd_str) == str:
        cmd = cmd_str.split(' ')
    result = subprocess.run(cmd, check=raise_error,
                            capture_output=capture_output, text=text)

    return_dict = {
        'out': result.stdout,
    }

    if not raise_error:
        return_dict['err'] = result.stderr

    return return_dict

def main(
    universal_dict={
        "DotFileLoc": "dot_files",
        "SymLink": True,
    },
    config_dict={
        'PluginManager': 'Vundle',
        'VimDotName': '_vimrc'
    }
):
    config_dict = {k:x.lower() for k, x in config_dict.items()}
    # TODO: Add else cause in the dictionary comprehension
    # universal_dict = {k:x.lower() for k, x in universal_dict.items() if type(x)
    #                  is not bool}
    print('[magenta]Getting Vundle...')
    cmd = ['git', 'clone']

    if config_dict['PluginManager'] == 'vundle':
        cmd.append('https://github.com/VundleVim/Vundle.vim.git')
        cmd.append('~/.vim/bundle/Vundle.vim')
        # Clone the repo to the location

    print(config_dict)
    print(universal_dict)
    print(cmd)

    #  the dot file to the location
    if universal_dict['SymLink']:
        pass
    else:
        pass
    prog_dict = prog_runner('ls ../Components', raise_error=True)
    # cmd = ['ls', 'Componentys']
    # result = subprocess.run(cmd, check=False, capture_output=True, text=True)

    if prog_dict['err']:
        print('[red]Std Errors:\n', prog_dict['err'])
    else:
        print('[blue]Std Out:\n', prog_dict['out'])
        print('[magenta]Run completed with no errors!')



if __name__ == '__main__':
    fire.Fire(main)
