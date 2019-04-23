import datetime
import time
from enum import Enum

date = input().split()

months = {'янв': 31, 'фев': 28, 'мар': 31, 'апр': 30, 'май': 31, 'июн': 30,
          'июл': 30, 'авг': 31, 'сен': 30, 'окт': 31, 'ноя': 30, 'дек': 31,
          'января': 31, 'февраля': 28, 'марта': 31, 'апреля': 30, 'мая': 31, 'июня': 30,
          'июля': 30, 'августа': 31, 'сентября': 30, 'октября': 31, 'ноября': 30, 'декабря': 31,
          'январь': 31, 'февраль': 28, 'март': 31, 'апрель': 30, 'июнь': 30,
          'июль': 30, 'август': 31, 'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31}

name_month = {'янв': 'января', 'фев': 'февраля', 'мар': 'марта',
              'апр': 'апреля', 'май': 'мая', 'июн': 'июня',
              'июл': 'июля', 'авг': 'августа', 'сен': 'сентября',
              'окт': 'октября', 'ноя': 'ноября', 'дек': 'декабря',
              'январь': 'января', 'февраль': 'февраля', 'март': 'марта',
              'апрель': 'апреля', 'июнь': 'июня',
              'июль': 'июля', 'август': 'августа', 'сентябрь': 'сентября',
              'октябрь': 'октября', 'ноябрь': 'ноября', 'декабрь': 'декабря',
              'января': 'января', 'февраля': 'февраля', 'марта': 'марта',
              'апреля': 'апреля', 'мая': 'мая', 'июня': 'июня',
              'июля': 'июля', 'августа': 'августа', 'сентября': 'сентября',
              'октября': 'октября', 'ноября': 'ноября', 'декабря': 'декабря'}



that_year = datetime.datetime.today().year


def isint(s): # проверка на инт и стр
    try:
        int(s)
        return True
    except ValueError:
        return 'Не корректная запись'

def isstr(m): # проверка на инт и стр
    try:
        int(m)
        return 'Не корректная запись'
    except ValueError:
        return True


if int(date[0]) > 0 and date[1] in months:
    if isint(date[0]) == True and isstr(date[1]) == True:
        print('ok')
        if (2020 - datetime.datetime.today().year) % 4 != 0:
            print('високос')
            months["фев"] = 29
            months["февраль"] = 29
            months["февраля"] = 29
            if months[date[1]] >= int(date[0]):
                print('kruto')
            else:
                print('nene')

        else:
            print('невисокос')
    else:
        print('not srt or int')
else:
    print('date < 0 или нет значения в словаре')

print(isint(date[0]))
print(isstr(date[1]))
print(time.ctime())
print(months[date[1]])
a = 'https://ru.wikipedia.org/wiki/' + date[0] + '_' + name_month[date[1]]
print(a)
print('https://ru.wikipedia.org/wiki/' + date[0] + '_' + name_month[date[1]])

#>>> d1 = {"Russia":"Moscow", "USA":"Washington"}
#>>> d1["China"]="Beijing"
#>>> print(d1)
#{'Russia': 'Moscow', 'China': 'Beijing', 'USA': 'Washington'}