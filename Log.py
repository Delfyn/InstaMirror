import sys
import time


class LogFile:
    """Create log.txt with neceseary information."""

    def __init__(self, name='log.txt'):
        self.name = name

    def terminal_to_file(self, text):  # TODO FIX
        """Basicly IM.py > file.txt"""
        # f = open(self.name + 'a')
        # f.write(text + '\n')
        with open(self.name, 'a') as out:
            out.write('1' + '\n')
