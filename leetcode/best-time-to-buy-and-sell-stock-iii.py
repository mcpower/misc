"""
WRONG
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
# Currently not working.
class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		best = 0
		curmin = 9e99
		for i in prices:
			curmin = min(curmin, i)
			best = max(best, i - curmin)
		return best
		
testFunction = Solution().maxProfit
expected = [
	[[[100, 150, 10, 61]], 51]
]

wellDone = True
for inp, out in expected:
	result = testFunction(*inp)
	if result != out:
		print "Test case {}, expecting {}, got {}".format(inp, out, result)
		wellDone = False
if wellDone:
	print "All test cases passed."