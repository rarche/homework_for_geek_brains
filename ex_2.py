time_user = int(input('Введите время в секундах: '))

time_hours = int(time_user // 3600)
time_minutes = int((time_user - (time_hours * 3600)) // 60)
time_seconds = time_user - time_hours * 3600 - time_minutes * 60

print (f"{time_hours:02}" + ":" + f"{time_minutes:02}" + ":" + f"{time_seconds:02}")
