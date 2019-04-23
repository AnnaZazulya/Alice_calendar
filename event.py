from datetime import date

data = input().split()
today = date.today()
event = date(today.year, int(data[1]), int(data[0]))
if event < today:
    my_birthday = event.replace(year=today.year + 1)
time_to_birthday = abs(my_birthday - today)
print('До события:', time_to_birthday.days, 'дней')
