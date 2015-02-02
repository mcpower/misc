inp = open("rosalind_1b.txt").read().rstrip()
mapping = {"A": "T", "T": "A", "C": "G", "G": "C"}
print "".join(mapping[i] for i in reversed(inp))