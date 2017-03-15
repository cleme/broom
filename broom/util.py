#!/usr/bin/env python
from __future__ import division

__author__ = "Jose C. Clemente"
__copyright__ = "Copyright 2017, The Clemente Lab"
__credits__ = ["Jose C. Clemente"]
__license__ = "GPL"
__version__ = "0.1-dev"
__maintainer__ = "Jose C. Clemente"
__email__ = "jose.clemente@gmail.com"

##############################
## General helper functions ##
##############################

def command_handler(commands, logger, close_logger, print_commands=False):
    """ Partially adapted from QIIME.
    """
    if print_commands:
        print commands
    else:
        for c in commands:
            out, err, val = system_call(c)

def system_call(cmd, shell=True):
    """ Originally from QIIME.

    Call cmd and return (stdout, stderr, return_value).

    cmd can be either a string containing the command to be run, or a sequence
    of strings that are the tokens of the command.

    Please see Python's subprocess. Popen for a description of the shell
    parameter and how cmd is interpreted differently based on its value.

    """
    proc = Popen(cmd,
                 shell=shell,
                 universal_newlines=True,
                 stdout=PIPE,
                 stderr=PIPE)
    # communicate pulls all stdout/stderr from the PIPEs to
    # avoid blocking -- don't remove this line!
    stdout, stderr = proc.communicate()
    return_value = proc.returncode
    
    return stdout, stderr, return_value
