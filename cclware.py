""" cclware main module. see danielsedoff@github """

from datetime import datetime
from shellex import shellex, cmdc
from history import history


NEWLINE = "\n"
LOG_FILE = 'ccl.log'

commands = []
commands.append(("history", history))
commands.append(("sh", shellex))
commands.append(("cmdc", cmdc))

def extract_params(line, cmd):
    """ extract parameters from the user input string """
    return line[len(cmd):]

def time_now():
    """ current date and time as string formatted together with prompt symbol """
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S > ")
    return dt

def log(line):
    """ append a line to the log file """
    with open(LOG_FILE, 'a', encoding='utf8') as log_file:
        log_file.write(time_now() + line + NEWLINE)

while True:
    userLine = input("> ").strip()
    log(userLine)
    userCmd = userLine.split(" ")[0]
    for command in commands:
        if command[0] == userCmd:
            commandFunction = command[1]
            commandFunction(extract_params(userLine, userCmd))
