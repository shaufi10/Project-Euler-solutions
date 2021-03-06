# 
# Solution to Project Euler problem 24
# by Project Nayuki
# 
# http://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import itertools, sys
if sys.version_info.major == 2:
    range = xrange


def compute():
	arr = list(range(10))
	permiter = itertools.permutations(arr)
	for i in range(999999):
		next(permiter)
	return "".join([str(x) for x in next(permiter)])


if __name__ == "__main__":
	print(compute())
