"""A vaccination calculator."""

__author__ = "730322809"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population Considered"))
dosesgiven: int = int(input("Doses Administered"))
dpd: int = int(input("Doses Per Day"))
apv: int = dosesgiven / 2
tpv: int = round(int(input("Target Percent Vaccinated")))
daysremaining: int = round(((population * (tpv / 100)) - apv) / (dpd / 2))

from datetime import datetime, timedelta
today: datetime = datetime.today()
one_day: timedelta = timedelta(daysremaining)
tomorrow: datetime = today + one_day

print(tomorrow.strftime("%B %d, %Y")) 
print("We will reach " + str(tpv) + "% vaccination in " + str(daysremaining) + " days, which falls on " + str(tomorrow.strftime("%B %d, %Y")) + ".")


 


