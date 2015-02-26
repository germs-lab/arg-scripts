import sys
import os
import json
import urllib
import subprocess

def taxid_to_taxonomy(taxid):
    url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=" + taxid + "&retmode=xml"
    proc = subprocess.Popen(["curl", url], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()

    l = []
    for line in out.split('\n'):
        if line.strip().startswith("<ScientificName>"):
            dat = line.strip().split('<ScientificName>')[1].split('</ScientificName>')[0]
            l.append(dat)
    l.insert(0, taxid)
    taxonomy = ';'.join(l)
    return(taxonomy)

for line in open(sys.argv[1]):
    line = line.rstrip().split('\t')
    taxid = line[1]
    taxonomy = taxid_to_taxonomy(str(taxid))
    print taxonomy
