__author__ = "Partha Das"
__copyright__ = "Partha Das"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Partha Das"
__status__ = "Production"

'''
Utility file to store the common helper functions for the software.
'''
import os
import fire
import subprocess
# import Path
from rich import print


def prog_runner(cmd_str, raise_error=True, capture_output=True, text=True):
    cmd = cmd_str.split(' ')
    result = subprocess.run(cmd, check=raise_error,
                            capture_output=capture_output, text=text)

    return_dict = {
        'out': result.stdout,
    }

    if not raise_error:
        return_dict['err'] = result.stderr

    return return_dict
