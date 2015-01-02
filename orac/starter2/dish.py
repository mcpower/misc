a=map(int,open("dishin.txt").readlines()[1:])
open("dishout.txt","w").write("%d %d %d"%(min(a),max(a),sum(a)/len(a)))