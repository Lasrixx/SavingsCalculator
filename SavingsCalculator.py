import math

class Solution:
    def number_of_days_to_save(self,moneySaved):
        if moneySaved < 0 or moneySaved > 74926:
            return -1
        if moneySaved == 0:
            return 0
        #Work out how many weeks it will
        #Take to accumulate the money
        #Then we can go back a week 
        #And work out how many days past
        #That last week it takes to get the money

        #moneySaved = 7/2 * w^2 + 49/2 * w
        #w = (-49+-(49^2-4*7*-2m)^0.5)/2*7
        a = 7
        b = 49
        c = -2*moneySaved
        d = (b**2) - (4*a*c)
        weeks = (-b+math.sqrt(d))/(2*a)
        print(weeks)

        #If money has been saved by the end of a week
        #We can return how many days have been in them weeks
        if weeks == int(weeks):
            return int(weeks*7)

        #If we have a decimal in the week,
        #We know that at some point during that
        #week we will hit the target amount
        #So can now iterate through the days
        #Using d+w (days+weeks) until the target 
        #is hit
        if int(weeks) == 0:
            amount = 0
        else:
            amount = (7*(int(weeks)**2)+49*int(weeks))/2
            print(amount)
        for d in range(1,8):
            amount+= d+int(weeks)
            if amount >= moneySaved:
                return 7*int(weeks)+d


sol = Solution()
print(sol.number_of_days_to_save(36))