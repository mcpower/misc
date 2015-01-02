a,i,s=open("rainin.txt").readlines(),0,0
x=int(a.pop(0).split()[1])
while s<x:s,i=s+int(a.pop(0)),i+1
open("rainout.txt","w").write(str(i))