"""
Transform data from qduoj to domjudge
"""
import os
import sys
from shutil import copyfile

def usage():
    print("USAGE:", sys.argv[0], "DATA_DIRECTORY [-spj]")
    exit()

def main():
    curp = 1
    names = {}
    ext_trans = {'.in': '.in', '.ans': '.out'}

    if len(sys.argv) not in [2, 3]: usage()
    if len(sys.argv) == 3 and sys.argv[2] == '-spj': del ext_trans['.ans']

    for p, _, flist in os.walk(sys.argv[1]):
        for f in flist:
            name, ext = os.path.splitext(f)
            if ext not in ext_trans: continue
            newext = ext_trans[ext]
            if not names.get(name):
                names[name] = curp
                curp += 1
            print("Copy %s to %s" % (os.path.join(p, f), str(names[name]) + newext))
            copyfile(os.path.join(p, f), str(names[name]) + newext)

if __name__ == '__main__':
    main()

