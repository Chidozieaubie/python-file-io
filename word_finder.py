#! /usr/bin/env python3

import sys
import re


with open('origin.txt', 'r') as in_stream:
    with open('result.txt', 'w') as out_stream:
        lineNumber = 0
        for line in in_stream:
            line = line.strip()
            lineNumber += 1
            wordobj = re.compile(r'(\w*herit\w*)', re.IGNORECASE)
            word_list = wordobj.findall(line)
            for word in word_list:
                out_stream.write('{0}\t{1}\n'.format(lineNumber, word))
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('result.txt is closed?', out_stream.closed)



