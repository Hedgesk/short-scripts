class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        mult = 0 
        for i in range(0,len(num1)):
            for j in range(0,len(num2)):
               mult += (int(num1[len(num1) - i - 1]) * int(num2[len(num2) - j - 1])) * pow(10, i + j)
               
        return str(mult)