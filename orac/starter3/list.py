z,x,c=open("listin.txt").read().split()[1:],{},0
for i in z:
	x[i]=x.get(i,0)+1
print max(x.itervalues())
#open("listout.txt","w").write("\n".join())