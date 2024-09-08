newline = "\n"

def history(line):
    with open('ccl.log') as log_file:
        lines = list(filter(lambda l: line in l, log_file.readlines()))
        print("".join(lines))
