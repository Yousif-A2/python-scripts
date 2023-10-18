words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense =[]
for i in words:
    x=len(i)-1
    if i[x] in "e":
        f = i+"d"
    else:
        f = i+"ed"
    past_tense.append(f)
print(past_tense)