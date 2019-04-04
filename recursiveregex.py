#!/bin/python
import re
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("pattern")

folder = os.getcwd()

for (dirpath, dirnames, filenames) in os.walk(folder):
    for filename in filenames:
        opened = open(filepath, 'rw')
        str_f = opened.read()
        lines = str_f.split('\n')
        newlines = []
        for line in lines:
            re.sub(pattern, line)
            newlines.append(line)
        newstr = lines.join('\n')
        opened.write(newstr) 

