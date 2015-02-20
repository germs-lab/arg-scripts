bash id-to-taxid.sh ncbi-ids-for-taxon.txt > taxon-map.txt
python taxon-to-text.py taxon-map.txt > taxon-list.txt
