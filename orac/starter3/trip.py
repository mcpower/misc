a=map(int,open("tripin.txt").readlines())
z=[i for i in range(1,a[0]+1)if a[i]%3<1]
open("tripout.txt","w").write(["Nothing here!","%d\n%s"%(len(z)," ".join(map(str,z)))][len(z)>1])