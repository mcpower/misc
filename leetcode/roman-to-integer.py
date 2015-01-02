"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
	# @return an integer
	def romanToInt(self, s):
		mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		nums = map(lambda x: mapping[x], s)
		previous = 9001
		out = 0
		for num in nums:
			if num > previous:
				out -= previous * 2 # oh god why
			out += num
			previous = num
		return out

	def romanToInt2(self, s):
		mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
		nums = map(lambda x: mapping[x], s)
		previous = -1
		out = 0
		for num in reversed(nums):
			if num >= previous:
				out += num
			else:
				out -= num
			previous = num
		return out
		

testFunction = Solution().romanToInt2
expected = {
	("IX",): 9,
	("MCMLIV",): 1954,
	("MCMXC",): 1990,
	("MMXIV",): 2014,
	("XXII",): 22
}

wellDone = True
for inp, out in expected.iteritems():
	result = testFunction(*inp)
	if result != out:
		print "Test case {}, expecting {}, got {}".format(inp, out, result)
		wellDone = False
if wellDone:
	print "All test cases passed."