datetime = input('输入年月日')
year, mon, day = int(datetime[:4:]), int(datetime[4:6:]), int(datetime[6::])
print(year, mon, day)
mon_list = [31,28,31,30,31,30,31,31,30,31,30,31]
days = day
if mon<=2:
    days += sum(mon_list[:mon-1:])
else:
    days += sum(mon_list[:mon-1:])
    if (year%400==0) or (year%4==0 and year%100!=0):
        days += 1

print(days)