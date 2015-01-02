"""
UNFINISHED
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array. 
"""


class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        

testFunction = Solution().majorityElement
expected = {
	([1,2,3,4,1,1,1],): 1,
	([1,1,])
}

wellDone = True
for inp, out in expected.iteritems():
	result = testFunction(*inp)
	if result != out:
		print "Test case {}, expecting {}, got {}".format(inp, out, result)
		wellDone = False
if wellDone:
	print "All test cases passed."