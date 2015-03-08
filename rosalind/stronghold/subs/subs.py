s,t = open("rosalind_subs.txt").read().split()
for i in xrange(len(s) - len(t)):
	if s[i:i+len(t)] == t:
		print i+1,