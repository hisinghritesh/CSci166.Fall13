from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hr = now.hour
mn = now.minute
sc = now.second
print str(month) +  '/' + str(day) + \
   '/' + str(year) + ' ' + str(hr) +':' \
   + str(mn) + ':' + str(sc)
