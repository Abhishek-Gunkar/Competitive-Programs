def FindMaxSum(a, n):

	print(a)

	# if array length is one
	if n < 2:
		return a[0]

	# declaring array for storing
	dp = [0]*n

	# base conditions
	dp[0] = a[0]
	print("dp[0] : ", dp[0])

	dp[1] = max( a[0], a[1] )
	print("dp[1] : ", a[1])

	for i in range(2, n):
		dp[i] = max( dp[i-1], dp[i-2] + a[i] )
		print("dp[i] : ", dp[i])

	return dp[n-1]

res = FindMaxSum([5, 5, 10, 100, 10, 5], 6)

print(res)
