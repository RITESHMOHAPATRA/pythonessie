#!/usr/bin/python2.7

import time
import os
import sys

print "Starting..."

def bar():
    toolbar_width = 40
    
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))

    for i in xrange(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("\n")

def main():
    pos = os.getcwd()
    files = os.listdir(".")
    bar()
    for f in files: 
        if os.access(f, os.F_OK):
            print "%r Exists" % f
        if os.access(f, os.R_OK):
            print "Reading %r: Allowed" % f
        if os.access(f, os.W_OK):
            print "Writting % r: Allowed" % f
        if os.access(f, os.X_OK):
            print "Executing %r: Allowed" % f 
    # os.chroot("/root")
    # os.rename('3.txt', '1.txt')
    # print files
    os.chdir('/root')
    print os.getcwd()

if __name__ == "__main__":
    main()



