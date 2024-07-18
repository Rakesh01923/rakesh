n = int(input("Enter a number: "))

count = 0
first = 0
second = 1
temp = 0
fact = 1

for i in range(1,n+1):
    fact *= i
print("FACTORIAL:",fact)

print(first)
while(count<fact-1):
        first = second
        second = temp
        temp = first+second
        count += 1
        print(temp)


