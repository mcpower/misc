a=open("dictin.txt").readlines()
d=int(a[0].split()[0])+1
e=dict(z.split()for z in a[1:d])
open("dictout.txt","w").write("\n".join(e.get(i.strip(),"C?")for i in a[d:]))