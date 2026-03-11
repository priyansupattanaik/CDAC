#Employee bonus calculation. 
#If Experience >= 5 years & performance rating rating >= 4. then bonus is 4%.
#If Experince >=4 years & performance rating >= 3. then bonus is 3%.
#otherwise bonus is 0.

salary = int(input("Salary: "))
exp = float(input("Experience: "))
perf = float(input("Performance: "))

if exp >= 5 and perf >= 4:
    bonus = salary * 0.04
elif exp >= 4 and perf >= 3:
    bonus = salary * 0.03
else:
    bonus = 0

print("Bonus amount: ", bonus)
