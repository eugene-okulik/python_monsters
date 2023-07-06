import datetime

current_day = datetime.datetime.now()
# print(current_day)
requested_day = datetime.datetime.fromisoformat('2023-06-12 15:23:45.312167')
print(current_day - requested_day)
