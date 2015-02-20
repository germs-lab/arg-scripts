import sys, screed

for record in screed.open(sys.argv[1]):
    print record.name


