dna_string = open("rosalind_revc.txt").read().rstrip()
compliment_mapping = dict(zip("GTCA", "CAGT"))
out = "".join(compliment_mapping[i] for i in reversed(dna_string))
print out
open("out_rosalind_revc.txt", "w").write(out)