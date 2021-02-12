"""A vaccination calculator."""

__author__ = "730322809"
from datetime import datetime, timedelta
# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta


# Begin your solution here...
population: int = int(input("Population Considered"))
dosesgiven: int = int(input("Doses Administered"))
dpd: int = int(input("Doses Per Day"))
apv: int = int(dosesgiven / 2)
tpv: int = round(int(input("Target Percent Vaccinated")))
dr: int = round(float(((population * (tpv / 100)) - apv) / (dpd / 2)))

today: datetime = datetime.today()
one_day: timedelta = timedelta(dr)
t: datetime = today + one_day
final: str = str(t.strftime("%B %d, %Y")) + "."
print("We will reach " + str(tpv) + "% vaccination in " + str(dr) + " days, which falls on " + str(final))
