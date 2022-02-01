class Solution(object):
    def romanToInt(self, s):
        sum_arr = sum([int(i) for i in s.replace('CM','900 ').replace('M','1000 ').replace('CD','400 ').replace('D','500 ').replace('XC','90 ').replace('C','100 ').replace('XL','40 ').replace('L','50 ').replace('IX','9 ').replace('X','10 ').replace('IV','4 ').replace('V','5 ').replace('I','1 ').split()])
        return sum_arr