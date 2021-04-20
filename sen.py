# My name is Amir Ali Karimi
#This app determining age
# this app is based on the Gregorian calender
# mind that this program thinks that you where born at 00:00:00 
year_of_birth= int(input("sal tavalod khod ra vared konid"))
birth_month= int(input('mah tavalod khod ra vared konid'))
birthday= int(input("roz tavalod khod ra vared konid "))
import datetime
date_and_time = datetime.datetime.now()
year = (date_and_time.year)
month = (date_and_time.month)
day = (date_and_time.day)
hour = (date_and_time.hour)
minute = (date_and_time.minute)
second = (date_and_time.second)
if birth_month<= month :
    age_year = year - year_of_birth
    age_month = month - birth_month
else :
    age_year = (year - year_of_birth) - 1
    age_month = 12 + (month - birth_month)
    if birthday <=day :
      age_day = day - birthday
    else:
        age_day =  30 + (day - birthday)
        age_month = age_month - 1
age_hour = hour 
age_minute = minute 
age_second = second
print (age_year ,'years' ,age_month ,'months' ,age_day ,'days' ,
                age_hour ,'hours' ,age_minute ,'minutes' ,age_second ,'seconds')
