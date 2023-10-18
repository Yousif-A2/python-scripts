amount = int(input("please enter amount?"))

if amount>0 and amount<1000:
	discount = amount*  (5/100)
	final_amount = amount -discount
	print(final_amount)
elif amount>=1000 and amount<=5000 :
	discount= amount * (10/100)
	final_amount= amount- discount
	print(final_amount)

elif amount>5000:
	discount= amount*(15/100)
	final_amount= amount- discount
	print(final_amount)
else:
	print("enter corrent number")
	