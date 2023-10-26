# 8. String to Integer (atoi) https://leetcode.com/problems/string-to-integer-atoi/
# Runtime: 36 ms
# Memory Usage: 14.2 MB
class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''
        sign = ''
        for i in s:
            if(i.isalpha()):  # whenever encountered any alphabet
                break

            if(i == ' '):
                if(len(res)):  # break if case like '454 3983' ==> 454
                    break
                if(sign != ''):  # return 0 for case: '   +  576' ==> 0
                    return 0
                continue  # Otherwise continue

            if(i == '+' or i == '-') and ((sign != '') or (len(res))):  # if sign encountered second time
                break
            elif(i == '+' or i == '-') and (sign == ''):  # if sign encountered first time
                sign = i
                continue

            res += i  # add numbers as a str

        try:
            # int->float->result for condition like: '3.1415'
            k = int(float(sign+res))
            return max(-2**31, min(k, 2**31-1))  # simple limit check
        except:
            return 0
