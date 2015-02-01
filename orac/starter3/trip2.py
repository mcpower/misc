a=map(int,open("tripin.txt").readlines())
z=[str(i)for i in range(1,a[0]+1)if a[i]%3<1]
open("tripout.txt","w").write("%d\n%s"%(len(z)," ".join(z))if z else"Nothing here!")