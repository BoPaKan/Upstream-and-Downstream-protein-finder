
""" This script is used to parse GenPept(full) file to produce two files:
1. file containing map between NCBI ID's and DBSOURCE accessions used in UpDownProteins.py script
2. file containing only DBSOURCE accessions (this file will be used to download genbank files). """

f_out1 = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/NCBIDBmap.txt","w")
f_out2 = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/DBSOURCE.txt","w")

fa = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/sequence.gp")
lines = fa.readlines()
for line in lines:
    if line.find("LOCUS")!=-1:
        NCBI = line.split("       ")[1]
        f_out1.write(NCBI + "\t")
    if line.find("DBSOURCE")!=-1:
        DBSOURCE = line.split("accession ")[1]
        f_out1.write(DBSOURCE)
        f_out2.write(DBSOURCE)
fa.close()
f_out1.close()
f_out2.close()
