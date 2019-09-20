def geo_hashing(num):
    start = -90
    end = 90
    
    code = ''
    for _ in range(6):
        mid = (start+end)//2
        if mid >= 0:
            if mid <= num:
                code += '1'
                start = mid
            else:
                code += '0'
                end = mid
        else:
            if mid < num:
                code += '1'
                start = mid
            else:
                code += '0'
                end = mid

    return code

N = int(input())
print(geo_hashing(N))