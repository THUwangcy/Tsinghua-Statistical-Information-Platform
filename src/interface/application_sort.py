import math
import datetime


def get_now_time():
    date_time = datetime.datetime.now()
    return date_time


def count_time_gap(datestr):
    d1 = datetime.datetime.strptime(datestr, '%Y.%m.%d')
    return (get_now_time() - d1).days


def application_sort(applications):

    sorted_applications = []
    applications.sort(key=lambda k: (k.get('fillin', 0)), reverse=True)

    for app in applications:
        if count_time_gap(app['subscribe_time']) <= 7 and len(sorted_applications) < 10:
            sorted_applications.append(app)
        elif len(sorted_applications) >= 10:
            break

    return sorted_applications
