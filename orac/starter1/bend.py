z,p,m,n=open("bendin.txt").readlines(),lambda x:(x[2]-x[0])*(x[3]-x[1]),0,0
a,b=[map(int,z[i].split())for i in 0,1]
open("bendout.txt","w").write(str(p(a)+p(b)-max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))))