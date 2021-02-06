from datetime import datetime, timedelta
today: datetime = datetime.today()
print(today.strftime("%B,%d, %Y"))
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
print(tomorrow.strftime("%B %d, %Y")) 
