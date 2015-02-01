from collections import Counter
dna_string, k = [line.strip() for line in open("rosalind_1a.txt").readlines()]
k = int(k)
d = Counter()

for i in xrange(len(dna_string) - k + 1):
	d[dna_string[i:i+k]] += 1
most_freq = d.most_common(1)[0][1]
out = []
for key, value in d.most_common():
	if value != most_freq:
		break
	out.append(key)
for kmer in out:
	print kmer,