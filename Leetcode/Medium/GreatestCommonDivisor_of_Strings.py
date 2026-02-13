import math
def Gcd(string1,string2):
    if string1+string2!=string2+string1:
        return "No common divisor"
    x=math.gcd(len(string1),len(string2))
    return string1[:x]

string1="ababab"
string2="abab"
result=Gcd(string1,string2)
print(result)


'''Time Complexity for brute force method is O(min(n,m)*(n+m))
The efficient one is check -> O(n+m) , GCD -> O(log(min(n,m))), Slice -> O(x) so final time complexity is O(n+m) '''

