def removeDuplicates(arr):
 
    hashed = dict()
    dup = list()
    
    for a in arr:
        hashed[a] = None
    
    for a in arr:
        if hashed[a] == None:
            hashed[a] = 1
        
        elif hashed[a] == 1:
            dup.append(a)
    arr.reverse()
   
                    
    for a in dup:
        arr.remove(a)
    
    arr.reverse()
    
    return arr
    
    

print(removeDuplicates([2,2,3,3,7,5]))
