import sys

d = {}

for line in open("taxon-map.txt"):
    dat = line.rstrip().split('\t')
    ncbi_id = dat[0]
    tax_id = dat[1]
    d[ncbi_id] = tax_id

d2 = {}
for line in open("taxon-list.txt"):
    dat = line.rstrip().split(';')
    d2[dat[0]] = dat[1:]

for x in d.keys():
    print x + '\t' + '\t'.join(d2[d[x]])
    
