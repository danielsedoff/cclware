""" Command appender: this module will collect all commands from their sources """

from shellex import shellex, cmdc
from history import history
from note import note

def command_appender():
    """ The command collector itself """
    commands = []
    commands.append(("history", history))
    commands.append(("sh", shellex))
    commands.append(("cmdc", cmdc))
    commands.append(("note", note))
    return commands
