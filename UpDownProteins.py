""" This script is used to find 10 downstream and 10 upstream encoded proteins surrounding your protein of interest
(protein of interest must be given in file format: protein of interest NCBI accession "\t" DBSOURCE accession,
as in example file (NCBIDBmap.txt) this file can be generated using script NCBIDB.py from GenPept(full) file (sequence.gp in this example)).
If there are less than 10 downstream or upstream proteins the maximum number of surrounding proteins will be given.
This script also needs full genbank file generated by using NCBI Batch Entrez and your proteins of interest DBSOURCE accessions
(sequence.gb file in this example, DBSOURCE accessions are in file DBSOURCE.txt and it can be generated from GenPept(full) file using NCBIDB.py script).
The output produced is in fasta format. 
>protein of interest id_its position (always 0)-protein in its surroundings_its position (numbers indicate relative position to the protein of interest,
positive numbers indicate that the protein is upstream while negative numbers indicates that the protein is downstream relative to the protein of interest)
"\n" surrounding protein sequence. """

from collections import defaultdict

DB_PROT = defaultdict(list) # key is DBSOURCE accession and value is NCBI ID of our protein of interest (protein of which we want
# to find downstream and upstream encoded proteins). defaultdict is used because some proteins of interest might share DBSOURCE accession.

fa = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/NCBIDBmap.txt")
lines = fa.readlines()
for line in lines:
    NCB = line.split("\t")[0]
    DB = line.split("\t")[1]
    DB = DB.split(".")[0]
    DB = DB.replace(" ","")
    DB_PROT.setdefault(DB, []).append(NCB)
fa.close()

pID_seq = {} # key is protein ID and value is it's sequence

fb = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/sequence.gb")
lines = fb.readlines()
sw1 = "off"
for line in lines:
    if line.find("/protein_id=")!=-1:
        id_p = line.split("/protein_id=")[1]
        id_p = id_p.replace('"',"")
        id_p = id_p.split(".")[0]
    if line.find("/translation=")!=-1:
        sw1 = "on"
        seq = []
    if sw1 == "on":
        seq.append(line)
    if line.find('"\n')!=-1 and sw1 == "on":
        sw1 = "off"
        sequence = "\n".join(seq)
        sequence = sequence.replace('/translation="',"")
        sequence = sequence.replace("\n","")
        sequence = sequence.replace("                     ","")
        sequence = sequence.replace('"',"")
        pID_seq[id_p] = (sequence)
fb.close()

DB_SUR = defaultdict(list) # key is DBSOURCE accession and values are all proteins encoded in that locus (DBSOURCE accession)

fc = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/sequence.gb")
lines = fc.readlines()
sw2 = "off"
for line in lines:
    if line.find("LOCUS       ")!=-1:
        locus = line.split("       ")[1]
        if locus not in DB_SUR.keys():
            sw2 = "on"
    if line.find("/protein_id=")!=-1 and sw2 == "on": 
        id_ = line.split("/protein_id=")[1]
        id_ = id_.replace('"',"")
        id_ = id_.split(".")[0]
        DB_SUR.setdefault(locus, []).append(id_)
    if line.find("ORIGIN")!=-1:
        sw2 = "off"
fc.close()

f_out = open("/home/paulius/BIOINFORMATICS/GitHub/UDencodedProteins/UpDownStreamProteins.txt","w")

for key in DB_SUR.keys():
    pid = DB_PROT[key] # gives id of protein of our interest in that specific locus
    for x in pid:
        position_pid = DB_SUR[key].index(x) # gives position of protein of our interest in locus
        position_0 = position_pid - position_pid
        prot_int = x + "_" + str(position_0)
        down = position_pid - 10 # we set the lowest protein position that interests us in the locus
        up = position_pid + 11 # we set the highest protein position that interests us in the locus
        if position_pid == 0: # if there are no downstream proteins the down position is set to zero
            down = 0
        if position_pid < 10: # if there are less than 10 downstream proteins the down position is set to zero
            down = 0
        UpDown = DB_SUR[key][down:up] # upstream and downstream interval around our protein of interest
        for prot in UpDown:
            position = DB_SUR[key].index(prot)
            position = position - position_pid
            prot_up_down = prot + "_" + str(position)
            prot_seq = pID_seq[prot]
            f_out.write(">" + x + "_" + str(position_0) + "-" + prot_up_down + "\n" + prot_seq + "\n")
f_out.close()




