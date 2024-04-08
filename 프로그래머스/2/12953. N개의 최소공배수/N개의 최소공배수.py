def gcd(a,b):
    if b == 0: return a
    else: return gcd(b, a%b)
def solution(arr):
    answer = 0
    arr.sort()
    gcd_ = arr[0]
    lcm = arr[0]
    for i in arr[1:]:
        gcd_ = gcd(lcm, i)
        lcm = (i*lcm) // gcd_
    return lcm