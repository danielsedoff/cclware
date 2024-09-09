"""This module will contain shell calls"""
import subprocess

def shellex(line):
    """Run a shell command with a check"""
    args = line.strip().split(' ')
    try:
        subprocess.run(args, check=True)
    except Exception:
        print("sh did not return 0: " + str(Exception))


def cmdc(line):
    """Run a cmd /c command in Windows"""
    shellex("cmd.exe /c " + line
)
