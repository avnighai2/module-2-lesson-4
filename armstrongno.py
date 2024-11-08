
a = int(input("Enter the number: "))

temp = a 
numdigits = len(str(a))
sumofpowers = 0
i = 0 
while i < 3:
    digit = temp % 10
    sumofpowers += digit ** 3
    temp //= 10
    i += 1

if sumofpowers == a:
    print(f"The number {a} is an armstrong number ")
else:
    print(f"The number {a} is not an armstrong number ")