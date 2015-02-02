pattern, genome = [line.strip() for line in open("rosalind_1c.txt").readlines()]
out = []
k = len(pattern)
for i in xrange(len(genome) - k + 1):
	if genome[i:i+k] == pattern:
		print i,
		out.append(i)
open("rosalind_1c_out.txt", "w").write(" ".join(map(str, out)))