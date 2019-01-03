ans = 0
now = 1
for year in range(1900, 2001):
    for month in range(1,13):
        if now == 0:
            if not year == 1900:
                ans += 1
        if month == 2:
            if ( not year%400 == 0) and (year%100 == 0):
                day = 28
            elif year%4 == 0:
                day = 29
            else:
                day = 28
        elif month in [4,6,9,11]:
            day = 30
        else:
            day = 31
        now = (now+day)%7
print(ans)
