#! /usr/bin/env python3

import sys
import re
"""
This is a 'hardcoded' function that returns a list of word string alongside
line numbers from a text text file when queried with a string pattern.
I unfortunately could not get this to work as dynamic function that could take input files and 
search string from the commandline. I tried 'input' and sys.argv[] functions to do that, but I kept getting error messages
I guess at this point I have exhausted my 'coding skills'

"""
def main():
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

if __name__ == '__main__':
    main()


