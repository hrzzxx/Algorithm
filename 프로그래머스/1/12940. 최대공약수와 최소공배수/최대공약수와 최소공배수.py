def gcd(a,b):
    if not b: return a
    else: return gcd(b,a%b)
def lcm(a,b):
    gcd_ = gcd(a,b)
    return (a*b) // gcd_
def solution(a,b):
    gcd_ = gcd(a,b)
    answer = [gcd_, (a*b) // gcd_]
    return answer