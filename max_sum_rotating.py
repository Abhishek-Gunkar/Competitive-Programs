def max_sum(arr,n):
    
    maxo = 0
    
    
    for a in range(n):
        sum = 0
        res = rotateArr(arr, 1, len(arr))
        
        for i in range(len(arr)):
            sum += i * arr[i]
        if sum > maxo:
            maxo = sum
    return maxo
    
        
def max_sum_pro(a, n):
	
	cum_sum = 0  # variable for sum up just elements

	for i in range(0,n):
		cum_sum = cum_sum+a[i] # just elements value summed
		
	initial_value = 0	# for index * element sum
	mx = 0	# maximum sum

	for i in range(0, n):
		initial_value += i*a[i] # index * element sum
		mx = initial_value # max has initial value sum - above one

	for i in range(1, n):
		temp = initial_value - (cum_sum-a[i-1]) + a[i-1]*(n-1)
		initial_value = temp
		
		if (temp > mx):
			mx = temp
	return mx
    
print( max_sum_pro([1,2,3,4],4))
