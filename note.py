""" This module contains basic note taking. Really basic, at least now. """

LINE_PROMPT = ">> "
NOTES_FILE = 'notes.log'
NEWLINE = '\n'

def num_format(num, max_num):
    """ Line number formatter. """
    max_num_len = len(str(max_num))
    num_len = len(str(num))
    return '0' * (max_num_len - num_len) + str(num)

def search_note(fragment):
    """ Search the NOTES_FILE for *line* """
    with open(NOTES_FILE, encoding='utf8') as notes_file:
        lines = notes_file.readlines()
        max_num = len(lines)
        for i, line in enumerate(lines):
            if fragment.strip().upper() not in line.upper():
                continue
            print('')
            print('   Line ' + num_format(i - 1 + 1, max_num + 1) + ': ' + lines[i - 1] if i > 0 else '', end='')
            print('>> Line ' + num_format(i + 1, max_num + 1) + ': ' + lines[i], end='')
            print('   Line ' + num_format(i + 1 + 1, max_num + 1) + ': ' + lines[i + 1] if i < max_num else '', end='')
        print('')

def write_note(lines):
    """Append the new note to the NOTES_FILE"""
    with open(NOTES_FILE, 'a', encoding='utf8') as notes_file:
        notes_file.write(NEWLINE.join(lines))

def add_note():
    """Get the new note content from keyboard input"""
    print(">> Writing a new note. 3 x [ENTER] = END.")
    lines = []
    while True:
        nextline = input(LINE_PROMPT)
        lines.append(nextline)
        if len(lines) > 2:
            if '' == (''.join(lines[-3:])):
                write_note(lines)
                break

def note(line):
    """Process the *note* command with or without args"""
    if len(line.strip()) == 0:
        add_note()
    else:
        search_note(line)
