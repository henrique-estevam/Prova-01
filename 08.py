texto = input("Digite o texto que deseja verificar: ");
valor = input("Digite a letra que deseja saber: ");

index = 0;

for letra in texto:
    if letra == valor:
        print(index);
        break 
    else: 
        index = index + 1;

if letra != valor: 
    print('-1');