import datetime
import time
from datetime import date

data = input().split()
print(data)

months = {'янв': 31, 'фев': 28, 'мар': 31, 'апр': 30, 'май': 31, 'июн': 30,
          'июл': 30, 'авг': 31, 'сен': 30, 'окт': 31, 'ноя': 30, 'дек': 31,
          'января': 31, 'февраля': 28, 'марта': 31, 'апреля': 30, 'мая': 31, 'июня': 30,
          'июля': 30, 'августа': 31, 'сентября': 30, 'октября': 31, 'ноября': 30, 'декабря': 31,
          'январь': 31, 'февраль': 28, 'март': 31, 'апрель': 30, 'июнь': 30,
          'июль': 30, 'август': 31, 'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31}

name_month = {'янв': '%D1%8F%D0%BD%D0%B2%D0%B0%D1%80%D1%8F', 'фев': '%D1%84%D0%B5%D0%B2%D1%80%D0%B0%D0%BB%D1%8F',
              'мар': '%D0%BC%D0%B0%D1%80%D1%82%D0%B0', 'апр': '%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F',
              'май': '%D0%BC%D0%B0%D1%8F', 'июн': '%D0%B8%D1%8E%D0%BD%D1%8F',
              'июл': '%D0%B8%D1%8E%D0%BB%D1%8F', 'авг': '%D0%B0%D0%B2%D0%B3%D1%83%D1%81%D1%82%D0%B0',
              'сен': '%D1%81%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8F',
              'окт': '%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F',
              'ноя': '%D0%BD%D0%BE%D1%8F%D0%B1%D1%80%D1%8F', 'дек': '%D0%B4%D0%B5%D0%BA%D0%B0%D0%B1%D1%80%D1%8F',
              'январь': '%D1%8F%D0%BD%D0%B2%D0%B0%D1%80%D1%8F', 'февраль': '%D1%84%D0%B5%D0%B2%D1%80%D0%B0%D0%BB%D1%8F',
              'март': '%D0%BC%D0%B0%D1%80%D1%82%D0%B0', 'апрель': '%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F',
              'июнь': '%D0%B8%D1%8E%D0%BD%D1%8F', 'июль': '%D0%B8%D1%8E%D0%BB%D1%8F',
              'август': '%D0%B0%D0%B2%D0%B3%D1%83%D1%81%D1%82%D0%B0',
              'сентябрь': '%D1%81%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8F',
              'окттябрь': '%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F',
              'ноябрь': '%D0%BD%D0%BE%D1%8F%D0%B1%D1%80%D1%8F', 'декабрь': '%D0%B4%D0%B5%D0%BA%D0%B0%D0%B1%D1%80%D1%8F',
              'января': '%D1%8F%D0%BD%D0%B2%D0%B0%D1%80%D1%8F', 'февраля': '%D1%84%D0%B5%D0%B2%D1%80%D0%B0%D0%BB%D1%8F',
              'марта': '%D0%BC%D0%B0%D1%80%D1%82%D0%B0', 'апреля': '%D0%B0%D0%BF%D1%80%D0%B5%D0%BB%D1%8F',
              'мая': '%D0%BC%D0%B0%D1%8F', 'июня': '%D0%B8%D1%8E%D0%BD%D1%8F',
              'июля': '%D0%B8%D1%8E%D0%BB%D1%8F', 'августа': '%D0%B0%D0%B2%D0%B3%D1%83%D1%81%D1%82%D0%B0',
              'сентября': '%D1%81%D0%B5%D0%BD%D1%82%D1%8F%D0%B1%D1%80%D1%8F',
              'октяьря': '%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F',
              'ноября': '%D0%BD%D0%BE%D1%8F%D0%B1%D1%80%D1%8F',
              'декабря': '%D0%B4%D0%B5%D0%BA%D0%B0%D0%B1%D1%80%D1%8F',}

count_months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'июн': 6,
                'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12,
                'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
                'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12,
                'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'июнь': 6,
                'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12}

that_year = datetime.datetime.today().year


# проверка на инт числа


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return 'Не корректная запись'

# проверка на стр месяца


def isstr(m):
    try:
        int(m)
        return 'Не корректная запись'
    except ValueError:
        return True


# проверка на високосный или невисокосный год
if (2020 - that_year) % 4 == 0:
    print('високос')
    months["фев"], months["февраль"], months["февраля"] = 29, 29, 29
else:
    print('невисокос')


if len(data) == 3:
    if 'до' in data:
        data.remove('до')
    else:
        data.remove('До')
    today = date.today()
    event = date(today.year, count_months[data[1]], int(data[0]))
    if event < today:
        my_event = event.replace(year=today.year + 1)
    time_to_event = abs(my_event - today)
    print('До события:', time_to_event.days, 'дней')
else:
    if int(data[-0]) > 0 and data[-1] in months:
        if isint(data[-0]) == True and isstr(data[-1]) == True:
            if months[data[-1]] >= int(data[-0]):
                print('https://ru.wikipedia.org/wiki/' + data[-0] + '_' + name_month[data[-1]])
            else:
                print('нету таких дат')
        else:
            print('not srt or int')
    else:
        print('data < 0 или нет значения в словаре')


#print(time.ctime())
#print(months[data[1]])


