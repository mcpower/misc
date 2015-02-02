from __future__ import division
"""
homo dom - homo dom = 100%
homo dom - hetero = 100%
homo dom - homo rec = 100%

hetero - homo dom = 100%
hetero - hetero = 75%
hetero - homo rec = 50%

homo rec - homo dom = 100%
homo rec - hetero = 50%
homo rec - homo rec = 0%
"""

k, m, n = [int(i) for i in open("rosalind_iprb.txt").read().split()]
pop = k + m + n
print (k / pop) + ((m * (k + 0.75 * (m - 1) + 0.5 * n)) / (pop * (pop - 1))) + ((n * (k + 0.5 * m)) / (pop * (pop - 1)))