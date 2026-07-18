class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a = []
        for i in range(left, right+1):
            num_str = str(i)
            num_list = list(num_str)
            print(num_list)
            c = 1
            if "0" in num_list:
                continue
            else:
                for j in range(len(num_list)):
                    if i % int(num_list[j]):
                        c = 0
                if c == 1:
                    a.append(i)
        return a
