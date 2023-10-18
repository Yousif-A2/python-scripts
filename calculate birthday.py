import datetime 
#from datetime import datetime,date 

year = int( input("Please Enter The Year?"))
month= int( input("Please Enter The month?"))
day= int( input("Please Enter The day?"))

today_date = datetime.datetime.now()
#print(today_date)

today_date_only_date = datetime.datetime.today()
#print(today_date_only_date)

DOB = datetime.datetime(year,month,day)
#print(DOB)

age = (today_date - DOB)/365

print("your age is",age.days)



#print(type(year))