def is_leap(year):
    leap = False
    isLeapBy400 = year % 400
    isLeapBy4 = year % 4
    isLeapUnless100 = year % 100
    if isLeapBy400 == 0:
        return True
    elif (isLeapBy4 == 0) and (isLeapUnless100 != 0):
        return True
    else:
        return leap

year = int(input())
print(is_leap(year))