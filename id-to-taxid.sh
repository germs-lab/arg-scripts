#from biostars 10959
readarray a < $1

for ACC in ${a[*]}
do
   echo -n -e "$ACC\t"
   curl -s "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=${ACC}&rettype=fasta&retmode=xml" |\
   grep TSeq_taxid |\
   cut -d '>' -f 2 |\
   cut -d '<' -f 1 |\
   tr -d "\n"
   echo
 done