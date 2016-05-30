#!/usr/bin/env python
#
import difflib
import sys


def file(filename):
    try:
        f = open(filename)
        text = f.read().splitlines()
        f.close()
        return text
    except IOError as error:
        print 'read file error:',str(error)
        sys.exit()

if __name__ == '__main__':
    try:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
    except Exception,e:
        print 'Error:'+str(e)
        print 'Usage:file_diff.py filename1 filename2'
        sys.exit()
    
    if filename1 == '' or filename2 == '':
        print 'Usage:file_diff.py filename1 filename2'
        sys.exit()
    

    text1 = file(filename1)
    text2 = file(filename2)
    
    d = difflib.HtmlDiff()
    print d.make_file(text1,text2) 

