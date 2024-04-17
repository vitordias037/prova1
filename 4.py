num: int
num2: int
num3: int

num = int(input("digite o primeiro numero:"))
num2 = int(input("digite o segundo numero:"))
num3 = int(input("digite o terceiro numero:"))
                          
if (num <= num2) and num2 <= num3:
  print("o do meio é:" ,num2)
  # numero 1 menor que numero 2 e 2 menor 3
elif (num >= num2) and num <=num3:
  # quando 1 e maior que 2 e 1 menor que 3
  print("o do meio é:" ,num)  
elif (num >= num2) and num2 >= num3:
  # quando 1 e maior que 2 e 2 maior que 3
  print("o do meio é:" ,num2)
elif (num > num3) and num < num2:
  # quando 1 e maior que 3 e 1 menor q 2
  print("o do meio é:" ,num)
elif (num < num3) and num > num2:
  # quando 1 e menor que 3 e 1 maior q 2
  print("o do meio é:" ,num)     

else:
  print("o do meio é:" ,num3)
  
 

