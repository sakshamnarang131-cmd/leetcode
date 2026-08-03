class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for ops in operations:
            if ops == "C":
                record.pop()
            elif ops == "D":
                record.append(int(2*record[len(record)-1]))
            elif ops == "+":
                record.append(int(record[len(record)-1] + record[len(record)-2]))
            else:
                record.append(int(ops))
        return sum(record)
