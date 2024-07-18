n = int(input("Enter a number:"))

print("Prime Number:")
i=2
end = 0
while(i):
    if(end == n):
        break
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        end += 1
    i+=1
