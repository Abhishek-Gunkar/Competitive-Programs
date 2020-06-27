def duplicates(arr, n):
    hashmap = dict()
    setter = set()
    
    for a in arr:
    	hashmap[a] = None

    for a in arr:
    	if hashmap[a] == None:
    		hashmap[a] = 1
    
    	elif hashmap[a] == 1:
    		setter.add(a)
    
    
    if len(setter) == 0:
    	return [-1]
    else:
        l = list(setter)
        l.sort()
        return l




arr = list(map(int, input().split()))

print( duplicates(arr, len(arr)) )
