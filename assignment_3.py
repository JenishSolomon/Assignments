#Enter the range of fibonacci series

a = int(input("Enter the Range Number: "))

b = 0

c = 1

for num in range(0, a):
           if(num <= 1):
                      d = num
           else:
                      d = b + c
                      b = c
                      c = d
           print(d)
