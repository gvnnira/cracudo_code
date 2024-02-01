#Problema Terreno
largura = int(input("Qual a largura do terreno? "))
comprimento = int(input("Qual o comprimento do terreno? "))
valor_metro = int(input("Qual o valor do metro quadrado? "))
area_terreno = largura * comprimento
preco_terreno = valor_metro * area_terreno
print(f"\nA área do terreno é de {area_terreno} metros quadrados "
      f"e o preço do terreno é de R${preco_terreno},00")