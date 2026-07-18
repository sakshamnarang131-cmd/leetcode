class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        month_codes = [0,3,3,6,1,4,6,2,5,0,3,5]
        month_code = month_codes[month - 1]
        if year%4==0 and year!=2100:
            if month == 1:
                month_code = 6
            elif month == 2:
                month_code = 2
        # else:
        #     if month == 1:
        #         month_code = 0
        #     elif month == 2:
        #         month_code = 3
        # if month == 3 or month == 11:
        #     month_code = 3
        # elif month == 4 or month == 7:
        #     month_code = 6
        # elif month == 5:
        #     month_code = 1
        # elif month == 6:
        #     month_code = 4
        # elif month == 8:
        #     month_code = 2
        # elif month == 9 or month == 12:
        #     month_code = 5
        # elif month == 10:
        #     month_code = 0
        
        if year <2000:
            year_code = ((year%100) + (year%100)//4)%7
        elif year == 2100:
            year_code = 4
        else:
            year_code = ((year%100) + (year%100)//4 + 6)%7
        weekday_value = (day + month_code + year_code) % 7
        a = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return a[weekday_value]
