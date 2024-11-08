#take an input and reverse it using while loop

num = int(input("Enter the number:"))
temp = num  
result = 0 
 
while temp > 0: 
    digit = temp % 10
    result = (result * 10)+ digit 
    temp //= 10  
    
print(f" The reversed number is {result}")