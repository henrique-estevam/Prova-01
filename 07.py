def substituir_letra():
    texto = input("Digite a palavra: ");
        
    letra_m = input("Digite a letra que será substituida: ");
        
    letra_s = input("Digite a letra que substituirá a letra escolhida: ");
        
    lista_letras = [caractere for caractere in texto];
        
    palavras = [letra_s if caractere == letra_m else caractere for caractere in lista_letras];
        
    resultado = ''.join(palavras);
    
    print(resultado);

substituir_letra();