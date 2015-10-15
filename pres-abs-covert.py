import sys

for n, line in enumerate(open(sys.argv[1])):
    if n == 0:
        print line.rstrip()
    else:
        dat = line.rstrip().split('\t')
        for n2, x in enumerate(dat):
            if n2 == 0:
                continue
            else:
                x = int(x)
                if x > 0:
                    x = 1
                else:
                    x = 0
                dat[n2] = str(x)
        print '\t'.join(dat)
