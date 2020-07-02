# Function should return an integer value
def convertFive(n):
    n = str(n)
    temp = ''
    for i in n:
        if i == '0':
            temp += '5'
        else:
            temp += i
    return temp
            
    # Code here

