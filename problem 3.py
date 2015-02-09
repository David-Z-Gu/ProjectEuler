number = 600851475143
k = 0
number1 = number//2
for i in range (2, number1):
    while number % i == 0 and number > 0:
   
       k = i
       print(i)
       number = number / k