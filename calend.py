#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from datetime import datetime, timedelta


def to_month(number):
    months = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    return(months[number])


def to_week_day(number):
    week_days = ["", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", 
                 "Суббота", "Воскресение"]
    return(week_days[number])


def conky_cal(arg):
    '''
        There are 6 types:
            - "left_month",
            - "right_month",
            - "left_days",
            - "right_days",
            - "current_day",
            - "week_day" 
    '''
    raz = 31
    half = raz // 2

    results = dict()

    td = datetime.today()
    results['current_day'] = str(td.day)
    results['week_day'] = to_week_day(td.isoweekday())
    past_days = ''
    next_days = ''
    for num_day in range(1, half+1):
        left_days = td-timedelta(days=num_day)
        right_days = td+timedelta(days=(half+1-num_day))

        next_days = str(right_days.day)+' '+next_days
        past_days = str(left_days.day)+' '+past_days

        results['left_days'] = past_days
        results['right_days'] = next_days

        if num_day == half:
            results['left_month'] = to_month(left_days.month)
            results['right_month'] = to_month(right_days.month)
    return results[arg]

if __name__ == '__main__':
    try:
        print(conky_cal(sys.argv[1]))
    except Exception:
        print('No argument')