class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count =0
        x_binary = bin(x)[2:]
        y_binary = bin(y)[2:]
        if len(y_binary) != len(x_binary):
            for i in range(abs(len(y_binary) - len(x_binary))):
                if len(y_binary) > len(x_binary):
                    x_binary = "0"+x_binary
                else:
                    y_binary = "0"+y_binary
        for i in range(min(len(x_binary),len(x_binary))):
            if x_binary[i] != y_binary[i]:
                count+=1
        return count
