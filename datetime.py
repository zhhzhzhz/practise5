from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
delta

from datetime import timedelta
d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)

def pretty_timedelta(td):
    if td.days >= 0:
        return str(td)
    return f'-({-td!s})'

d = timedelta(hours=-1)
str(d)  # not human-friendly

pretty_timedelta(d) 

from datetime import timedelta
duration = timedelta(seconds=11235813)
duration.days, duration.seconds

duration.total_seconds()

from datetime import timedelta
year = timedelta(days=365)
ten_years = 10 * year
ten_years

ten_years.days // 365

nine_years = ten_years - year
nine_years

three_years = nine_years // 3
three_years, three_years.days // 365

from datetime import date
date.fromisoformat('2019-12-04')

date.fromisoformat('20191204')

date.fromisoformat('2021-W01-1')

from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001
d


# Methods related to formatting string output
d.isoformat()

d.strftime("%d/%m/%y")

d.strftime("%A %d. %B %Y")

d.ctime()

'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")


# Methods for extracting 'components' under different calendars
t = d.timetuple()
for i in t:
    print(i)









ic = d.isocalendar()
for i in ic:
    print(i)




# A date object is immutable; all operations produce a new object
d.replace(year=2005)