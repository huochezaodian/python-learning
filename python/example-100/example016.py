#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

format = '%d/%m/%Y'

if __name__ == '__main__':
    print(datetime.date.today().strftime(format))

    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime(format))

    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime(format))

    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime(format))