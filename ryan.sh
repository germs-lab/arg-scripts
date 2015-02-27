for x in *blastxout; do python blast-m8-parser-best.py $x > $x.besthits; done
python count-up.py *besthits
cut -k 1 summary-count.tsv > gene-ids.txt
bash id-to-taxid.sh gene-ids.txt > taxon-map.txt
python taxon-to-text.py taxon-map.txt > taxon-list.txt