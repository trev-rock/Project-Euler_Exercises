import datetime # need to use datetime library 
sunday_counter = 0
for year in range(1901,2001): # range of years we need to check
    for month in range(1,13): # range of months in a year
        if datetime.datetime(year,month,1).weekday() == 6: # if the 1st of the month is on a sunday then we add it to the counter
            sunday_counter += 1
print(sunday_counter)