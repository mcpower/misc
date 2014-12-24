"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

	1 -> A
	2 -> B
	3 -> C
	...
	26 -> Z
	27 -> AA
	28 -> AB 
"""


class Solution:
	# @return a string
	def convertToTitle(self, num):
		out, cur = [], num
		while cur != 0:
			cur, letter = divmod(cur, 26)
			if cur != 0 and letter == 0:
				cur -= 1
				letter += 26
			out.append(chr(letter + 64))
		return "".join(reversed(out))

testFunction = Solution().convertToTitle
expected = {
	(1,): "A",
	(26,): "Z",
	(27,): "AA",
	(28,): "AB",
	(26*2,): "AZ"
}

wellDone = True
for inp, out in expected.iteritems():
	result = testFunction(*inp)
	if result != out:
		print "Test case {}, expecting {}, got {}".format(inp, out, result)
		wellDone = False
if wellDone:
	print "All test cases passed."