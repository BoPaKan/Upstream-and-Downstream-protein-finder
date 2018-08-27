# Upstream-and-Downstream-protein-finder
Two scripts and example data are added, which can be used to obtain upstream and downstream proteins and their sequences
for your protein of interest.

Files:

NCBI file contains NCBI accessions of proteins of interest as an example. Using them from NCBI Batch Entrez the sequence.gp (GenPept(full)) file was generated and using script NCBIDB.py from sequence.gp two files were created: DBSOURCE.txt (containing only DBSOURCE accessions for proteins of interest) and NCBIDBmap.txt (containing map between NCBI accessions and DBSOURCE accessions). The DBSOURCE.txt file was used to generate full genbank (sequence.gb) file using NCBI Batch Entrez. Files NCBIDBmap.txt and sequence.gb were used with a script UpDownProteins.py to find 10 downstream and 10 upstream proteins encoded in the surroundings of our proteins of interest and generate UpDownStreamProtein.txt file, which has an output in fasta format. The output format: protein of interest_its position (always 0)-protein in its surroundings_position relative to the protein of interest (negative numbers indicate that the protein is encoded downstream while positive numbers indicate that the protein is encoded upstream relative to the protein of interest) "\n" sequence of the surrounding protein. 
Example: 
>CTT04386_0-CTT04224_-8
MFVLIAGVNVHNEYYVNRIAGIAGYAGRVVELIDETTRKIDLLSDQERKKADVNDADIFLMLKAFVEMGFKISLHK
>CTT04386_0-CTT04254_-7
MVSYDKIRAEYRAKYRAYKLELIDDLIAQRDQLNFTFSDLLNSKRDCKRKREYLRLSALIGKLQNSI
