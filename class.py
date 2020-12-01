#while loop
'''desired_code = False
while not desired_code:
    code = input("Please enter 4 digits: ")
    if code == "1234":
        desired_code = True
        print("*******\nyou enter the right coode")
print("Thank you")
'''

#continue
'''num = False
while not num:
    a = int(input("Enter a number:"))
    if a<=10:
        continue
    else:
        num = True
'''

#break
sum = 0
for i in range(1,10):
    sum += i
    if i==3:
        break
print(sum)
