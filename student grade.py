pass_grade = ['a','b','c','d']

failed = 'F'

grade = input("Please Enter your grade:")

if grade.lower() or grade.upper() in pass_grade:
	print("congratulation")
elif grade.lower() == failed or grade.upper() == failed:
	print(" you have failed the course")
else: 
	print("Please enter correct grade")