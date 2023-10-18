sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
list = sentence.split()

for i in list:
   # print(i)
    x = len(i)
    if i[0]==i[x-1]:
        same_letter_count+=1
    print(same_letter_count)
