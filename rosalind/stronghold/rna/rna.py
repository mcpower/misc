dna_string = open("rosalind_rna.txt").read().rstrip()
rna_string = dna_string.replace("T", "U")
print rna_string
open("out_rosalind_rna.txt", "w").write(rna_string)