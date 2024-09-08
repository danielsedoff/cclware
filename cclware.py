from datetime import datetime
from history import history 


newline = "\n"
commands = []
commands.append(("history", history))

def extract_params(line, cmd):
    return line[len(cmd):]

def time_now():
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S > ")
    return dt

def log(line):
    with open('ccl.log', 'a') as log_file:
        log_file.write(time_now() + line + newline)
    
while(True):
    userLine = input("> ").strip()
    log(userLine)
    userCmd = userLine.split(" ")[0]
    print ("cmd is: " + userCmd)
    for command in commands:
        if(command[0] == userCmd):
            commandFunction = command[1]
            commandFunction(extract_params(userLine, userCmd))
    
