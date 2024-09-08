""" This module contains a History command that takes its commandline args as a whole string. """

LOG_FILE = 'ccl.log'


def history(line):
    """ The History command. """
    with open(LOG_FILE, encoding='utf8') as log_file:
        lines = list(filter(lambda l: line in l, log_file.readlines()))
        print("".join(lines))
