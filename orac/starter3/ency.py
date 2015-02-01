a=open("encyin.txt").read().split()
b=int(a.pop(0))
open("encyout.txt","w").write("\n".join(a[i]for i in map(int,a[b+1:])))