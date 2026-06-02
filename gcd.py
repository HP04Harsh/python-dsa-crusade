# GCD of Two Numbers

class Solution:
    def gcd(self, a: int, b: int) -> int:
       while b==0:
         return a
       return self.gcd(b, a%b)  
          

    def lcm(self, a: int, b: int) -> int:
        return a*b // self.gcd(a, b)   