import datetime

given_date = datetime.datetime.fromisoformat('2022-05-14 20:34:13.212967')
requested_time = given_date.replace(year=given_date.year + 3)
print(requested_time)
