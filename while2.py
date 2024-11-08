#take an input from a user go till that number and get the sum and print it 

a = int(input("Enter the number:"))
i = 1
sum = 0 
while(i <= a):
    sum += i 
    print(i)
    i += 1
print("The sum of the given number",a ,"is",sum)