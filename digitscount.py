# Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        rev = 0
        count = 0

        while num>0:
            rev = num%10
            num = num//10

            if rev != 0 and num%rev == 0:
                count += 1
        return count