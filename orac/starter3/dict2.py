# based off partinallyinfinite's codegolf
a=map(str.split,open("dictin.txt").readlines())
d=int(a[0][0])+1
e=dict(a[1:d])
open("dictout.txt","w").write("\n".join(e.get(i[0].strip(),"C?")for i in a[d:]))