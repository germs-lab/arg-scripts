import sys

d_gene = {}

for f in sys.argv[1:]:
    for line in open(f):
        dat = line.rstrip().split('\t')
        query = dat[0]
        gene = dat[1]
        if d_gene.has_key(gene):
            d_gene[gene][query] = d_gene[gene].get(query,0) + 1
        else:
            d_gene[gene] = {}
            d_gene[gene][query] = 1

fp = open('summary-count.tsv', 'w')

gene_list = set()
for gene in d_gene:
    for x in d_gene[gene]:
        gene_list.add(x)

for x in sorted(gene_list):
    fp.write('\t%s' % x.split('.')[0])
fp.write('\n')

gene_list_sorted = sorted(gene_list)

for gene in d_gene:
    fp.write('%s\t' % gene)
    for x in gene_list_sorted:
        x1 = x.split('.')[0]
        if d_gene[gene].has_key(x1):
            fp.write('%s\t' % d_gene[gene][x1])
        else:
            fp.write('0\t')
    fp.write('\n')




