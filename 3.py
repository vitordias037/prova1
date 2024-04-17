cat: str
valor : float

cat = input("digite a categoria do seu produto: A, B ou C: ")
valor = float(input("digite o preço do seu produto:"))

if cat == "A":
  R = (valor * 10)/ 100 
  print("o preço com desconto é R$:",valor - R)
elif cat == "B":
  R = (valor * 15)/ 100
  print("o preço com desconto é R$:",valor - R)  

else:
  R = (valor * 20)/ 100
  print("o preço com desconto é R$:",valor - R)

