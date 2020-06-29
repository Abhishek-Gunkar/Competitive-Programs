def equilibriumPoint(A, N):
	
	if len(A) == 1:
		return 1
		
	elif len(A) == 2:
		return -1
		
	else:
		
		left = 0
		right = 0
		total = sum(A)
		
		for i in range(1, N):
			
			left += A[i-1]	
			right = total - A[i] - left
			
			if left == right:
				return i+1
		else:
		    return -1

equilibriumPoint([1,8,2,4,5], 5)
