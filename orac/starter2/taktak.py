a,b=0,int(open("taktakin.txt").read())
while b%11!=1:a,b=a+1,b*2
open("taktakout.txt","w").write("%d %d"%(a,b))