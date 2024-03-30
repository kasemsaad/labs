num = eval(input("Enter a number: "))
countlms = 1
lms = []
while countlms <= num:
    count = 1
    lm = []
    while count <= countlms:
        lm.append(count * countlms)
        count += 1
    lms.append(lm)
    countlms += 1
print(lms)