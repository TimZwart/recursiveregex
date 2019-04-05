#!/bin/python
import re
import argparse
import os
import pdb

parser = argparse.ArgumentParser()
parser.add_argument("pattern")
parser.add_argument("replacement")
arguments = parser.parse_args()

folder = os.getcwd()


for (dirpath, dirnames, filenames) in os.walk(folder):
    for filename in filenames:
        filepath = "/".join([dirpath , filename])
        opened = open(filepath)
        str_f = opened.read()
        opened.close()
        lines = str_f.split('\n')
        newlines = []
        for line in lines:
            newline = re.sub(arguments.pattern, arguments.replacement, line)
            newlines.append(newline)
        newstr = '\n'.join(newlines)
        opened = open(filepath, 'w')
        opened.write(newstr)
        opened.close() 

