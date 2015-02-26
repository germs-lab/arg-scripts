import sys, screed

for record in screed.open(sys.argv[1]):
    if len(record.name.split('_')[0]) < 5:
        print record.name.split('_')[0] + "_" + record.name.split('_')[1]
    else:
        print record.name.split('_')[0]


